
# Thema
Planung und Erstellung einer Backend-Microservices-Architektur aus den Anforderungen durch das Spiel  `Stirnraten`. 

# Inhaltsverzeichnis

## Einleitung
* Gründe und Notwendigkeit
* Herausforderungen

## Grundlagen
* Microservices
* Monolithische Struktur
* Monolith vs. Microservices 
* Makro-Mikro-Architektur 
* Kommunikation zwischen Microservices

## Konzept Stirnraten API 
### Anforderungen
* Bounded Contexts für mögliche Microservices: Wörter CRUD, Customer CRUD, Rangliste CRUD, Authentifizierung, Messaging Service 
* Authentifizierung (Abwägung zwischen unterschiedlichen Methoden)
* Abwägen zwischen der Kommunikation (Synchron, Asynchon, wo ist was nötig und warum?)
* Messaging (Kafka vs. RabbitMQ vs. ?)
* Schnittstellen (Abwägen zwischen REST, Protobuf, Atom)
* Speicherung Vor- und Nachteile für NoSql und relationale Datenbank

### Implementierung/Umsetzung
* Architektur für Services (Messaging, Authentifizierung)  
* Datenbank anlegen und verbinden 
* Einzelne Services Dockern, um einen Container zu erhalten
* Container in einer Container Registry in Azure erstellen 
* Container Instanz erstellen und von außen erreichbar machen 

## Schluss/Fazit 
//Ausblick Kubernetes (...) 
