import doctest


class Road:
    def __init__(self,distance: float, traveled_distance: float):
        """
        :param distance: Длина дороги
        :param traveled_distance: Пройденное расстояние

        >>> road = Road(500, 200)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Длина дороги должна быть типа int или float')
        if distance < 0:
            raise ValueError('Число должно быть положительным')
        self.distance = distance

        if not isinstance(traveled_distance, (int, float)):
            raise TypeError('Оставшаяся длина дороги должна быть типа int или float')
        if traveled_distance < 0:
            raise ValueError('Число должно быть положительным')
        self.traveled_distance = traveled_distance

    def remaining_distance(self) -> float:
        """
        Нахождение оставщейся дистанции

        :return: Оставшаяся дистанция

        >>> distance = Road(500, 200).remaining_distance()
        """
        ...

    def remaining_travel_time(self, average_speed: float = 60) -> float:
        """
        Нахождение оставшегося времени в пути

        :param average_speed: Средняя скорость машины
        :return: Остаток времени в пути в часах

        >>> time = Road(500, 200).remaining_travel_time(60)
        """
        if not isinstance(average_speed, (int, float)):
            raise TypeError('Скорость должна быть типа int или float')
        if average_speed < 0:
            raise ValueError('Скорость должна быть положительным числом')
        ...

class Paper:
    def __init__(self, symbols: int, symbols_in_string: int):
        """
        :param symbols: Количество символов
        :param symbols_in_string: Количество символов в строке

        >>> paper = Paper(1000, 100)
        """
        if not isinstance(symbols, int):
            raise TypeError('Количество символов должно быть типа int')
        if symbols < 0:
            raise ValueError('Количество символов должно быть положительным числом')
        self.symbols = symbols

        if not isinstance(symbols_in_string, int):
            raise TypeError('Количество символов в строке должно быть типа int')
        if symbols_in_string < 0:
            raise ValueError('Количество символов в строке должно быть положительнымм числом')
        self.symbols_in_string = symbols_in_string

    def number_of_lines(self) -> int:
        """
        Нахождение количества строк на которых разместится текст

        :return: Количество строк в тексте

        >>> string = Paper(1000, 100).number_of_lines()
        """
        ...

    def number_of_pages(self, string_in_paper: int) -> int:
        """
        Нахождение количества страниц на которых разместится текст

        :param string_in_paper: Количество строк в одной странице
        :return: Количество строниц

        >>> pages = Paper(1000, 100).number_of_pages(10)
        """
        if not isinstance(string_in_paper, int):
            raise TypeError('Количство строк на одной странице должно быть типа int')
        if string_in_paper < 0:
            raise ValueError('Количество строк на одной странице должно быть положительным числом')
        ...

class Poultry_farm:
    def __init__(self, number_of_eggs : int, count_of_week: int):
        """
        :param number_of_eggs: Количество яиц на птицефабрике
        :param count_of_week: Количество недель за которые было полученно такое количество яиц

        >>> farm = Poultry_farm(1000, 10)
        """
        if not isinstance(number_of_eggs, int):
            raise TypeError('')
        if number_of_eggs < 0:
            raise ValueError('')
        self.number_of_egg = number_of_eggs

        if not isinstance(count_of_week, int):
            raise TypeError('')
        if count_of_week < 0:
            raise ValueError('')
        self.count_of_week = count_of_week

    def speed_of_eggs(self) -> int:
        """
        Нахождение скорости получения яиц с птицефабрики за неделю

        :return: Скорость получения яиц с одной птицефабрики за одну неделю

        >>> speed = Poultry_farm(1000, 10)
        """
        ...

    def count_of_chicken(self, eggs_from_chicken: int = 10) -> int:
        """
        Нахождение количества куриц на птицефабрики

        :param eggs_from_chicken: Количество яиц получаемых с одной курицы в неделю
        :return: Количество куриц на одной птицефабрике

        >>> chicken = Poultry_farm(1000, 10).count_of_chicken(10)
        """
        if not isinstance(eggs_from_chicken, int):
            raise TypeError('')
        if eggs_from_chicken < 0:
            raise ValueError('')
        ...


if __name__ == "__main__":
    doctest.testmod()

