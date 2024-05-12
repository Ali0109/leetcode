from abc import ABCMeta, abstractmethod


class IScales(metaclass=ABCMeta):
    @abstractmethod
    def get_weight(self):
        pass


class RussianScales(IScales):
    def __init__(self, current_weight: float):
        self.__current_weight = current_weight

    def get_weight(self):
        return self.__current_weight


class BritishScales(IScales):
    def __init__(self, current_weight: float):
        self.__current_weight = current_weight

    def get_weight(self):
        return self.__current_weight


class AdapterBritishScales(BritishScales, IScales):
    def __init__(self, current_weight: float):
        super().__init__(current_weight)

    def get_weight(self):
        return super().get_weight() * 2.20462


if __name__ == "__main__":
    my_weight = 30
    russian_scales = RussianScales(my_weight)
    british_scales = AdapterBritishScales(my_weight)

    print(russian_scales.get_weight())
    print(british_scales.get_weight())
