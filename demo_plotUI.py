from PyQt6.QtWidgets import QApplication, QMessageBox, QPushButton, QVBoxLayout, QTabWidget, QFileDialog, QComboBox, QHBoxLayout, QLabel, QMainWindow
from PyQt6.QtGui import QFont, QPainter, QPixmap, QColor, QBrush
from PyQt6.QtCore import Qt, pyqtSignal
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from threading import Thread
import pandas as pd
import numpy as np
import sys
import os
from demo_database import Database

font = QFont("Cordia New", 16)

class MyPlot(QMainWindow):
    signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Smart Glove")
        self.setGeometry(100, 100, 1200, 900)

        central_widget = QTabWidget()
        self.setCentralWidget(central_widget)

        self.username = Database.get_current_user()
        self.current_mode = "Line"
        
        # Create Main Layout
        main_layout = QVBoxLayout()

        # Create two figures for bar and line plots
        self.figure_bar = Figure(figsize=(8, 12), dpi=80)
        self.canvas_bar = FigureCanvas(self.figure_bar)
        self.navigator = NavigationToolbar(self.canvas_bar)
        main_layout.addWidget(self.navigator)
        main_layout.addWidget(self.canvas_bar)

        # Axes for bar and line plots
        self.ax_bar = self.figure_bar.add_subplot(111)
        self.ax_bar.set_xlabel("Time (s)", fontsize=12)
        self.ax_bar.set_ylabel("Pressure (kPa)", fontsize=12)
        self.ax_bar.set_title("Real-Time Pressure Data (Bar)", fontsize=18)

        self.y_data = {}  # Will store averaged sensor values

        # Button layout
        button_layout = QHBoxLayout()

        # Create Mode Selection
        self.mode_source_combo = QComboBox()
        self.mode_source_combo.addItems(["Line", "Bar"])
        self.mode_source_combo.setFont(font)
        self.mode_source_combo.currentIndexChanged.connect(self.change_mode_source)
        button_layout.addWidget(self.mode_source_combo)

        # Data source combo box
        self.data_source_combo = QComboBox()
        self.data_source_combo.addItems(["(Please Select Data)"])
        self.data_source_combo.setFont(font)
        self.data_source_combo.currentIndexChanged.connect(self.change_data_source)
        button_layout.addWidget(self.data_source_combo)
        update_combo = Thread(target=self.get_sheet_name)
        update_combo.start()

        self.reset_button = QPushButton("Reset")
        self.reset_button.setFont(font)
        self.reset_button.clicked.connect(self.reset_clicked)
        button_layout.addWidget(self.reset_button)

        self.save_button = QPushButton("Save PNG")
        self.save_button.setFont(font)
        self.save_button.clicked.connect(self.save_clicked)
        button_layout.addWidget(self.save_button)

        # Add the new CSV save button
        self.csv_save_button = QPushButton("Save Excel")
        self.csv_save_button.setFont(font)
        self.csv_save_button.clicked.connect(self.save_csv_clicked)
        button_layout.addWidget(self.csv_save_button)

        # Add the Overview Button
        self.overview_button = QPushButton("Save Overview")
        self.overview_button.setFont(font)
        self.overview_button.clicked.connect(self.save_overview)
        button_layout.addWidget(self.overview_button)

        # Add the Game Button
        self.game_button = QPushButton("Save Game Score")
        self.game_button.setFont(font)
        self.game_button.clicked.connect(self.save_game)
        button_layout.addWidget(self.game_button)

        main_layout.addLayout(button_layout)

        # Statistics labels
        self.mean_label = QLabel("Mean: N/A")
        self.max_label = QLabel("Max: N/A")
        self.min_label = QLabel("Min: N/A")
        self.current_value_label = QLabel("Current Value: N/A")

        self.mean_label.setFont(font)
        self.max_label.setFont(font)
        self.min_label.setFont(font)
        self.current_value_label.setFont(font)

        stats_layout = QHBoxLayout()
        stats_layout.addWidget(self.mean_label)
        stats_layout.addWidget(self.max_label)
        stats_layout.addWidget(self.min_label)
        stats_layout.addWidget(self.current_value_label)

        main_layout.addLayout(stats_layout)

        central_widget.setLayout(main_layout)
        self.showMaximized()

    def get_sheet_name(self):
        self.fetched = Database.get_start_index(self.username)
        self.sheet_name = list(self.fetched.keys())
        self.sheet_name.sort()
        self.data_source_combo.addItems(self.sheet_name)

    def reset_clicked(self):
        self.y_data.clear()
        self.ax_bar.clear()
        self.ax_bar.set_xlabel("Time (s)", fontsize=12)
        self.ax_bar.set_ylabel("Pressure (kPa)", fontsize=12)
        self.ax_bar.set_title("Real-Time Pressure Data (Bar)", fontsize=18)
        self.canvas_bar.draw()
        self.update_statistics()

    def save_clicked(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "PNG Files (*.png);;All Files (*)")
        if file_name:
            self.figure_bar.savefig(f"{file_name}_{self.current_mode}.png")

    def update_plot(self):
        if len(self.y_data["pressure"]) > 0:
            self.ax_bar.clear()
            if self.current_mode == "Bar":
                self.ax_bar.bar(range(len(self.y_data["pressure"])), self.y_data["pressure"], color="blue")

            elif self.current_mode == "Line":
                self.ax_bar.plot(range(len(self.y_data["pressure"])), self.y_data["pressure"], color="red")
                
            ticks = np.arange(0, len(self.y_data) + 1, 10)
            labels = [(i // 10) for i in ticks]
            self.ax_bar.set_xlabel("Time (s)", fontsize=12)
            self.ax_bar.set_ylabel("Pressure (kPa)", fontsize=12)
            self.ax_bar.set_title("Real-Time Pressure Data (Line)", fontsize=18)

            self.ax_bar.set_xticks(ticks, labels)

            self.ax_bar.set_xlim(min(range(len(self.y_data["pressure"]))), max(range(len(self.y_data["pressure"]))))

            self.canvas_bar.draw()

            # Update live data statistics
            self.update_statistics()

    def change_mode_source(self):
        self.current_mode = self.mode_source_combo.currentText()
        self.update_plot()

    def change_data_source(self):
        current_data = self.data_source_combo.currentText()
        self.y_data = Database.get_pressure(self.username, current_data, self.fetched[current_data])
        print(self.y_data)
        self.update_plot()

    def update_statistics(self):
        if len(self.y_data["pressure"]) > 0:
            smoothed_mean = np.mean(self.y_data["pressure"])
            smoothed_max = max(self.y_data["pressure"])
            smoothed_min = min(self.y_data["pressure"])
            self.mean_label.setText(f"Mean: {smoothed_mean:.2f}")
            self.max_label.setText(f"Max: {smoothed_max:.2f}")
            self.min_label.setText(f"Min: {smoothed_min:.2f}")
            data = self.y_data["pressure"][-1]
            self.current_value_label.setText(f"Last Value: {data:.2f}")

    def save_csv_clicked(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx);;All Files (*)")
        if file_name:
            try:
                if not file_name.lower().endswith(".xlsx"):
                    file_name += ".xlsx"
                df = pd.DataFrame({
                    "Timestamp": self.y_data["timestamp"],
                    "Pressure":  pd.to_numeric(self.y_data["pressure"], errors="coerce")
                })
                df.to_excel(file_name, index=False)
            except PermissionError:
                message = QMessageBox()
                message.setWindowTitle("Warning")
                message.setText("Please Close Excel Before Saving")
                message.setIcon(QMessageBox.Icon.Warning)
                message.exec()

    def save_overview(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx);;All Files (*)")
        if file_name:
            try:
                if not file_name.lower().endswith(".xlsx"):
                    file_name += ".xlsx"
                overview = Database.get_overview(self.username)
                df = pd.DataFrame(overview)
                df.to_excel(file_name, index=False)
            except PermissionError:
                message = QMessageBox()
                message.setWindowTitle("Warning")
                message.setText("Please Close Excel Before Saving")
                message.setIcon(QMessageBox.Icon.Warning)
                message.exec()

    def save_game(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx);;All Files (*)")
        if file_name:
            try:
                if not file_name.lower().endswith(".xlsx"):
                    file_name += ".xlsx"
                game = Database.get_game(self.username)
                df = pd.DataFrame(game)
                df.to_excel(file_name, index=False)
            except PermissionError:
                message = QMessageBox()
                message.setWindowTitle("Warning")
                message.setText("Please Close Excel Before Saving")
                message.setIcon(QMessageBox.Icon.Warning)
                message.exec()

    def closeEvent(self, event):
        self.signal.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyPlot()
    window.show()
    sys.exit(app.exec())
