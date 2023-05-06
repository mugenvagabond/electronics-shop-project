import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # self.all.append(self)

    @property
    def name(self):
        """
        Декоратор, делающий поле name private
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Декоратор, позволяющий атрибуту name в режиме private присваивать новые значения при обращении через
        экземпляр класса к атрибуту.
        Выполняет проверку на количество символов в строке и возвращает соответствующие сообщения
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов")

    def __repr__(self):
        """
        Магический метод, который выводит форматированную строку с данными об экземпляре класса и его полями
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Магический метод, который выводит конкретное поле в экземпляре класса
        """
        return f'{self.name}'

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv
        Возвращает строку с данными о количестве записей о товарах
        """
        path = os.path.join("items.csv")

        with open(path, newline='') as file:
            reader = csv.DictReader(file)
            cls.all.clear()
            for row in reader:
                cls.all.append(cls(row['name'], float(row['price']), int(row['quantity'])))
        return len(cls.all)

    @staticmethod
    def string_to_number(number):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(number))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = int(self.price * self.quantity)
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = float(self.price * self.pay_rate)
