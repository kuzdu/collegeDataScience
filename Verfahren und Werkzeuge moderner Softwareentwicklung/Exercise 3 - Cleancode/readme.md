# Clean Code

## Spielausschnitt 
- [Clean Code Ausschnitt aus dem Spiel Stirnraten](cleanCodeExample.md)

## Clean Code Style Sheet -  Top 20 
Das folgende Style Sheet zeigt meine Top 20 Regeln für Clean Code. 

## 1. Sinnvolle Variablennamen 

Variablennamen sollten sprechend und nicht abgekürzt sein. 

Don't
```
var n = 4000
var t = 1.19
var bto = n * t
```

Do
```
var netto = 4000
var taxes = 1.19
var brutto = netto * taxes 
```
## 2. Abfragen in Funktionen auslagern 

Abfragen sollten in Funktionen ausgelagert werden, um die Lesbarkeit zu verbessern.

Don't
```
if user.age >= 20 && user.hasDriverLicense == true && !user.isDrunk && user.hasDriverExperience > 1 {
driveCar() 
} 
```

Do
```
if user.isAllowedToDrive() {
driveCar()
} 
```


## 3. Sprechende Funktionen
Funkionen sollten sprechend sein.

Don't
```
if check() {
    transition(account)
} else {
    error()
}
```

Do
```
if isTransitionValid() {
    startTransistionTo(bankAccount)
} else {
    showError()    
}
```

## 4. Langen Code in Funktionen aufsplitten

Don't
```
let user = User()
user.age = ageTextfield.text
user.name = nameTextField.text
user.hasDriverLicense = driverLicenseSwitch.value
user.isDrunk = isDrunkSwitch.value
user.hasDriverExperience = Int(hasDriverExperienceTextField.text)

if user.age >= 20 && user.hasDriverLicense == true && !user.isDrunk && user.hasDriverExperience > 1 {
let machine = Machine("VWGolf")
machine.ignitionOn = true
user.machine = machine
...
} 
```

Do
```
let user = createUser()
if user.isAllowedToDrive() {
    drive("VWGolf")
}

```

## 5. Keine Seiteneffekte 

Seiteneffekte müssen immer verhindert werden. 

Don't
```
// self = user-Objekt
func setAge(age: Int) {
    self.age = age
    if age >= 18 {
        self.ofAge = true
    }
}
```

Do
```
func setAge(age: Int) {
    self.age = age
}
func isOfAge() {
    return self.age >= 18
}
```


## 6. Konstruktoren/Funktionen nicht überparametrisieren, sondern in Objekte aufteilen

Drei Argumente in einer Funktion/Konstruktoren sind okay, vier kritisch und alles ab fünf zu viel.


Don't
```
let user= user("Michael", "Müller", 20, "Maxstraße 4a", "51023", Köln)
```

Do
```
let address = Address("Maxstraße 4a", "51023", "Köln")
let personalInformation = PersonalInformation("Michael","Müller","20")
let user = User(personalInformation, address)
```


## 7. Nicht jeder kennt jeden

Klassen sollten so aufgebaut sein, dass nicht jeder jeden kennt, sondern nur seine Nachbarn. 
Dies verhindert
- Referenzprobleme
- gewährt Übersichtlichkeit, wer, was genau macht und machen darf 
- verhindert Fehlerhafte Implementierungen durch Direktzugriffe.

Don't 
``` 
var currentLocationLatidude = locationManager.currentLocation.position.coordinate.latitude
var currentLocationLongitude = locationManager.currentLocation.position.coordinate.longitude
```

Do
```
var currentLocationLatidude = locationManager.getCurrentLocationLatitude() 
var currentLocationLatidude = locationManager.getCurrentLocationLongitude()
```

## 8. Switch vs. if-else 

Natürlich hängt es ein wenig von der Erfahrung ab, wann man Switch und wann if-else verwendet, allerdings bietet sich ein switch besonders an, wenn abgeschlossene Zustände erwartet werden, während if-else eher für kürzere Entscheidungsphasen sinnvoll ist. 

Do
```
enum ProfileCells {
    personalData, payment, address, logout
}

func getNextCell(profileCell: ProfileCell) -> TableViewCell {
    switch profileCell {
    case .personalData: return PersonalDataCell()
    case .payment: return PaymentCell() 
    case .address: return AddressCell()
    case .logout: return LogoutCell()
    }
}
```
Das Äquivalent sähe als if-else wie folgt aus: 
```
func getNextCell(profileCell: ProfileCell) -> TableViewCell {
    if profileCell == .personalData {
        return PersonalDataCell()
    } else if == .payment {
        return PaymentCell()
    } else if == .address {
        return AddressCell()
    } else {
        return LogoutCell()
    }
}
```
Nachtteile bzgl. des `if-else`: 
- ist unübersichtlicher
- wirft keinen Compiler Error, wenn das Enum erweitert wird. Dies geschieht allerdings beim  `switch` , da nicht alle Zustände abgedeckt ist.
- wird das Enum erweitert, wird die if-else Strutkur fehlerhaft, was aber nicht zwingend vom Entwickler bemerkt werden muss (je nach Größe des Projektes). 

Alternativ:
```
func getNextCell(profileCell: ProfileCell) -> TableViewCell {
    // ...
    } else if == .logout {
        return LogoutCell()
    } else {
        return TableViewCell() // leere Zelle
    }
}
```
So kann zwar immer nur tatsächlich die Zelle zurückgegeben werden, welche angefordert ist, allerdings setzt die Funktion durch `-> TableViewCell`  voraus, dass immer eine intialisierte Zelle zurückgegeben wird.  In diesem Fall durch  `return TableViewCell()` eine unnötige/leere Zelle erzeugt. 


## 9. TODOs sind verboten

Code in dem `TODO` steht  darf nicht in ein Branch gepushed werden. Unfertige Implementierungen sind unsauber, schnell fehlerhaft und einfach falsch. 
Falls eine Funktionalität eingebaut wurde, die funktioniert, allerdings noch einmal überarbeitet werden sollte, dann kann dies durch einen Kommentar gelöst werden.

Don't
```
//TODO: error handling is a general error at the moment, should improving this
func xy() {
    ...
}
```

Do
```
/**
return is always just a general error
see Ticket-123 on www.trello.de/ticket-123: "improving error handling for xy" 
*/
func xy() {
...
}
```

## 10.  Konventionen der Entwicklungssprache nutzen.
Je nach Programmiersprache  gibt es common ways, best practices und/oder Konventionen. An diese sollte man sich immer halten, und diese einheitlich und durchgängig für das Projekte verwenden. 

Mögliche Stile wären z.B. snake_case, camelCase oder UpperCamelCase. Auch die Klammersetzung sollte einheitlich sein, wie z.B.

```
if isUserThursty() {
    //drink a water
} else {
    //drink a beeer
}
    
```

```
if (isUserThursty())
{
    //drink water
} 
else 
{
    //drink a beer
}
```
Beide Varianten sind gleichrichtig. Während die erste klassisch für `Swift` ist, wird die andere für `.net` eingesetzt. Wichtig ist die Einheitlichkeit im Projekt. 


## 11. Kurzschreibweisen bevorzugen
Kurzschreibweisen können gerade für Anfänger schwieriger zu lesen sein, allerdings sparen sie viel Platz und erleichtern  so die Lesequalität.

Einige Beispiele aus `Swift`

Don't
```
var foundItem: Item!
for item in items {
    if item.id == 1293 {
        foundItem = item
        break
    }
}
...
```

Do
```
var foundItem = items.first.filter({ 0$.id == 1293 })
```

## 12. Löschen von nutzlosem Code und Kommentaren

Code, der nicht verwendet wird, sollte gelöscht werden, genau wie unnötige Kommentare. Da Versionsverwaltungen (wie z.B Git) verwendet werden, ist der Code ohnehin nie weg. 


