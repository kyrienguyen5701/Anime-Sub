import speech_recognition as sr 

r = sr.Recognizer()
kimiiro = sr.AudioFile('Kimiiro-Subliminal.wav')
with kimiiro as src:
    audio = r.record(src)

print(r.recognize_google(audio))