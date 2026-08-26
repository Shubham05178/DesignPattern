from text_momento import  TextMomento
class TextEditor:
    def __init__(self):
        self.__text=""
    def write(self,text):
        self.__text+=text
    def save(self):
        return TextMomento(self.__text)
    def restore(self,tm:TextMomento):
        self.__text=tm.get_text()
    def get_text(self):
        return self.__text