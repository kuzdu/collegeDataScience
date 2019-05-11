
# Legende
 ✅: In sich abgeschlossen
 🔨: Work in Progress
 🔜: Coming soon

# Thema
Planung und Erstellung einer Backend-Microservices-Architektur aus den Anforderungen durch das Spiel  `Stirnraten`. 

# Inhaltsverzeichnis

## Glossar 🔨

## Einleitung
* Gründe und Notwendigkeit 🔜
* Herausforderungen 🔜

## Grundlagen
* Microservices ✅
* Monolithische Struktur ✅
* Monolith vs. Microservices  ✅ 
* Architektur von Micrsoservices ✅ 
* Kommunikation ✅
* Authentifizierung ✅
* Docker ✅ 

## Konzept Stirnraten API 
### Anforderungen
* Anforderungen erfassen 🔨
* Gesetzte Makroarchitektur festlegen und begründen (Technologiestack, Programmiersprachen, Datenbanken, Docker, Rest etc.) 🔜
* DDD anwenden, um Bounded Contexts für mögliche Microservices zu entwerfen: Wörter CRUD, Customer CRUD, Rangliste CRUD, Authentifizierung, Messaging Service  🔜
* Authentifizierung und Authorisierung (Was gibt es, Eigenbau, Drittanbieter, Netflixs Zhul?) 🔜
* Abwägen zwischen Kommunikationsarten: Messaging (Kafka vs. RabbitMQ vs. ?) 🔜

### Implementierung/Umsetzung
* Architektur für Services (Messaging, Authentifizierung) 🔜
* Datenbank anlegen und verbinden 🔜
* Einzelne Services Dockern, um einen Container zu erhalten 🔜
* Container in einer Container Registry in Dockerhub erstellen (vllt zu spezifisch) 🔜
* Container Instanz erstellen und von außen erreichbar machen 🔜

## Schluss/Fazit 
* Ausblick Kubernetes (...) 🔜
* (Microservice) Frontend 🔜

------
(Ggf.) offene Fragen:
In Grundlagen ist geplant, allgemein zu erklären, was ist Authentifzierung und Authorisierung und welche gängigen Möglichkeiten gibt es.  
Im Konzept entscheide ich mich für XY und wäge zwischen Technologien ab.
