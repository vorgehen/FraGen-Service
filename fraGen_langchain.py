#!/usr/bin/env python
# coding: utf-8
import json

import toml
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from langchain_community.document_loaders import WikipediaLoader, Docx2txtLoader, PyPDFLoader, TextLoader

import chromadb
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

config = toml.load("fraGen_service_config.toml")
env = config["SETUP"]["env"]


OPENAI_API_KEY = config["PROJECT"][env]["openAIKey"]

## Setting up vector database and embeddings

# TODO embedding model konfigurierbar machen
embedding_function = OpenAIEmbeddings(model="text-embedding-3-large", openai_api_key=OPENAI_API_KEY)

def document_to_collection(document_name:str) :
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=120, chunk_overlap=0)
    vector_db = Chroma(
        document_name,
        embedding_function=embedding_function,
        persist_directory="./chroma_langchain_db",

    )


    pdf_loader = PyPDFLoader("resources/" + document_name)
    pdf_chunks = text_splitter.split_documents(pdf_loader.load())

    def grouper(iterable, n):
        for i in range(0, len(iterable), n):
            yield iterable[i:i + n]

    for group in list(grouper(pdf_chunks, 150)):
        vector_db.add_documents(group)

def get_rag_chain(document_name:str, vector_db_search:str):
    vector_db = Chroma(
        document_name,
        embedding_function=embedding_function,
        persist_directory="./chroma_langchain_db",
    )
    results = vector_db.similarity_search(vector_db_search, 4) # four clostest results

    ## Asking a question through a RAG chain
    from langchain_core.prompts import PromptTemplate
    # Use three sentences maximum and keep the answer as concise as possible.
    rag_prompt_template = """Du bist Dozent für einen Uni Kurs und das Dokument stammt von dir. 
    Auf Grundlage des Dokuments möchtest Du dem Leser des Dokuments  Fragen stellen, 
    um  das Verständnis des Inhalts des Dokuments zu überprüfen.
    Stelle die Fragen in Form von Multiple Choice  
    mit 5 Antwortmöglichkeiten.
    Benutze keine Meta Informationen des Dokuments wie Autor oder Kapitelnummer

    {context}
    Question: {question}
    Helpful Answer:"""

    rag_prompt = PromptTemplate.from_template(rag_prompt_template)


    retriever = vector_db.as_retriever()

    from langchain_core.runnables import RunnablePassthrough
    question_feeder = RunnablePassthrough()


    from langchain_openai import ChatOpenAI

    chatbot = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name="gpt-4o-mini")

    # set up RAG chain

    return {"context": retriever, "question": question_feeder} | rag_prompt | chatbot

def execute_chain(chain, my_question):
    my_answer = chain.invoke(my_question)
    return my_answer

import io
from contextlib import redirect_stdout
def console_output (content:str):
    with io.StringIO() as buf, redirect_stdout(buf):
        print(content)
        output = buf.getvalue()
    return output

def ask_question(document_name:str, my_question:str):
        # question = "Was steht im Dokument"
    rag_chain = get_rag_chain(document_name, my_question)
    result = execute_chain(rag_chain, my_question)
    # pretty_json_string = json.dumps(result.content, indent=4)
    pretty_json_string = console_output(result.content)
    return pretty_json_string

