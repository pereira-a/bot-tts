import urllib.request

import requests

class TTS:
    """
    Base class for Text-to-Speech (TTS) providers.

    Attributes:
        provider_id (str): The identifier for the TTS provider.
    """

    def __init__(self, provider_id):
        """
        Initializes the TTS provider with the given provider ID.

        Args:
            provider_id (str): The identifier for the TTS provider.
        """
        self.provider_id = provider_id

    def generate(self, text):
        """
        Generates speech from the given text. This method should be implemented
        by subclasses.

        Args:
            text (str): The text to be converted to speech.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("Subclass must implement abstract method")
    
    def download_and_save(self, url):
        """
        Downloads the audio file from the given URL and saves it to the local
        filesystem.

        Args:
            url (str): The URL of the audio file to download.
        """
        response = requests.get(url)
        with open("./tts-audio.mp3", "wb") as file:
            file.write(response.content)
        self.bot.logger.debug("Audio file downloaded and saved")