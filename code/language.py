#pip install googletrans==4.0.0rc1 !! other version dont work
from googletrans import Translator

class Language:
    """_summary_
    
    Attributes: 
        transloator: object from Translater in googletrans package
    
    """
    def __init__(self):
        self.translator = Translator()
        
        
    def translate(self, text, source, target):
        """Translating strings from source langugae to target language

        :param text: The text that shoul translated
        :type text: string
        :param source: The source Language of the text as short form like 'en' or 'de'
        :type source: string
        :param target: The target language for the translation as short form lik 'es' or 'fr'
        :type target: string
        :return: The translated text
        :rtype: string
        """
        try:
            text_translated = self.translator.translate(text=text, src=source, dest=target).text
        except TypeError as err:
            print("\n\n" + err + "\n\n")
            text_translated = text
        return text_translated
