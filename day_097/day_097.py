import speech_recognition as sr

def reconhecer_fala():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando o ruído ambiente... Aguarde um momento.")
        recognizer.adjust_for_ambient_noise(source)
        print("Pronto! Pode falar.")

        audio = recognizer.listen(source)

        try:
            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
        except sr.UnknownValueError:
            print("Não consegui entender o que você disse.")
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala; {e}")

if __name__ == '__main__':
    reconhecer_fala()