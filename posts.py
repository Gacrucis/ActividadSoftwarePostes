from typing import Type

from elements import Element

class Post:

    def __init__(self, slots) -> None:
        self._slot_amount = slots
        self.slots = [None for n in range(slots)]

    def install(self, element, index: int = None) -> None:

        if index is None:
            for i, slot in enumerate(self.slots):
                if slot is None:
                    index = i
                    break
        
        if index is None:
            print('Poste lleno!')
            return

        self.slots[index] = element #type: ignore

    def remove(self, index: int = None) -> None:
        
        if index is None:
            for i, slot in enumerate(self.slots):
                if slot is not None:
                    index = i
                    break

        if index is None:
            print('Poste vacio!')
            return

        self.slots[index] = None
        

    def __repr__(self) -> str:
        string = f'{"_"*18}\n'
        for element in self.slots:
            if element:
                string += f'| {repr(element) : ^14} |'
            
            else:
                string += f'| {"-" : ^14} |'

            string += '\n'

        string += f'| {" " : ^14} |\n'
        string += f'| {" " : ^14} |\n'

        return string
        

class NormalPost(Post):

    def __init__(self) -> None:
        super().__init__(slots=5)

class BigPost(Post):

    def __init__(self) -> None:
        super().__init__(slots=7)