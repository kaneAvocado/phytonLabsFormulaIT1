class Table:
    def __init__(self, material: str, dimensions: tuple, color: str):
        self.material = material
        self.dimensions = dimensions
        self.color = color

    def resize(self, new_dimensions: tuple):
        """ Изменяет размеры стола.
        Args:
            new_dimensions (tuple): Новые размеры стола.
        """

    def repaint(self, new_color: str):
        """ Перекрашивает стол в другой цвет.
        Args:
            new_color (str): Новый цвет стола.
        """


    def move(self, new_position: tuple):
        """ Перемещает стол в новое место.
        Args:
            new_position (tuple): Координаты нового местоположения стола.
        """

class Tree:
    def __init__(self, species: str, age: int, height: float):
        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int):
        """ Увеличивает высоту дерева за указанное количество лет.
        Args:
            years (int): Количество лет для роста.
        """


    def trim(self, new_height: float):
        """ Обрезает дерево до указанной высоты.
        Args:
            new_height (float): Новая высота дерева.
        """

    def fertilize(self, fertilizer_type: str):
        """ Удобряет дерево указанным типом удобрения.
        Args:
            fertilizer_type (str): Тип удобрения.
        """

class SocialNetwork:
    def __init__(self, name: str, user_count: int, is_private: bool):
        self.name = name
        self.user_count = user_count
        self.is_private = is_private

    def add_user(self, user_name: str):
        """ Добавляет нового пользователя в социальную сеть.
        Args:
            user_name (str): Имя пользователя.
        """


    def remove_user(self, user_name: str):
        """ Удаляет пользователя из социальной сети.
        Args:
            user_name (str): Имя пользователя.
        """


    def change_privacy_settings(self, new_privacy_setting: bool):
        """ Изменяет настройки приватности социальной сети.
        Args:
            new_privacy_setting (bool): Новая настройка приватности.
        """

