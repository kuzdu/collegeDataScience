# Lamdba

Eine lustige Sache ist es geworden. Ich habe den Messenger Telegram (sowas wie WhatsApp in cool) verwendet, um einen Bot zu registrieren. Diesem Bot kann man einen gewissen `payload` schicken.  Hier ein klassisches "Hello World".

![Telegram](images/telegrambot.png "Telegram")

Anschließend befülle ich eine DynamoDB (noch per Hand) mit Geburtstagsterminen. 

![DynamoDB](images/dynamodb.png "DynamoDB")

Diese Datenbank wird von einer lamda-Funktion mittels Cronjob einmal am Tag ausgelesen. Folgender Code kommt dabei zum Einsatz.

![lambda](images/lambda.png "lambda")

Es werden die Geburstage angesehen und falls ein Geburtstag am heutigen Tag ist, erhalte ich eine Push Notification mittels Telegram. 

![Reminder](images/reminder.png "Reminder")

Und das wars. Im Prinzip ziemlich mächtig, was AWS da bereitstellt. Wenn man überlegt, dass man noch relativ leicht ein API Gateway erstellen kann, hätte man ziemlich schnell ein Reminder programmiert. 👨‍💻
