"""Dog Object"""


class Dog:
    """Dog Class"""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Dog(name={self.name}, age={self.age})"

    def __gt__(self, other_dog) -> bool:
        return self.age > other_dog.age
