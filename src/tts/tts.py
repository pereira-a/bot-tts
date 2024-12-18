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