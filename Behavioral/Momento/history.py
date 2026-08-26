from text_momento import TextMomento
from typing import List
class History:
    def __init__(self):
        self.__history:List[TextMomento]=[]
        self.__redo_history:List[TextMomento]=[]
    def undo(self):
        if self.__history:
            self.__redo_history.append(self.__history.pop())
            if self.__history:
                return self.__history[-1]
            return TextMomento("")
        return TextMomento("")
    def redo(self):
        if self.__redo_history:
            momento = self.__redo_history.pop()
            self.__history.append(momento)
            return momento
        if self.__history:
            return self.__history[-1]
        return TextMomento("")
    def save(self,tc:TextMomento):
        self.__history.append(tc)
        self.__redo_history.clear()