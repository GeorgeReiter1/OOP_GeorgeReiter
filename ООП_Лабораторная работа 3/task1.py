class Game:
    """Базовый класс, представляющий игру"""
    def __init__(self, title: str, number_of_players: int, year: int):
        """Инициализация игры"""
        self.title = title
        self.number_of_players = number_of_players
        self.year = year

    def __repr__(self):
        """Представление объекта строковое"""
        return f"{self.__class__.__name__}(title={self.title}, number_of_players={self.number_of_players}, year={self.year})"

    def __str__(self):
        """представление игры"""
        return f"{self.title} ({self.year}), Количество игроков: {self.number_of_players}"

    def setup(self):
        """Подготовка игры"""
        pass

    def play(self):
        """Начать игру"""
        pass


class VideoGame(Game):
    """Класс, представляющий видеоигру, наследуется от Game"""
    def __init__(self, title: str, number_of_players: int, year: int, platform: str):
        """Инициализация видеоигры"""
        super().__init__(title, number_of_players, year)
        self.platform = platform

    def install(self):
        """Установка видеоигру"""
        pass

    def play_online(self):
        """Играть в видеоигру онлайн"""
        pass


class BoardGame(Game):
    """Класс, представляющий настольную игру, наследуется от Game"""
    def __init__(self, title: str, number_of_players: int, year: int, material_of_manufacture: str):
        """Инициализация настольной игры"""
        super().__init__(title, number_of_players, year)
        self.material_of_manufacture = material_of_manufacture

    def setup(self):
        """Переопределенный метод подготовки для настольной игры."""
        # Дополнительные шаги для настройки настольной игры, например расстановка игровых элементов
        super().setup()

    def play(self):
        """Переопределенный метод игры для учета правил конкретной настольной игры."""
        # Правила, специфичные для настольных игр, такие как способ бросать кубики или доставать карты
        super().play()


if __name__ == "__main__":
    # Создаем экземпляр настольной игры
    monopoly = BoardGame(title="Монополия", number_of_players=2, year=1935, material_of_manufacture="Бумага и пластик")

    # Создаем экземпляр видеоигры
    minecraft = VideoGame(title="Minecraft", number_of_players=1, year=2011, platform="PC")

    # Выводим информацию о настольной игре
    print(monopoly)
    monopoly.setup()
    monopoly.play()

    # Выводим информацию о видеоигре
    print(minecraft)
    minecraft.install()
    minecraft.play_online()

