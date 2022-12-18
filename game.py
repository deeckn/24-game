from PySide6.QtWidgets import QWidget, QHBoxLayout, QMessageBox
from PySide6.QtCore import Qt
from components.core import CoreSection
from components.controls import Controls
from components.history import HistoryTab
import theme
from service import GameService


class Game(QWidget):
    def __init__(self):
        super().__init__(None)

        self.service = GameService()

        # Window setup
        self.setWindowTitle("24 Game")
        self.setGeometry(400, 180, 1080, 720)
        self.setStyleSheet(f"""
            background-color: {theme.colors.get("dark")};
        """)

        # Layout
        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)

        # Page components
        self.core_widget = CoreSection()
        self.controls = Controls()
        self.history_tab = HistoryTab()

        self.core_widget.set_question(self.service.get_question())

        # Insert components
        self.layout.addWidget(self.history_tab, 1)
        self.layout.addWidget(self.core_widget, 2)
        self.layout.addWidget(self.controls, 1)

        # Behavior
        self.core_widget.set_submit_btn_on_click(self.submit)
        self.core_widget.set_skip_btn_on_click(self.skip)
        self.core_widget.set_reveal_btn_on_click(self.reveal)

    def submit(self):
        # Input validation
        user_input = self.core_widget.get_user_input().replace(" ", "")
        if not self.service.is_input_valid(user_input):
            return

        # Calculate result
        user_result = self.service.calculate_result(user_input)

        # Add to history
        self.history_tab.add_history(user_input, user_result)

        # Check correctness
        if self.service.is_correct(user_result):
            self.service.increment_current_score()
            current_score = self.service.get_current_score()
            self.controls.set_current_score(current_score)
            self.core_widget.reset_user_input()

            high_score = self.service.get_high_score()
            self.controls.set_high_score(high_score)

            question = self.service.get_question()
            self.core_widget.set_question(question)
        else:
            print("Incorrect")

    def skip(self):
        self.service.increment_skip_count()
        self.controls.set_skip_count(self.service.get_skip_count())

        question = self.service.get_question()
        self.core_widget.set_question(question)

    def reveal(self):
        solution = self.service.get_solution()
        QMessageBox.information(None, "Solution", solution)
