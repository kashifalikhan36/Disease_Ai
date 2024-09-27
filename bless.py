from AI import Ai_assistent
from speech import Ai_assis
from heart import Heart


def Bless_ai():
    heart=Heart()
    AI=Ai_assistent()
    user_and_ai=Ai_assis()
    text_output=user_and_ai.recognize_from_microphone()
    language_detector=AI.Language_detect(text_output)
    Doc_result=AI.Doc_result(text_output)
    Heart=heart.Model(Doc_result)
    Ai_Listen_you=AI.Assistent_listen(Heart)
    return user_and_ai.text_to_speech(Ai_Listen_you,language_detector)