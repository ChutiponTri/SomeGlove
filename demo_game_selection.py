from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QMessageBox, QComboBox, QFrame
from PyQt6.QtGui import QFont, QIcon, QDoubleValidator
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from multiprocessing import Process
from datetime import datetime
import sys
from demo_Flappy import flappy
from demo_Jetpack import jetpack
from demo_Piano import piano
from demo_plotUI import MyPlot
from demo_database import Database
from demo_plot_analysis import Analysis
from demo_feedback_1_window import Feedback_1_Window
from demo_feedback_2_window import Feedback_2_Window
from demo_feedback_3_window import Feedback_3_Window
from demo_controller import Controller, Perform_GUI_Action

font = QFont("Cordia New", 16)

class GameSelection(QMainWindow):
    signal = pyqtSignal()
    pressure = []
    def __init__(self):
        super().__init__()
        self.setWindowTitle("หน้าต่างเกม")
        self.setWindowIcon(QIcon("icons/select.png"))

        # Create Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Get Username
        self.username = Database.get_current_user()

        # Start Connection
        self.start_connection()

        # Create Plot UI Button
        self.plot_button = QPushButton("Admin")
        self.plot_button.setStyleSheet(
            "QPushButton { border:none ; color:blue ; text-decoration:underline ; }"
            "QPushButton:hover { color : red ; }"
        )
        self.plot_button.setFont(QFont("Cordia New", 20))
        self.plot_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.plot_button.clicked.connect(self.plot_start)

        # Create Logout Button
        logout_button = QPushButton("Logout")
        logout_button.setStyleSheet(
            "QPushButton { border:none ; color:blue ; text-decoration:underline ; }"
            "QPushButton:hover { color : red ; }"
        )
        logout_button.setFont(QFont("Cordia New", 20))
        logout_button.setCursor(Qt.CursorShape.PointingHandCursor)
        logout_button.clicked.connect(self.close)

        # Create Separator
        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.VLine)
        frame.setFrameShadow(QFrame.Shadow.Sunken)

        # Create Labels
        header = QLabel("โปรดเลือกเกมที่ต้องการเล่น")
        user_label = QLabel("หมายเลข HN : %s" % self.username)
        flappy_label = QLabel("Flappy Bird")
        jetpack_label = QLabel("Jetpack Joyride")
        piano_label = QLabel("Piano Tiles")

        # Create Buttons
        flappy_button = QPushButton()
        jetpack_button = QPushButton()
        piano_button = QPushButton()

        # Flappy Button
        flappy_button.setIcon(QIcon("icons/flappy.png"))
        flappy_button.setIconSize(QSize(100, 100))
        flappy_button.setFixedSize(120, 120)
        flappy_button.clicked.connect(lambda : self.game_start(flappy, "FlappyBird"))
        flappy_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Jetpack Button
        jetpack_button.setIcon(QIcon("icons/jetpack.jpg"))
        jetpack_button.setIconSize(QSize(100, 100))
        jetpack_button.setFixedSize(120, 120)
        jetpack_button.clicked.connect(lambda : self.game_start(jetpack, "JetpackJoyride"))
        jetpack_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Piano Button
        piano_button.setIcon(QIcon("icons/piano.png"))
        piano_button.setIconSize(QSize(100, 100))
        piano_button.setFixedSize(120, 120)
        piano_button.clicked.connect(lambda : self.game_start(piano, "PianoTiles"))
        piano_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Feedback 1 Button
        feedback_1_button = QPushButton("ผลทดสอบความแข็งแรง")
        feedback_1_button.setFont(font)
        feedback_1_button.clicked.connect(lambda : self.evaluation_form(Feedback_1_Window))
        feedback_1_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Feedback 2 Button
        feedback_2_button = QPushButton("ผลทดสอบการประเมินทำงาน")
        feedback_2_button.setFont(font)
        feedback_2_button.clicked.connect(lambda : self.evaluation_form(Feedback_2_Window))
        feedback_2_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Feedback 3 Button
        feedback_3_button = QPushButton("แบบประเมินความพึงพอใจ")
        feedback_3_button.setFont(font)
        feedback_3_button.clicked.connect(lambda : self.evaluation_form(Feedback_3_Window))
        feedback_3_button.setCursor(Qt.CursorShape.PointingHandCursor)

        # Setting Font
        header.setFont(QFont("Cordia New", 24, QFont.Weight.Bold))
        user_label.setFont(QFont("Cordia New", 20, QFont.Weight.Bold))
        flappy_label.setFont(font)
        jetpack_label.setFont(font)
        piano_label.setFont(font)

        # Create Mode Selection Box
        self.mode_selection = QComboBox()
        self.mode_selection.addItems(["โหมดกำมือ", "โหมดแบมือ", "โหมดออโต้"])
        self.mode_selection.setFont(font)

        # Create Percentage Selection Box
        self.percentage_selection = QComboBox()
        self.percentage_selection.addItems([str(i) for i in range(0, 110, 10)])
        self.percentage_selection.setCurrentIndex(5)
        self.percentage_selection.setEditable(True)
        self.percentage_selection.setFont(font)
        self.percentage_selection.setValidator(QDoubleValidator())

        # Create Delay Selection Box
        self.delay_selection = QComboBox()
        self.delay_selection.addItems([str(i) for i in range(1000, 6000, 1000)])
        self.delay_selection.setCurrentIndex(1)
        self.delay_selection.setEditable(True)
        self.delay_selection.setFont(font)
        self.delay_selection.setValidator(QDoubleValidator())

        # Create Button Layout
        button = QGridLayout()
        button.setAlignment(Qt.AlignmentFlag.AlignRight)
        button.addWidget(user_label, 0, 0, 1, 4)
        button.addWidget(self.plot_button, 1, 0)
        button.addWidget(frame, 1, 1)
        button.addWidget(logout_button, 1, 2)

        # Create Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(header, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addStretch(1)
        # main_layout.addWidget(user_label, alignment=Qt.AlignmentFlag.AlignRight)
        main_layout.addLayout(button)
        main_layout.addStretch(1)

        # Create Game Button Layout
        grid_layout = QGridLayout()
        grid_layout.addWidget(flappy_button, 0, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(flappy_label, 1, 0, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(jetpack_button, 0, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(jetpack_label, 1, 1, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(piano_button, 0, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        grid_layout.addWidget(piano_label, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addLayout(grid_layout)
        main_layout.addStretch(2)

        # Create Selection Layout
        selection_layout = QHBoxLayout()
        selection_layout.addWidget(self.mode_selection)
        selection_layout.addWidget(self.percentage_selection)
        selection_layout.addWidget(self.delay_selection)
        main_layout.addLayout(selection_layout)

        # Create Evaluation Button Layout
        form_layout = QHBoxLayout()
        form_layout.addWidget(feedback_1_button)
        form_layout.addWidget(feedback_2_button)
        form_layout.addWidget(feedback_3_button)
        main_layout.addLayout(form_layout)
            
        # Setting Layout
        central_widget.setLayout(main_layout)

        self.setGeometry(400, 100, 800, 600)

        print("Game Selection Window is Ready")

    # Function to Start Connection
    def start_connection(self):
        self.connection = Controller(self.username, self.pressure)
        self.connection.start()

        self.perform = Perform_GUI_Action()
        self.perform.start()

    # Function To Start When Game Was Chosen
    def game_start(self, game_task, game_label):
        try:
            self.selection_check()
            self.connection.game = game_label
            self.perform.game = game_label
            self.connection.resume()
            self.perform.resume()
            
            self.clear_list()
            self.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task_A = Process(target=game_task)
            task_A.start()

            self.hide()
            task_A.join()
            
            self.show()
            self.stop_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.connection.stop()
            self.perform.stop()

            self.save(game_label)

            print("%s is Closed" % game_label)

        except Exception as e:
            message = QMessageBox()
            message.setWindowTitle("Wait")
            message.setText(f"Error {e}")
            message.setIcon(QMessageBox.Icon.Information)
            message.exec()

    # Function to Save Pressure Data
    def save(self, game_label):
        if len(self.pressure) > 0:
            data_to_save = {"Start Time": self.start_time, "Stop Time": self.stop_time, "Username": self.username, "Pressure": self.pressure, "Game":game_label}
            self.analysis = Analysis(data_to_save)
            self.analysis.save_status.connect(self.status)
            self.analysis.start()
        else:
            print("Data does not Exist")

    # Function to Display Save Status
    def status(self, status):
        message = QMessageBox()
        message.setWindowTitle("Save Status")
        if "Save" in status:
            message.setText("Save file %s Successfully!" % self.username)
            message.exec()
        elif "Permission" in status:
            message.setText("Please Close Excel File")
            message.exec()
        elif "Error" in status:
            message.setText(status)
            message.exec()

    # Function to Start Plot UI
    def plot_start(self):
        self.plot = MyPlot()
        self.plot.signal.connect(self.on_plot_close)
        self.hide()
        self.plot.show()

    # Function to Toggle When Plot UI was closed
    def on_plot_close(self):
        self.show()

    # Function to Check Mode Selection
    def selection_check(self):
        percent = int(self.percentage_selection.currentText())
        delay = int(self.delay_selection.currentText())
        mode = self.mode_selection.currentText()
        if mode == "โหมดกำมือ":
            mode = 'R'
        elif mode == "โหมดแบมือ":
            mode = 'G'
        elif mode == "โหมดออโต้":
            mode = 'A'
        
        self.connection.write_back(mode, percent, delay)

    # Function to Open Evaluation Forms
    def evaluation_form(self, form):
        self.form = form(self.username)
        self.form.signal.connect(self.show)
        self.form.show()
        self.hide()

    # Function to Clear the list
    def clear_list(self):
        self.pressure.clear()

    # Autocall Function To Toggle When Window Closed
    def closeEvent(self, event):
        Database.del_current_user(self.username)
        self.signal.emit()
        self.connection.disconnect()
        self.perform.disconnect()
        print("Game Selection Window is Closed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameSelection()
    window.show()
    sys.exit(app.exec())