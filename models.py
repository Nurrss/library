from dataclasses import dataclass
from enums import ItemStatus

@dataclass
class Book():
    id : int
    title : str
    author : str
    status : ItemStatus = ItemStatus.AVAILABLE

    def __init(self, id : int , title : str , author : str):
        self.id = id
        self.title = title
        self.author = author

@dataclass
class Reader():
    id : int
    name : str
