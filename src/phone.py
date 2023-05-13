# coding=utf-8
from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Инициализатор, который наследует поля класса Item и добавляет новое - number_of_sim
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Выводит информацию о названии класса и его полях в строковом виде
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Позволяет вызывать приватное поле __number_of_sim
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """
        Сеттер, который выполняет проверку на целое, неотрицательное число и в зависимости от результата
        проверки - либо даёт возможность перезадать поле number_of_sim, либо выдаёт ошибку ValueError с текстом ошибки
        """
        if number_of_sim >= 1 and isinstance(number_of_sim, int):
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
