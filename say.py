# pip3 install pulsectl
import pyttsx3
import pulsectl
import random

# Call this to get a 'say' function which reuses underlying engine instance
def get_sayer():
	engine = pyttsx3.init()
	engine.setProperty('volume', 0.2)  # Stop it blasting us when we have paused a movie
	pulse = pulsectl.Pulse()

	def say(msg):
		print(msg)
		if not is_running(pulse):
			choose_voice(engine)
			engine.say(msg)
			engine.runAndWait()


	return say


def is_running(pulse):
	sinks = pulse.sink_list()
	return any(sink.state == 'running' for sink in sinks)


def choose_voice(engine):
	voices = engine.getProperty('voices')
	voice_ids = []
	for voice in voices:
		id = voice.id
		if id.startswith('english'):
			# English:
			voice_ids.append(id)
			# Chicks - only works on Linux:
			voice_ids.append(f"{id}+f1")
			voice_ids.append(f"{id}+f2")
			voice_ids.append(f"{id}+f3")
			voice_ids.append(f"{id}+f4")
	engine.setProperty('voice', random.choice(voice_ids))
