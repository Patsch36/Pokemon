#pip install googletrans==4.0.0rc1 !! other version dont work
from googletrans import Translator

class Language:
    def __init__(self):
        self.translator = Translator()
        
        
    def translate(self, text, source, target):
        text_translated = self.translator.translate(text=text, src=source, dest=target).text
        return text_translated
