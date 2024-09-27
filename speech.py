import azure.cognitiveservices.speech as speechsdk
class Ai_assis():
    def __init__(self):
        pass
    def recognize_from_microphone(self):
        print("Say Something .....")
        
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription='', region='centralindia')

        speech_translation_config.speech_recognition_language="hi-IN"
        speech_translation_config.speech_recognition_language="en-IN"

        target_language="en"
        speech_translation_config.add_target_language(target_language)

        audio_config = speechsdk.audio.AudioConfig(filename="audios/input.wav")
        translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)

        # print("Speak into your microphone.")
        translation_recognition_result = translation_recognizer.recognize_once_async().get()

        if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
            return translation_recognition_result.translations[target_language]
        
        elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
        elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = translation_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

    def text_to_speech(self,text,language):
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription='', region='centralindia')
        audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

        # The language of the voice that speaks.
        if language == "en":
            speech_config.speech_synthesis_voice_name = 'en-US-SaraNeural'
        elif language == "hi":
            speech_config.speech_synthesis_voice_name = 'hi-IN-SwaraNeural'
        else:
            speech_config.speech_synthesis_voice_name = 'en-US-SaraNeural'

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

        # Get text from the console and synthesize to the default speaker.

        speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            # Save the audio to a file
            with open("audios/output.wav", "wb") as audio_file:
                audio_file.write(speech_synthesis_result.audio_data)

    def speech_to_text():
        # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
        speech_config = speechsdk.SpeechConfig(subscription='', region='centralindia')
        speech_config.speech_recognition_language="en-US"

        audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

        print("Speak into your microphone.")
        speech_recognition_result = speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Recognized: {}".format(speech_recognition_result.text))
            
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            print("Speech Recognition canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")
