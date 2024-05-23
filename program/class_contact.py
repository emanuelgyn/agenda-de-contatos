class Contact:
    def __init__(self, name, number, email):
        self.__name = name
        self.__number = number
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    def __str__(self):
        return f'Nome: {self.name}, Nº {self.number}, E-mail: {self.email}'
