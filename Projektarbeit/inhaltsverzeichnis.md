
# Thema
Planung und Erstellung einer Backend-Microservices-Architektur aus den Anforderungen durch das Spiel  `Stirnraten`. 

# Inhaltsverzeichnis

## Einleitung
* Gründe und Notwendigkeit
* Herausforderungen

## Grundlagen
### Verständnis Mikro-Makro-Architektur 
* On Premise 
* Saas (Software as a Service)
* Paas (Platform as a Service)
* IaaS (Infrastructe as a Service)
* ggf. Container ... ?

### Kommunikation zwischen Microservices
* Domänen und Bounded Context 
* Synchon vs. Asynchron
* Messaging
* Schnittstellen REST, Protobuf und Atom
* Authentifizierung 
* Datenbank (NoSQL vs relationale Datenbank SQL) (ggf. rauslassen?)

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


---------------------------
#### offene Fragen
_Wünsche_  
* Im Git als .md open source schreiben
* vllt alle zwei Wochen einen festen Termin? 

#### Was wird nicht berücksichtigt
*  Frontend Microservice Lösungen, d.h. Webseite mit mehren UI-Modulen, wo jeweils ein anderer Microservice hinter steht,
*  Deploymentstrategien
*  Docker und Kubernetes
* Datenbank (NoSQL vs relationale Datenbank SQL) (ggf. rauslassen?)
