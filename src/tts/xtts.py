from .tts import TTS

class XTTS(TTS):
    def __init__(self):
        super().__init__("xtts")

    async def speak(self, text: str, lang: str, voice: str, speed: float) -> bytes:
        # TODO: Implement this
        pass