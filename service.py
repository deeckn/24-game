from PySide6.QtWidgets import QMessageBox
from shunting_yard import ShuntingYard
from pyswip import Prolog
from random import randint


class GameService:
    CONSULT_FILE = "24_consult.pl"
    current_score: int
    high_score: int
    skipped: int
    answer_rate: float
    current_question: str
    prolog: Prolog

    def __init__(self):
        self.current_score = 0
        self.high_score = 0
        self.skipped = 0
        self.current_question = str()
        self.calculator = ShuntingYard()
        self.prolog = Prolog()
        self.prolog.consult(GameService.CONSULT_FILE)

        # Mock variable
        self.random = 0

    def __generate_question(self):
        numbers = [randint(1, 9) for _ in range(4)]
        while not bool(list(self.prolog.query(f"solve24order({numbers},R)."))):
            numbers = [randint(1, 9) for _ in range(4)]

        self.current_question = list(map(str, numbers))

    def get_question(self) -> str:
        self.__generate_question()
        return self.current_question

    def get_current_score(self) -> int:
        return self.current_score

    def get_high_score(self):
        return self.high_score

    def get_skip_count(self) -> int:
        return self.skipped

    def increment_skip_count(self):
        self.skipped += 1

    def increment_current_score(self):
        self.current_score += 1

        if self.current_score > self.high_score:
            self.high_score = self.current_score

    def calculate_result(self, user_input: str) -> int:
        return self.calculator.compute(user_input)

    def is_correct(self, result: int) -> bool:
        return result == 24

    def is_input_valid(self, user_input: str) -> bool:
        if len(user_input) == 0:
            return False

        allowed_characters = list("123456789+-*/() ")
        for char in user_input:
            if char not in allowed_characters:
                QMessageBox.information(
                    None, "Invalid", "Please enter a mathematical expression.")
                return False

        available_numbers = list(self.current_question)
        user_numbers = []
        for num in user_input:
            if num.isalnum():
                user_numbers.append(num)

        for num in user_numbers:
            if user_numbers.count(num) != available_numbers.count(num):
                QMessageBox.information(
                    None, "Invalid", "Please use all four numbers only once")
                return False

        return True
