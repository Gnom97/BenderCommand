from serial import Serial, SerialException

def command(connection, commandStr, answerSize):
	#Ob gültige Parameter gesetzt sind
	if connection == None:
		print("command: connection ist None")
		return -1
	if commandStr == None or len(commandStr) == 0:
		print("command: commandStr ist None")
		return -1

	#Schreiben der Nachricht
	byteCount = connection.write(commandStr)
	#Überprüfung ob genug Bytes geschickt wurden
	if byteCount < len(commandStr):
		print("command: Es konnten nicht alle Bytes geschrieben")

	#Lesen der Antwort
	answer = None
	if answerSize == None:
		answer = connection.readline()
	elif answerSize > 0:
		answer = connection.read(answerSize)

	return answer
	
