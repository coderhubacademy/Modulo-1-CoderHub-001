from gtts import gTTS

texto = input("Ingresa el texto que quieres grabar: ")

tts = gTTS(texto, lang='es')

tts.save('prueba.mp3')