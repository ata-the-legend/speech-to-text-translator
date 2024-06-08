import wave, os, json, time

from vosk import Model, KaldiRecognizer, SetLogLevel
from broker import publish_for_translate

SetLogLevel(-1)

model = Model("./vosk_model/vosk-model-small-en-us-0.15")


def speech_to_text(audio):
    # time.sleep(10)
    transcription= []   
    try:
        with open("temp_audio.wav", "wb") as f:
            f.write(audio)

        with wave.open("temp_audio.wav", "rb") as wf:
            recognizer = KaldiRecognizer(model, wf.getframerate())

            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    result_dict = json.loads(recognizer.Result())
                    transcription.append(result_dict.get("text", ""))
            final_result = json.loads(recognizer.FinalResult())
            transcription.append(final_result.get("text", ""))
            transcription_text = ' '.join(transcription)


        os.remove("temp_audio.wav")
        return transcription_text
    except Exception as e:
        return {"error": str(e)}


def speech_to_translate(audio):
    etext = speech_to_text(audio)
    message = publish_for_translate(etext)
    return message
