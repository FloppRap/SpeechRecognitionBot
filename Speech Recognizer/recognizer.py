#SPEECH RECOGNIZER

import speech_recognition as sr

def Record():
	r = sr.Recognizer()

	voiceString = ""

	with sr.Microphone() as source:
	    print("Listening...")
	    r.pause_threshold = 1		# Minimum length of silence
	    r.energy_threshold = 4000	# Values below this threshold are considered silence
	    
	    audio = r.listen(source)	# Listening

	    try:
	        voiceString = r.recognize_google(audio, language="es-Ar")		# Convert audio to text (online)
	        print("You said: {}".format(voiceString))
	    except:
	        print("Sorry could not hear")

	return voiceString