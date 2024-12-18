import os
import requests
from dotenv import load_dotenv
from .tts import TTS

class MonsterTTS(TTS):
    def __init__(self):
        super().__init__("monster")
        # Load the environment variables
        load_dotenv()
        self.api_key = os.getenv("MONSTER_TOKEN")
        

    def generate(self, text):
        print("Generating TTS")
        url = 'https://api.console.tts.monster/generate'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.api_key
        }
        data = {
            "voice_id": "7e0ee786-b660-47ce-8de7-02fd49698efc",
            "message": text
        }

        response = requests.post(url, headers=headers, json=data)
        print("TTS generated")
        print(response.json())
        print(response.json()['url'])
        
        if response.status_code == 200:
            print("TTS generated")
            print(response.json())
            print(response.json()['url'])
            self.download_and_save(response.json()['url'])
            return response.json()['url']
        else:
            raise Exception("Failed to generate TTS: " + response.text)
