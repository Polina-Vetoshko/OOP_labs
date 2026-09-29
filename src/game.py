"""Игра «Угадай число»."""

import random

from .ui import UI
from .player import Player


class Game:
    """Управляет игровым циклом «Угадай число»."""

    def __init__(self, max_attempts: int = 10, ui: UI | None = None):
        self._max_attempts = max_attempts
        self._secret = 0
        self._ui = ui if ui is not None else UI()

    def run(self) -> None:
        self._secret = random.randint(1, 100)
        self._ui.show_message(
            f"Я загадал число от 1 до 100. "
            f"У вас {self._max_attempts} попыток."
        )
        player = Player("Игрок", self._ui)
        while player.attempts < self._max_attempts:
            guess = player.make_guess()
            player.increment_attempts()
            self._ui.show_message(self.check_guess(guess))
            if guess == self._secret:
                return
        self._ui.show_message(
            f"Попытки закончились. Было загадано: {self._secret}"
        )

    def check_guess(self, guess: int) -> str:
        if guess < self._secret:
            return "Больше!"
        elif guess > self._secret:
            return "Меньше!"
        return "Угадали!"

    @property
    def secret(self) -> int:
        return self._secret
