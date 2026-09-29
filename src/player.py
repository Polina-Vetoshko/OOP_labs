"""Игрок."""

from .ui import UI


class Player:
    """Игрок: имя, счётчик попыток, взаимодействие с UI."""

    def __init__(self, name: str, ui: UI):
        self._name = name
        self._attempts = 0
        self._ui = ui

    @property
    def name(self) -> str:
        return self._name

    @property
    def attempts(self) -> int:
        return self._attempts

    def make_guess(self) -> int:
        while True:
            try:
                return int(self._ui.get_input("Ваш вариант: "))
            except ValueError:
                self._ui.show_message("Введите целое число!")

    def increment_attempts(self) -> None:
        self._attempts += 1
