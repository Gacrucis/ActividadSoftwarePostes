class Element:

    def __init__(self, name='Element') -> None:
        self.name = name
        self.connections = []

    def connect(self, dest) -> None:
        self.connections.append(dest)
        dest.connections.append(self)

    def print_connections(self) -> None:
        string = f'|- {self} '
        for connection in self.connections:
            string += f'→ {connection} '
        
        string += ' -|'

        print(string)

    def __repr__(self) -> str:
        return self.name

class Transformador(Element):

    def __init__(self) -> None:
        super().__init__(name='Transformador')

class Cable(Element):

    def __init__(self, name='Cable') -> None:
        super().__init__(name)

class CableCorto(Cable):

    def __init__(self) -> None:
        super().__init__(name='Cable Corto')

class CableLargo(Cable):

    def __init__(self) -> None:
        super().__init__(name='Cable Largo')


