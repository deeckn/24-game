from shunting_yard import ShuntingYard


class GameService:
    current_score: int
    high_score: int
    skipped: int
    answer_rate: float
    current_question: str

    def __init__(self):
        self.current_score = 0
        self.high_score = 0
        self.skipped = 0
        self.current_question = str()
        self.calculator = ShuntingYard()

        # Mock variable
        self.random = 0

    def get_question(self) -> str:
        # Use Prolog here

        # Mock data
        questions = ["1 2 3 4", "4 3 2 1", "5 5 4 1"]
        self.random += 1
        return questions[self.random % 3]

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

        return False
