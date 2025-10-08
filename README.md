# FraGen Service
## Quick Start
1. Configure FastAPI in fraGen_service_config.toml
2. Add OpenAi Key to fraGen_service_config.toml
3. Start: python fraGen_service_fastapi.py
4. Use: http://127.0.0.1:5000/docs
## Sources
1. https://www.heise.de/ratgeber/Programmieren-mit-Python-Schnittstellen-entwickeln-mit-Pycharm-und-FastAPI-4940182.html?seite=all
2. Roberto Infante. AI Agents and Applications. Manning

## Beispiel

curl -X 'GET' \
  'protocol://host:port/document/2/Stelle%2010%20MC%20Fragen%20zum%20medizinischen%20Inhalt%20des%20Dokuments' \
  -H 'accept: application/json'

{
  "message": "Hier sind 10 Multiple-Choice-Fragen zum medizinischen Inhalt des Dokuments:\n\n1. Was beschreibt der Begriff \"vaskul�re Erkrankungen des Gehirns\"?\n   a) Erkrankungen des Herzmuskels  \n   b) Erkrankungen der Blutgef��e im Gehirn  \n   c) Neurologische Erkrankungen ohne vaskul�re Beteiligung  \n   d) St�rungen des Immunsystems  \n   e) Infektionskrankheiten des zentralen Nervensystems  \n\n2. Welche der folgenden Aussagen zu Gesundheit ist korrekt?\n   a) Gesundheit bedeutet immer das Fehlen von Krankheit  \n   b) Gesundheit ist ein Zustand v�lliger k�rperlicher, geistiger und sozialer Wohlbefindens  \n   c) Gesundheit ist nur k�rperlich definierbar  \n   d) Gesundheit ist nur relevant bis zu einem bestimmten Lebensalter  \n   e) Gesundheit bezieht sich ausschlie�lich auf die Abwesenheit von Symptomen  \n\n3.Welche der folgenden klinischen Fragestellungen ist in der allgemeinen Pathologie relevant?\n   a) Wo liegt die n�chste Klinik?  \n   b) Welche Symptome treten am h�ufigsten bei gesunden Menschen auf?  \n   c) Wie beeinflussen genetische Faktoren die Entstehung von Krankheiten?  \n   d) Was sind die besten Freizeitaktivit�ten f�r einen gesunden Lebensstil?  \n   e) Welche Medikamente sind die g�nstigsten in der Therapie?  \n\n4. Welche der folgenden Therapieans�tze wird h�ufig bei vaskul�ren Erkrankungen des Gehirns angewendet?\n   a) Bestrahlung  \n   b) Chirurgische Entfernung von Tumoren  \n   c) Antikoagulationstherapie  \n   d) Psychotherapie  \n   e) Physiotherapie zur St�rkung der Muskeln  \n\n5. Was ist ein h�ufiger Risikofaktor f�r die Entwicklung von vaskul�ren Erkrankungen des Gehirns?\n   a) Hoher Vitamin D-Spiegel  \n   b) Regelm��ige sportliche Bet�tigung  \n   c) Bluthochdruck  \n   d) Gesunde Ern�hrung  \n   e) Ausreichender Schlaf  \n\n6. Welche der folgenden Symptome ist typischerweise mit einer vaskul�ren Erkrankung des Gehirns verbunden?\n   a) Hautausschl�ge  \n   b) Ged�chtnisverlust  \n   c) Magenbeschwerden  \n   d) Sehst�rungen  \n   e) Gelenkschmerzen  \n\n7. Was ist das Hauptziel der allgemeinen Pathologie?\n   a) Die Auffindung und Diagnose seltener Krankheiten  \n   b) Die Untersuchung der Ursachen, Mechanismen und Folgen von Krankheiten  \n   c) Die Entwicklung neuer Medikamente  \n   d) Die Durchf�hrung medizinischer Eingriffe  \n   e) Die Aufkl�rung der Patienten �ber gesunde Lebensweisen  \n\n8. Welches der folgenden Konzepte ist f�r das Verst�ndnis von Krankheiten besonders wichtig?\n   a) Psychologische Stabilit�t  \n   b) Soziale Isolation  \n   c) Pathophysiologische Prozesse  \n   d) Finanzielle Absicherung  \n   e) K�rperliche Sch�nheit  \n\n9. Welches Organ ist am h�ufigsten von vaskul�ren Erkrankungen betroffen?\n   a) Lunge  \n   b) Leber  \n   c) Gehirn  \n   d) Herz  \n   e) Nieren  \n\n10. Was wird als Voraussetzung f�r die Diagnose einer Krankheit angesehen?\n    a) Vorhandensein von Symptomen  \n    b) Der Patient muss �lter als 50 Jahre sein  \n    c) Keine vorherigen Erkrankungen  \n    d) Vorliegende Labortests m�ssen negativ sein  \n    e) Vollst�ndige Familienanamnese  \n\nDiese Fragen sollten helfen, das Verst�ndnis des Inhalts des Dokuments zu �berpr�fen.\n"
}

## Tips
source fraGen_venv/bin/activate
(fraGen_venv) root@ubuntu:/var/www/FraGen-Service# python fraGen_service_fastapi.py