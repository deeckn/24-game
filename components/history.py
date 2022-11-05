from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
import theme


class HistoryTab(QWidget):
    def __init__(self):
        super().__init__(None)
        self.setStyleSheet("background-color: #333333;")

        # Layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)

        # Page components
        self.title = QLabel("History")

        # Insert widgets to layout
        self.layout.addWidget(self.title)

        # Styling
        self.layout.setSpacing(0)

        self.title.setFont(theme.font_bold)
        self.title.setStyleSheet(
            f"color: {theme.colors.get('white')}; padding: 8px 16px;")
        self.title.setAlignment(Qt.AlignCenter)

    def add_history(self, user_input, result):
        label = QLabel(text=f"{user_input} = {result}")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(theme.font_normal)
        label.setStyleSheet(f"color: {theme.colors.get('white')}")
        self.layout.addWidget(label)
