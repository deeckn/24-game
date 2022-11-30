from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
import theme


class CoreSection(QWidget):
    def __init__(self):
        super().__init__(None)

        # Layout
        self.layout = QVBoxLayout(self)

        # Page elements
        self.title_label = QLabel(text="24 Game")
        self.question_label = QLabel(text="5 5 4 1")

        self.input_label = QLabel(text="Type your answer here:")
        self.answer_input = QLineEdit()

        self.button_container = QWidget()
        self.button_container_layout = QHBoxLayout()
        self.skip_button = QPushButton(text="Skip")
        self.reveal_button = QPushButton(text="Reveal")
        self.submit_button = QPushButton(text="Submit")

        self.credit_label = QLabel(
            text="Game made by Chakrin Deesit and Tawan Lekngam")

        # Insert components to layout
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.question_label)
        self.layout.addWidget(self.input_label)
        self.layout.addWidget(self.answer_input)

        self.button_container_layout.addWidget(self.skip_button)
        self.button_container_layout.addWidget(self.reveal_button)
        self.button_container_layout.addWidget(self.submit_button)
        self.button_container.setLayout(self.button_container_layout)
        self.layout.addWidget(self.button_container)

        self.layout.addWidget(self.credit_label)

        # Styling
        self.title_label.setStyleSheet(f"""
            font-size: 72pt;
            color: {theme.colors.get("white")};
        """)

        self.title_label.setFont(theme.font_bold)
        self.title_label.setAlignment(Qt.AlignCenter)

        self.question_label.setStyleSheet(f"""
            font-size: 48pt;
            color: {theme.colors.get("white")};
        """)

        self.question_label.setFont(theme.font_bold)
        self.question_label.setAlignment(Qt.AlignCenter)

        self.input_label.setStyleSheet(f"""
            color: {theme.colors.get("white")};
        """)

        self.input_label.setFont(theme.font_normal)

        self.answer_input.setStyleSheet(f"""
            background-color: {theme.colors.get("white")};
            border-radius: 5px;
            max-height: 36px;
            font-size: 12pt;
            padding: 4px 8px;
        """)

        self.answer_input.setFont(theme.font_normal)

        self.skip_button.setStyleSheet(f"""
            background-color: {theme.colors.get("white")};
            color: {theme.colors.get("primary")};
            border-radius: 5px;
            height: 36px;
        """)

        self.skip_button.setFont(theme.font_bold)

        self.reveal_button.setStyleSheet(f"""
            background-color: {theme.colors.get("white")};
            color: {theme.colors.get("primary")};
            border-radius: 5px;
            height: 36px;
        """)

        self.reveal_button.setFont(theme.font_bold)

        self.submit_button.setStyleSheet(f"""
            background-color: {theme.colors.get("primary")};
            color: {theme.colors.get("white")};
            border-radius: 5px;
            height: 36px;
        """)

        self.submit_button.setFont(theme.font_bold)

        self.credit_label.setStyleSheet(f"""
            color: {theme.colors.get("white")};
        """)

        self.credit_label.setFont(theme.font_normal)
        self.credit_label.setAlignment(Qt.AlignCenter)

    def reset_user_input(self):
        self.answer_input.setText("")

    def get_user_input(self):
        return self.answer_input.text()

    def set_submit_btn_on_click(self, function):
        self.submit_button.clicked.connect(function)

    def set_reveal_btn_on_click(self, function):
        self.reveal_button.clicked.connect(function)

    def set_skip_btn_on_click(self, function):
        self.skip_button.clicked.connect(function)

    def set_question(self, question: str):
        self.question_label.setText(" ".join(list(question)))
