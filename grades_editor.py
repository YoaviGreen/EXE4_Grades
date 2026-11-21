from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QSpinBox
from About import AboutWindow

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.about_window = AboutWindow()

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Grades Fixer')
        self.setGeometry(100, 100, 600, 640)

        self.choose_button = QPushButton('Choose File', self)
        self.choose_button.setGeometry(20, 20, 140, 35)

        self.file_label = QLabel('Selected file:', self)
        self.file_label.setGeometry(180, 20, 100, 35)

        self.file_box = QLineEdit(self)
        self.file_box.setGeometry(285, 20, 295, 35)
        self.file_box.setReadOnly(True)
        self.file_box.setObjectName('output')
        self.file_box.setPlaceholderText('No file selected')

        self.bonus_label = QLabel('Bonus points:', self)
        self.bonus_label.setGeometry(20, 75, 110, 35)

        self.bonus_box = QSpinBox(self)
        self.bonus_box.setGeometry(135, 75, 100, 35)
        self.bonus_box.setRange(0, 100)

        self.update_button = QPushButton('Update File', self)
        self.update_button.setGeometry(255, 75, 150, 35)

        self.about_button = QPushButton('About', self)
        self.about_button.setGeometry(440, 75, 140, 35)
        self.about_button.clicked.connect(self.show_about_window)

    def show_about_window(self):
        self.about_window.show()

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()