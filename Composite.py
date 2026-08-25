from abc import ABC,abstractmethod
from typing import List
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass
class File(FileSystemComponent):
    def __init__(self,name):
        self.__file_name=name
    def show_details(self):
        print(f"{self.__file_name}")
class Folder(FileSystemComponent):
    def __init__(self,component):
        self.__name=component
        self.__components:List[FileSystemComponent]=[]
    def add_component(self,componet):
        self.__components.append(componet)
    def show_details(self):
        print(f"Folder Name:{self.__name} has {len(self.__components)} items")
        for component in self.__components:
            component.show_details()

f1=File("f1")
f2=File("f2")
f3=File("f3")
f11=Folder("GDrive")
f11.add_component(f1)
f11.add_component(f2)
f11.add_component(f3)
f12=Folder("Shubham Gdrive")
f11.add_component(f12)
f12.add_component(f1)
f12.add_component(f2)
f11.show_details()