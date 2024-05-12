from __future__ import annotations
from abc import ABC, abstractmethod


class ICharacterFactory(ABC):
    @abstractmethod
    def create(self):
        return ICharacter()


class ICharacter(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self):
        pass

    @abstractmethod
    def get_skills(self):
        pass

    @abstractmethod
    def add_skill(self, skill):
        pass


class HumanCharacterFactory(ICharacterFactory):
    def create(self):
        return HumanCharacter()


class HumanCharacter(ICharacter):
    def go(self):
        return "Human go"

    def attack(self):
        return "Human attack"

    def defense(self):
        return "Human defense"

    def get_skills(self) -> list:
        return ["Human skill 1", "Human skill 2", "Human skill 3"]

    def add_skill(self, skill):
        return "Human skill 4"


class ElfCharacterFactory(ICharacterFactory):
    def create(self):
        return ElfCharacter()


class ElfCharacter(ICharacter):
    def go(self):
        return "Elf go"

    def attack(self):
        return "Elf attack"

    def defense(self):
        return "Elf defense"

    def get_skills(self) -> list:
        return ["Elf skill 1", "Elf skill 2", "Elf skill 3"]

    def add_skill(self, skill):
        return "Elf skill 4"


if __name__ == "__main__":
    factory = HumanCharacterFactory()
    character = factory.create()
    human_go = character.go()
    print(human_go)

    factory = ElfCharacterFactory()
    character = factory.create()
    elf_go = character.go()
    print(elf_go)
