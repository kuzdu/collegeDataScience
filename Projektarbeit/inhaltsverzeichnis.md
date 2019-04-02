
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
* Kommunikation (REST, welche Ebene?, Protobuf, Atom) zwischen Microservices (mit API-Gateway, (Synchron, Asynchon, wo ist was nötig und warum?))
* Authentifizierung und Authorisierung (Vor- und Nachteile von verschiedenen Verfahren)

## Konzept Stirnraten API 
### Anforderungen
* Gesetzte Makroarchitektur festlegen und begründen (Technologiestack, Programmiersprachen, Datenbanken etc.)
* DDD anwenden, um Bounded Contexts für mögliche Microservices zu entwerfen: Wörter CRUD, Customer CRUD, Rangliste CRUD, Authentifizierung, Messaging Service 
* Authentifizierung und Authorisierung (Was gibt es, Eigenbau, Drittanbieter, Netflixs Zhul?) 
* Abwägen zwischen Kommunikationsarten: Messaging (Kafka vs. RabbitMQ vs. ?)

### Implementierung/Umsetzung
* Architektur für Services (Messaging, Authentifizierung)  
* Datenbank anlegen und verbinden 
* Einzelne Services Dockern, um einen Container zu erhalten
* Container in einer Container Registry in Dockerhub erstellen (vllt zu spezifisch) 
* Container Instanz erstellen und von außen erreichbar machen 

## Schluss/Fazit 
//Ausblick Kubernetes (...) 
//(Microservice) Frontend 
