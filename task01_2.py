

"""Создать не менее двух дескрипторов для атрибутов классов, которые вы 
создали ранее в ДЗ. Создать метакласс для паттерна Синглтон. Выполнить тесты"""

class IsString:
    def __set__(self, instance, value):
        if type(value) != str:
            raise TypeError(f'{self.my_attr} должно быть строкой')
        elif not value.istitle():
            raise ValueError(f'{self.my_attr} должно быть строкой!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class NonNegative:
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f'{self.my_attr} должно быть числом')
        elif value < 0:
            raise ValueError(f'{self.my_attr} должно быть положителным числом')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker():
    name = IsString()
    surname = IsString()
    wage = NonNegative()
    bonus = NonNegative()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.wage + self.bonus

    def __str__(self):
        return f"Name: {self.get_full_name()}\nSalary: {self.get_total_income()}\n"
    
print(Position)    