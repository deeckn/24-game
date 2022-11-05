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
        self.answer_rate = 0
        self.current_question = str()

        self.random = 0

    def get_question(self) -> str:
        questions = ["1 2 3 4", "4 3 2 1", "5 5 4 1"]
        self.random += 1
        return questions[self.random % 3]

    def calculate_result(self, user_input: str) -> int:
        # Apply shunting yard algorithm here
        return 24

    def is_correct(self, result: int):
        return result == 24

    def increment_current_score(self):
        self.current_score += 1

    def get_current_score(self) -> int:
        return self.current_score

    def increment_skip_count(self):
        self.skipped += 1

    def get_skip_count(self) -> int:
        return self.skipped
