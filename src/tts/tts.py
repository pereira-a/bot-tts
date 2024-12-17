class TTS:
    def __init__(self, provider_id):
        self.provider_id = provider_id

    def generate(self, text):
        raise NotImplementedError("Subclass must implement abstract method")