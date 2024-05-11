from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def create(self):
        pass


class JapaneseEngine(IEngine):
    def create(self):
        print(1123)


if __name__ == '__main__':
    japanese_engine = JapaneseEngine()
    japanese_engine.create()
