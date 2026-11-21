from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QSpinBox, QTableWidget, QTableWidgetItem, QFileDialog
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
        self.choose_button.clicked.connect(self.choose_file)

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

        self.table = QTableWidget(50, 3, self)
        self.table.setGeometry(20, 130, 560, 480)
        self.table.setHorizontalHeaderLabels(['ID', 'Original Grades', 'Corrected Grades'])
        self.table.setColumnWidth(0, 170)
        self.table.setColumnWidth(1, 160)
        self.table.setColumnWidth(2, 160)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

    def choose_file(self):
        file_name, file_filter = QFileDialog.getOpenFileName(self, 'Choose grades file', '', 'CSV files (*.csv)')
        if file_name == '':
            return

        self.selected_file = file_name
        self.file_box.setText(file_name)

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []

        with open(file_name, 'r') as f:
            next(f)
            for line in f:
                student_id, grade = line.strip().split(',')
                self.student_ids.append(student_id)
                self.original_grades.append(int(grade))
                self.corrected_grades.append(int(grade))

        self.bonus_box.setValue(0)
        self.update_table()

    def update_table(self):
        self.table.clearContents()
        for row in range(len(self.student_ids)):
            self.table.setItem(row, 0, QTableWidgetItem(self.student_ids[row]))
            self.table.setItem(row, 1, QTableWidgetItem(str(self.original_grades[row])))
            self.table.setItem(row, 2, QTableWidgetItem(str(self.corrected_grades[row])))

    def show_about_window(self):
        self.about_window.show()

if __name__ == '__main__':
    app = QApplication()
    with open('style.qss', 'r') as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    app.exec()