from src.item import Item


class LanguageMixin:
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        """
        Сеттер для поля language
        """
        return self.__language

    def change_lang(self):
        """
        Метод для изменения раскладки клавиатуры.
        По-умолчанию задан язык клавиатуры - 'EN'
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        else:
            raise AttributeError('property "language" of "KeyBoard" object has no setter')
        return self


class KeyBoard(Item, LanguageMixin):
    """
    Класс, для товара - клавиатуры, который наследует поля класса Item.
    У класса LanguageMixin есть свой атрибут language и метод для изменения языка (раскладки клавиатуры), которые
    добавляются в цепочку наследования класса KeyBoard.
    """
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
