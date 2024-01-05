# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Laptop:
    """
    Класс описывает объем оперативной памяти (RAM) ноутбука и потребляемой памяти
    """
    def __init__(self, random_access_memory: Union[int, float], memory_consumption: Union[int, float]):
        """
        :param random_access_memory: Объем оперативной памяти в гигабайтох
        :param memory_consumption: Потребляемая память в гигабайтах
        Example:
        >>> laptop1 = Laptop(32, 10) # инициализация экземпляра класса
        """
        self.random_access_memory = None
        self.init_random_access_memory(random_access_memory)
        self.memory_consumption = None
        self.init_memory_consumption(memory_consumption)

    def init_random_access_memory(self, random_access_memory: Union[int, float]):
        """
        Метод проводит валидацию аргумента random_access_memory на соответствие нужному
        типу аннотации и возможного значения
        :param random_access_memory: Объем оперативной памяти в гигабайтох
        """
        if not isinstance(random_access_memory, (int, float)):
            raise TypeError
        if not random_access_memory > 0:
            raise ValueError
        self.random_access_memory = random_access_memory

    def init_memory_consumption(self, memory_consumption: Union[int, float]):
        """
        Метод проводит валидацию аргумента memory_consumption на соответствие нужному
        типу аннотации и возможного значения
        :param memory_consumption: Потребляемая память в гигабайтах
        """

        if not isinstance(memory_consumption, (int, float)):
            raise TypeError
        if not memory_consumption >= 0:
            raise ValueError
        if not memory_consumption < self.random_access_memory:
            raise ValueError
        self.memory_consumption = memory_consumption


class CoffeeMachine:
    """
    Класс описывает количество типов напитков (кофе), которые сможет сделать кофемашина
    """
    def __init__(self, number_of_coffee_types: int, cappuccino_maker: bool, mouthpiece_for_water: bool):

        """
        :param number_of_coffee_types: Количество видов напитков
        :param cappuccino_maker: Наличие капучинатора
        :param mouthpiece_for_water: Наличие крана для подачи кипятка
        Example:
        >>> CoffeeMachine1 = CoffeeMachine(8, True, False) # инициализация экземпляра класса
        """

        if not isinstance(number_of_coffee_types, int):
            raise TypeError("Должно быть целое число")
        if not number_of_coffee_types > 0:
            raise ValueError("Должно быть положительное число")
        self.number_of_coffee_types = number_of_coffee_types

        if not isinstance(cappuccino_maker, bool):
            raise TypeError("Наличие капучинатора должно быть типа bool")
        self.cappuccino_maker = cappuccino_maker

        if not isinstance(mouthpiece_for_water, bool):
            raise TypeError("Наличие крана для подачи кипятка должно быть типа bool")
        self.mouthpiece_for_water = mouthpiece_for_water

    def add_milk(self, milk: bool) -> None:
        """
        Метод проверяет наличие капучинатора и молока.
        Если и то и другое присутствует, количество видов напитков увеличивается на 4.
        :param milk: Наличие молока
        >>> CoffeeMachine1 = CoffeeMachine(8, True, False)
        >>> CoffeeMachine1.add_milk(True)
        """
        if not isinstance(milk, bool):
            raise TypeError
        ...

    def add_tea(self, tea: bool) -> None:
        """
        Метод проверяет наличие крана для подачи кипятка и чая.
        Если и то и другое присутствует, количество видов напитков увеличивается на 3.
        :param tea: Наличие чая
        >>> CoffeeMachine1 = CoffeeMachine(8, False, True)
        >>> CoffeeMachine1.add_tea(True)
        """
        if not isinstance(tea, bool):
            raise TypeError
        ...


class GarbageCollection:
    """
    Класс описывает тип мусора и наполненность мусорного ведра
    """
    def __init__(self, garbage_type: str, bin_capacity: int, fullness: Union[int, float]):
        """
        :param garbage_type: Тип мусора
        :param bin_capacity: Вместимость ведра, условные единицы
        :param fullness: наполненность ведра
        Example:
        >>> garbageCollection1 = GarbageCollection("Сжигаемый мусор", 100, 50) # инициализация экземпляра класса
        """

        if not isinstance(garbage_type, str):
            raise TypeError("Тип данных - текст")
        self.garbage_type = garbage_type

        if not isinstance(bin_capacity, int):
            raise TypeError("Должно быть целое число")
        if not bin_capacity > 0:
            raise ValueError("Должно быть положительное число")
        self.bin_capacity = bin_capacity

        if not isinstance(fullness, (int, float)):
            raise TypeError("Должно быть число")
        if not fullness >= 0:
            raise ValueError("Не может быть отрицательным")
        self.fullness = fullness

    def add_garbage(self, garbage_type: str, amount: Union[int, float]) -> None:
        """
        Метод проверяет тип мусора и довавляет его в корзину, если мусор подходит для корзины.
        :param garbage_type: Тип мусора
        :param amount: количество нового мусора
        >>> garbageCollection1 = GarbageCollection("Сжигаемый мусор", 100, 50)
        >>> garbageCollection1.add_garbage("Сжигаемый мусор", 50)
        """
        if not isinstance(garbage_type, str):
            raise TypeError("Тип данных - текст")

        if not isinstance(amount, (int, float)):
            raise TypeError("Должно быть число")
        if not amount >= 0:
            raise ValueError("Не может быть отрицательным")
        ...

    def time_to_throw_out(self) -> bool:
        """
        Метод проверяет заполненность мусорки и выдает True, если мусорка заполнена
        на 75% или больше.
        :return: Мусор пора выкинуть
        >>> garbageCollection1 = GarbageCollection("Сжигаемый мусор", 100, 50)
        >>> garbageCollection1.time_to_throw_out()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
