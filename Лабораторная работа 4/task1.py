class Animal:
    """Базовый класс Животное."""

    def __init__(self, name: str, species: str):
        """
        Инициализирует объект Животное.
        Args:
            name (str): Имя животного.
            species (str): Вид животного.
        """
        self.name = name
        self.species = species

    def make_sound(self) -> str:
        """
        Воспроизводит звук животного.
        Returns:
            str: Звук, издаваемый животным.
        """
        pass

    def __str__(self) -> str:
        """
        Возвращает начальное представление объекта.
        Returns:
            str: Начальноее представление объекта.
        """
        return f"{self.name} - {self.species}"

    def __repr__(self) -> str:
        """
        Возвращает начальное представление объекта для вывода в интерпретаторе.
        Returns:
            str: Начальное представление объекта.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, species={self.species!r})"


class Cat(Animal):
    """Дочерний класс Кошка, наследующий от базового класса Животное."""

    def __init__(self, name: str, breed: str):
        """
        Инициализирует объект Кошка.
        Args:
            name (str): Имя кошки.
            breed (str): Порода кошкии.
        """
        super().__init__(name, species="Кошка")
        self.breed = breed

    def wag_tail(self) -> str:
        """
        Имитирует виляние хвостом.
        Returns:
            str: Сообщение о вилянии хвостом.
        """
        pass

    def make_sound(self) -> str:
        """
        Воспроизводит мяуканье кошки.
        Returns:
            str: Звук мяуканья.
        """
        return "Мяу-мяу"

    def __repr__(self) -> str:
        """
        Возвращает начальное представление объекта для вывода в интерпретаторе.
        Returns:
            str: Начальное представление объекта.
        """
        return f"{self.__class__.__name__}(name={self.name!r}, breed={self.breed!r})"
