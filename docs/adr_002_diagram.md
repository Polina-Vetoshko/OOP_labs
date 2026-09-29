Задание 2.1

Принята следующая диаграмма классов:

```mermaid
classDiagram
    class Game {
        -secret: int
        -max_attempts: int
        -ui: UI
        +run(): void
        +check_guess(guess: int): str
        +secret: int
    }

    class Player {
        -name: str
        -attempts: int
        -ui: UI
        +make_guess(): int
        +increment_attempts(): void
        +name: str
        +attempts: int
    }

    class UI {
        +show_message(message: str): void
        +get_input(prompt: str): str
    }

        Game --> UI : uses
        Game --> Player : creates
        Player --> UI : uses


1. Наследования нет.

В текущей архитектуре нет классов, которые должны наследоваться друг от друга.
Game, Player и UI решают разные задачи и не образуют отношение
«является» (is-a).


2. Композиция есть между Game и Player.

Game создаёт объект Player внутри метода run() и управляет его
жизненным циклом. Игрок существует в рамках конкретной игры.
Поэтому на диаграмме используется композиция:


3. Циклических зависимостей нет.

Направление зависимостей:

text
Game  →  Player
Game  →  UI
Player → UI
UI не зависит ни от Game, ни от Player.
Поэтому цикла вида A → B → A нет.


