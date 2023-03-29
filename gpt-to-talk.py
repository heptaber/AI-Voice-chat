#!/usr/bin/python3

import speech_recognition as sr
import os, pyttsx3
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')
engine = pyttsx3.init()
finish_phrases = {"goodbye", "finish", "bye", "see you", "see you later"}
messages_log = [
        {"role": "system", "content": "You are a helpful assistant with exciting, interesting things to say."},
        {"role": "user", "content": "Hello, how are you?"},
]


def extract_voice_to_text():
    speech_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognizer.listen(source, phrase_time_limit=2)
        audio_text = ""

        try:
            audio_text = speech_recognizer.recognize_google(audio)
        except Exception as ex:
            print("Exception: ", str(ex))

        return audio_text

def chatting_AI():
    global messages_log
    print("Listening...")
    user_text_input = extract_voice_to_text()
    print("You said: " + user_text_input)
    messages_log.append({"role": "user", "content": user_text_input})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages_log
    )
    reply = response.choices[0].message.content
    engine.say(reply)
    engine.runAndWait()
    messages_log.append({"role": "system", "content": reply})
    if user_text_input.lower() in finish_phrases:
        print("Bye!\nExiting...")
        exit(0)

    chatting_AI()


def main():
    print("Welcome! The discussions starts here ;)")
    chatting_AI()

if __name__ == "__main__":
    main()
