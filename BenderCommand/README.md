# BenderCommand
Benötigte Bibliotheken: 
https://github.com/pyserial/pyserial
https://github.com/boppreh/keyboard
Achtet darauf, dass die Module für Python3 und nicht Python2 installiert werden.

Aufbau eines Kommandos:
	command(connection, commandStr, answerSize)
	
	connection: Objekt, welches die Serielle Verbindung darstellt
	commandStr: Das Kommando, welches als String über die Verbindung geschickt wird
	answerSize: Die größe der Antwort des Arduinos in Bytes. Wird None Übergeben, wird bis zum nächsten Newline vom Arduino gelesen

	return: liefert die Antwort des Arduinos oder -1 im Fehlerfall

Eigenes Kommando erstellen:
	siehe Beispiel BlueCommand
	Das eigene Kommando, muss die Funktion command aufrufen und die jeweils benötigten Parameter setzen
	Das eigene Kommando, kümmert sich um die Antwort vom Arduino
	Das eigene Kommando, muss in der main.py registriert werden (siehe commands = {"KommandoName" : commandFunktion})
	Das eigene Kommando, muss in der main.py importiert werden (siehe from BlueCommand import blue)
