class MyClass:
    def __init__(self):
        self._strategy = None

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, value):
        self._strategy = value


obj = MyClass()

print(obj.strategy)

obj.strategy = "new strategy"

print(obj.strategy)

obj.strategy = "new strategy2"

print(obj.strategy)
