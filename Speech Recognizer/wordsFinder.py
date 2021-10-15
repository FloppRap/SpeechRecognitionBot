from recognizer import Record

def findKeyWords(voiceString, keyWords):

	if voiceString != "":
		if voiceString.find(keyWords) != -1:
			print("Ok")
		else:
			print("No")
	else:
		print("voiceString is null")

if __name__ == "__main__":
	voiceString = Record().lower()

	keyWords = "hola chicos"

	findKeyWords(voiceString, keyWords)