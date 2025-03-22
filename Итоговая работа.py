class Coniferous_trees:
    """
    Базовый класс для представления хвойных деревьев в питомнике.
    Атрибуты: класс, порода, год высадки, высота
        species (str): species of tree.
        subspecies (str): class of tree.
        year_of_tree_planting (int): year.
        height_of_the_tree (float): height in meters.
    """

    def __init__(self, species: str, subspecies: str, year_of_tree_planting: int, height_of_the_tree: float):
        """
        Конструктор класса деревьев.
        :param species: класс дерева.
        :param subspecies: порода.
        :param year_of_tree_planting: Год высадки.
        :param height_of_the_tree: высота в метрах.
        """
        self.species = species
        self.subspecies = subspecies
        self.year_of_tree_planting = year_of_tree_planting
        self.height_of_the_tree = height_of_the_tree

    def __str__(self) -> str:
        """
        Возвращает строковое представление дерева.
        :return: Строка с описанием дерева.
        """
        return f"{self.species} {self.subspecies} ({self.year_of_tree_planting}), height_of_the_tree: {self.height_of_the_tree} m"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление дерева.
        :return: Формальное строковое представление.
        """
        return f" Хвойное_дерево (класс={self.species!r}, порода={self.subspecies!r}, год_высадки={self.year_of_tree_planting!r}, высота={self.height_of_the_tree!r})"

    def increase_height(self, height: float) -> None:
        """
        Увеличивает высоту дерева на заданное расстояние в метрах.
        :param height: Расстояние в метрах, на которое нужно увеличить высоту дерева.
        """
        if height < 0:
            raise ValueError("Высота не может быть отрицательной.")
        self.height_of_the_tree += height


class Yew_tree(Coniferous_trees):
    """
    Дочерний класс для представления хвойного дерева, Тис.
    Атрибуты:
        species (str): species of tree.
        subspecies (str): class of tree.
        year_of_tree_planting (int): year.
        height_of_the_tree (float): height in meters.
        watering (float): watering a tree in cubic meters.
    """

    def __init__(self, species: str, subspecies: str, year_of_tree_planting: int, height_of_the_tree: float, watering: float):
        """
        Конструктор класса Тис.
        :param species: класс дерева.
        :param subspecies: порода.
        :param year_of_tree_planting: Год высадки.
        :param height_of_the_tree: высота в метрах.
        :param watering: полив дерева в метрах кубических в день.
        """
        super().__init__(species, subspecies, year_of_tree_planting, height_of_the_tree)
        self.watering = watering

    def __str__(self) -> str:
        """
        Возвращает строковое представление класса Тис.
        :return: Строка с описанием класса Тис.
        """
        return f"{super().__str__()}, watering: {self.watering} m3"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление Тиса.
        :return: Формальное строковое представление.
        """
        return f"Тис(класс={self.species!r}, порода={self.subspecies!r}, год_высадки={self.year_of_tree_planting!r}, высота={self.height_of_the_tree!r}, полив={self.watering!r})"

    def increase_watering(self, water: float) -> None:
        """
        Увеличивает полив дерева на заданное колличество.
        Перегруженный метод, который также выводит сообщение о том, что полив увеличен.
        :param water: Колличество воды в метрах кубических, на которое нужно увеличить полив.
        """
        super().increase_watering(water)
        print(f"Полив дерева  {self.species} {self.subspecies} ({self.year_of_tree_planting}) увеличен на {water} м3.")


class Pine(Coniferous_trees):
    """
    Дочерний класс для представления хвойного дерева, Сосна.
    Атрибуты:
        species (str): species of tree.
        subspecies (str): class of tree.
        year_of_tree_planting (int): year.
        height_of_the_tree (float): height in meters.
        watering (float): watering a tree in cubic meters.
    """

    def __init__(self, species: str, subspecies: str, year_of_tree_planting: int, height_of_the_tree: float, watering: float):
        """
        Конструктор класса Сосна.
        :param species: класс дерева.
        :param subspecies: порода.
        :param year_of_tree_planting: Год высадки.
        :param height_of_the_tree: высота в метрах.
        :param watering: полив дерева в метрах кубических в день.
        """
        super().__init__(species, subspecies, year_of_tree_planting, height_of_the_tree)
        self.watering = watering

    def __str__(self) -> str:
        """
        Возвращает строковое представление класса Сосна.
        :return: Строка с описанием класса Сосна.
        """
        return f"{super().__str__()}, watering: {self.watering} m3"

    def __repr__(self) -> str:
        """
 Возвращает формальное строковое представление класса Сосна.
 :return: Формальное строковое представление.
        """
        return f"Сосна(класс={self.species!r}, порода={self.subspecies!r}, год_высадки={self.year_of_tree_planting!r}, высота={self.height_of_the_tree!r}, полив={self.watering!r})"

    def increase_watering(self, water: float) -> None:
        """
 Увеличивает полив дерева на заданное колличество в метрах кубических.
 :param water: Колличество воды в метрах в кубе, на которое нужно увеличить полив дерева.
        """
        if water < 0:
            raise ValueError("полив не может быть отрицательным.")
        self.  watering+=water


if __name__ == "__main__":
    # Создаем объекты классов
    Тис = Yew_tree("Taxales", "Taxus_canadensis", 1998, 20.5, 10.0)
    Сосна = Pine("Pinales", "Pinus_silvestris", 2000, 10.0, 8.0)

    # Выводим информацию о деревьях
    print(Тис)
    print(Сосна)

    # Увеличиваем высоту
    Тис.increase_height(10.2)
    Сосна.increase_height(8.0)

    # Выводим обновленную информацию
    print(Тис)
    print(Сосна)

