from abc import ABC,abstractmethod
class Parser(ABC):
    @abstractmethod
    def _data(self):
        pass
    def _open(self):
        print("Opening a File")
    def _close(self):
        print("Closing a File")
    def _parse(self):
        self._open()
        self._data()
        self._close()


class CSVParser(Parser):
    def _data(self):
        print("Parsing a CSV File")
class JSONParser(Parser):
    def _data(self):
        print("Parsing a JSON File")
class ExcelParser(Parser):
    def _data(self):
        print("Parsing a Excel File")

j=JSONParser()
j._parse()
c=CSVParser()
c._parse()
