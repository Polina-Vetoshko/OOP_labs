"""Интерфейс пользователя."""


class UI:
    """Абстракция над вводом/выводом."""

    def show_message(self, message: str) -> None:
        print(message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)
