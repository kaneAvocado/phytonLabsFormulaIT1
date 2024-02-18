class Automobile:
    """Базовый класс для автомобилей."""

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def __repr__(self):
        return f"Automobile('{self.brand}', '{self.model}', {self.year})"

    def start_engine(self) -> str:
        """Метод для запуска двигателя."""
        return "Engine started"

class PassengerCar(Automobile):
    """Дочерний класс для легковых автомобилей."""

    def __init__(self, brand: str, model: str, year: int, passengers: int):
        super().__init__(brand, model, year)
        self.passengers = passengers

    def __str__(self):
        return super().__str__() + f", Passengers: {self.passengers}"

    def start_engine(self) -> str:
        """Перегруженный метод для запуска двигателя с добавлением особенностей легкового автомобиля."""
        return super().start_engine() + " - smooth and quiet"

class Truck(Automobile):
    """Дочерний класс для грузовых автомобилей."""

    def __init__(self, brand: str, model: str, year: int, payload: float):
        super().__init__(brand, model, year)
        self.payload = payload  # Вес груза, который может перевозить грузовик

    def __str__(self):
        return super().__str__() + f", Payload: {self.payload} tons"

    def load_cargo(self, weight: float) -> str:
        """Метод для загрузки груза в грузовик."""
        return f"Loading {weight} tons of cargo"
