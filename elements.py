from __future__ import annotations


class Element:
    def __init__(self, name: str = "Element") -> None:
        self.name: str = name
        self.connections: list[Element] = []

    def connect(self, dest: Element) -> None:
        self.connections.append(dest)
        dest.connections.append(self)

    def print_connections(self) -> None:
        string = f"|- {self} "
        for connection in self.connections:
            string += f"→ {connection} "

        string += " -|"

        print(string)

    def __repr__(self) -> str:
        return self.name


class Transformer(Element):
    def __init__(self) -> None:
        super().__init__(name="Transformador")


class Cable(Element):
    def __init__(self, name="Cable") -> None:
        super().__init__(name)


class ShortCable(Cable):
    def __init__(self) -> None:
        super().__init__(name="Cable Corto")


class LongCable(Cable):
    def __init__(self) -> None:
        super().__init__(name="Cable Largo")
