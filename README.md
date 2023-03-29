# Voice chatting with gpt
Chatting with OpenAI via audio interface.<br>
Have fun.


### phrases to stop communication:
- Goodbye
- Finish
- Bye
- See you
- See you later

## To set environment variable
You should set an environment variable **OPENAI_API_KEY** using your OpenAI API key.

```sh
export OPENAI_API_KEY=YOUR_PERSONAL_API_KEY_INSTED_OF_THIS
```

## Extra requirements for Mac
PortAudio and flac should be installed.<br>
The recommended way is doing it via brew following next commands:

```sh
brew update
brew install portaudio
brew link --overwrite portaudio
brew install flac
```
