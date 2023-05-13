from src.item import Item


class LanguageMixin:
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        else:
            raise AttributeError('property "language" of "KeyBoard" object has no setter')
        return self


class KeyBoard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
