from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt
import theme


class Controls(QWidget):
    def __init__(self):
        super().__init__(None)

        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)

        # Page components
        self.current_score = QLabel(text="Current score: 0")
        self.skipped_count = QLabel(text="Skipped: 0")
        self.high_score = QLabel(text="High score: 0")

        self.start_game_btn = QPushButton(text="Start Game")
        self.practice_game_btn = QPushButton(text="Practice")

        # Insert page components
        self.layout.addWidget(self.current_score)
        self.layout.addWidget(self.skipped_count)
        self.layout.addWidget(self.high_score)
        # self.layout.addWidget(self.start_game_btn)
        # self.layout.addWidget(self.practice_game_btn)

        # Styling
        self.current_score.setStyleSheet(f"""
            color: {theme.colors.get("white")};
        """)

        self.current_score.setFont(theme.font_normal)

        self.skipped_count.setStyleSheet(f"""
            color: {theme.colors.get("white")};
        """)

        self.skipped_count.setFont(theme.font_normal)

        self.high_score.setStyleSheet(f"""
            color: {theme.colors.get("white")};
        """)

        self.high_score.setFont(theme.font_normal)

        self.start_game_btn.setStyleSheet(f"""
            color: {theme.colors.get("primary")};
            background-color: {theme.colors.get("white")};
            border-radius: 5px;
            max-width: 100px;
            padding: 4px 8px;
        """)

        self.start_game_btn.setFont(theme.font_bold)

        self.practice_game_btn.setStyleSheet(f"""
            color: {theme.colors.get("primary")};
            background-color: {theme.colors.get("white")};
            border-radius: 5px;
            max-width: 100px;
            padding: 4px 8px;
        """)

        self.practice_game_btn.setFont(theme.font_bold)

    def set_current_score(self, score: int):
        self.current_score.setText(f"Current score: {score}")

    def set_high_score(self, score: int):
        self.high_score.setText(f"High score: {score}")

    def set_skip_count(self, skipped: int):
        self.skipped_count.setText(f"Skipped: {skipped}")
