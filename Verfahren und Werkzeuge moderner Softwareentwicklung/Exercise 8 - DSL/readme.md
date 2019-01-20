Folgender Code ist ein _wirklich_ rudimentärer HTML Builder. 


Durch folgenden Code wird der HTML Builder aufgerufen 
```swift 
class ViewController: UIViewController {
 override func viewDidLoad() {
    super.viewDidLoad()

    let htmlBuilder = HTMLBuilder()
    htmlBuilder.includeLibrary(url: "www.google.de/js/chart.js").
               .addTitle(input: "Hello".uppercased()
                                       .kursiv()
                                       .bold())
               .printer()
 }
}
```

Der Output ist folgender: 
```html
<html>
<head>
<script type="text/javascript" src="www.google.de/js/chart.js"></script>
</head>
<body>
<h1><b><i>HELLO</i>/n</b>/n</h1>
</body>
</html>
```

Die Logik passiert hier:
```swift
class HTMLBuilder {
    private var head: [String] = []
    private var body: [String] = []

    func kursiv(input: String) -> HTMLBuilder {
        body.append("<i>\(input)</i>")
        return self
    }

    func addTitle(input: String) -> HTMLBuilder {
        body.append("<h1>\(input)</h1>")
        return self
    }

    func includeLibrary(url: String) -> HTMLBuilder {
        head.append("<script type=\"text/javascript\" src=\"\(url)\"></script>")
        return self
    }

    func printer() {
        print("<html>")

        print("<head>")
        for item in head {
            print(item)
        }
        print("</head>")


        print("<body>")
        for item in body {
            print(item)
        }
        print("</body>")
        
        print("</html>")
        }
    }
}
```

Die Stringveränderungen können mittels einer Extension umgesetzt werden. (Ich hätte an dieser Stelle auch meine eigene Stringklasse schreiben können, aber warum sollte ich das tun.)
```swift
extension String {
    func kursiv() -> String {
        return "<i>\(self)</i>/n"
    }

    func bold() -> String {
        return "<b>\(self)</b>/n"
    }
}
```

Im Endeffekt nicht wirklich praktisch, da mein Builder nicht mächtig ist. Es würde noch einiges an Fleißarbeit bedeuten alle HTML Elemente einzubinden und vermutlich würde es auch nicht so einfach weitergehen. Dann müsste man auch nochmal sehr über die DSL-Struktur nachdenken...  

Allerdings rein theoretisch ist bereits hier ein kleiner Mehrwert zu erkennen, man kann keinerlei Klammerfehler machen und man muss sich nicht um den  `head` und `body` kümmern. 
