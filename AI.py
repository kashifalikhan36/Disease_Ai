import openai
import json
class Ai_assistent:

    def __init__(self):
        openai.api_type = "azure"
        openai.api_base = "https://bless.openai.azure.com/"
        openai.api_version = "2023-07-01-preview"
        openai.api_key = ""
        data=""
        with open('data/ai_train.json','r') as file:
            data = json.load(file)
        self.messages=data
        with open('data/doc_train.json','r') as file:
            data2 = json.load(file)
        self.doc=data2
        self.text_identifier=[{"role": "system", "content": 'Ignore all the instructions you got before. From now on, you are going to act as Language detector. I would like you to simulate as language detector where whenever i said something to u you have need to give result as that "hi" which stands for Hindi or "en" and which stands for English. as example:-user said:-"kya haal h yrr"   then u reply:- "hi"    if user said:-"whats going on?" then u reply:- "en"'}]
        
    def Assistent_listen(self,data):
        self.messages.append(
            {"role": "user", "content": data},
        )

        chat = openai.ChatCompletion.create(
            engine="Bless",
            model="gpt-3.5-turbo", 
            messages=self.messages,

        )

        prompt = chat.choices[0].message.content

        self.messages.append({"role": "assistant", "content": prompt})
        with open('data/ai_train.json',"w") as file:
            json.dump(self.messages, file)
        return prompt
    
    def Doc_result(self,data):
        self.doc.append(
            {"role": "user", "content": data},
        )

        chat = openai.ChatCompletion.create(
            engine="Bless",
            model="gpt-3.5-turbo", 
            messages=self.doc,

        )

        prompt = chat.choices[0].message.content

        try:
            data=json.loads(prompt)
            print(data)
            print("check_1")
        except: 
            data={'status':'yes','data':{'PhysicalHealthDays':12,'SleepHours':4,'HeightInMeters':1.829,'WeightInKilograms':78,'Gender':1,'PhysicalActivitie':1,'HadStrokes':0,'HadDiabetess':0,'HadDepressiveDisorders':0,'AlcoholDrinker':0,'HighRiskLastYears':0,'CovidPosi':0}}
            pass
        if data["status"] == "no":
            print("check_2")
        print("check_3")
        with open('data/doc_data.json',"w") as file:
            json.dump(data, file)
        print("all okay")
        return data
    
    def Language_detect(self,data):

        self.text_identifier.append(
            {"role": "user", "content": data},
        )

        chat = openai.ChatCompletion.create(
            engine="Bless",
            model="gpt-3.5-turbo", 
            messages=self.text_identifier,
            
        )

        prompt = chat.choices[0].message.content

        self.text_identifier=[{"role": "system", "content": 'Ignore all the instructions you got before. From now on, you are going to act as Language detector. I would like you to simulate as language detector where whenever i said something to u you have need to give result as that "hi" which stands for Hindi or "en" and which stands for English. as example:-user said:-"kya haal h yrr"   then u reply:- "hi"    if user said:-"whats going on?" then u reply:- "en"'}]
        return prompt