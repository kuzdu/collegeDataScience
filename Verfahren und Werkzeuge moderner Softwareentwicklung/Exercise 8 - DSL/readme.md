Folgender Code ist ein _wirklich_ rudimentärer HTML Builder. 


Durch folgenden Code wird HTML Builder aufgerufen 
```
class ViewController: UIViewController {
 override func viewDidLoad() {
    super.viewDidLoad()

    let htmlBuilder = HTMLBuilder()
    htmlBuilder.includeLibrary(url: "www.google.de/js/chart.js").
               .addTitle(input: "Hello".kursiv()
                                       .bold()
                                       .uppercased())
               .printer()
 }
}
```

Der Output ist folgender: 
```
<html>
<head>
<script type="text/javascript" src="www.google.de/js/chart.js"></script>
</head>
<body>
<h1><B><I>HELLO</I>/N</B>/N</h1>
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

Die Stringveränderungen können mittels Extensions umgesetzt werden. 
```
extension String {
    func kursiv() -> String {
        return "<i>\(self)</i>/n"
    }

    func bold() -> String {
        return "<b>\(self)</b>/n"
    }
}
```

Im Endeffekt nicht wirklich praktisch, da sehr unmächtig.

Allerdings rein theoretisch ist auch hier ein kleiner Mehrwert zu erkennen, man kann keinerlei Klammerfehler machen und man muss sich nicht um den  `head` und `body` kümmern. 

Trotzdem möchte ich keine komplizierten HTML Strukturen abbilden müssen können, weil das bestimmt recht frickelig wird, wenn ids, mehr js, classes, divs usw. hinzukommen. 
