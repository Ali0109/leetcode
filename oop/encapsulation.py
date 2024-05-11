class Car:
    def __init__(self, brand, model):
        self._brand = brand
        self.__model = model

    def get_model(self):
        return self.__model

    def set_model(self, new_model):
        self.__model = new_model


my_car = Car("Toyota", "Corolla")

print(my_car.get_model())
my_car.set_model("Camry")
print(my_car.get_model())
