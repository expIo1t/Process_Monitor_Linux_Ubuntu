# pip install psutil
import psutil
import time
import sys

# pip install qdarkstyle
import qdarkstyle

# pip install PyQt5
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem


class ProcessMonitor(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window properties:
        self.setWindowTitle("𝗣𝗥𝗢𝗖𝗘𝗦𝗦 𝗠𝗢𝗡𝗜𝗧𝗢𝗥")
        self.setGeometry(100, 100, 490, 400)

        # Create the main layout:
        main_layout = QVBoxLayout()

        # Add the table widget:
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(["PID", "%CPU", "%MEM", "COMMAND"])
        main_layout.addWidget(self.table_widget)

        # Add the button layout:
        button_layout = QHBoxLayout()

        # Apply the QDarkStyleSheet theme:
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # Add the refresh button:
        refresh_button = QPushButton("𝗥𝗘𝗙𝗥𝗘𝗦𝗛")
        refresh_button.clicked.connect(self.display_processes)
        button_layout.addWidget(refresh_button)

        # Add the end process button:
        self.end_button = QPushButton("𝗘𝗡𝗗 𝗣𝗥𝗢𝗖𝗘𝗦𝗦")
        self.end_button.clicked.connect(self.end_process)
        button_layout.addWidget(self.end_button)

        # Add the button layout to the main layout:
        main_layout.addLayout(button_layout)

        # Set the main layout:
        self.setLayout(main_layout)

        # Initialize the process information:
        self.processes = []

        # Display the initial process information:
        self.display_processes()

        # Show the window:
        self.show()

    def display_processes(self):
        # Clear the table widget:
        self.table_widget.setRowCount(0)

        # Fetch the process information:
        self.processes = psutil.process_iter()

        # Add the information for each process to the table widget:
        for process in self.processes:
            try:
                process_info = process.as_dict(attrs=["pid", "name", "cpu_percent", "memory_percent"])
                pid = process_info["pid"]
                cpu_percent = process_info["cpu_percent"]
                mem_percent = process_info["memory_percent"]
                name = process_info["name"]

                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)

                self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(pid)))
                self.table_widget.setItem(row_position, 1, QTableWidgetItem(f"{cpu_percent:.1f}"))
                self.table_widget.setItem(row_position, 2, QTableWidgetItem(f"{mem_percent:.1f}"))
                self.table_widget.setItem(row_position, 3, QTableWidgetItem(name))

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Ignore processes, that cannot be accessed:
                pass

    def end_process(self):
        # Get the selected row:
        selected_row = self.table_widget.currentRow()

        # Get the PID of the process:
        pid_item = self.table_widget.item(selected_row, 0)
        pid = int(pid_item.text())

        # Get the process object:
        process = psutil.Process(pid)

        # Terminate the process:
        process.terminate()

        # Wait for the process to terminate:
        while True:
            try:
                if process.status() == psutil.STATUS_DEAD:
                    break
            except psutil.NoSuchProcess:
                break
            time.sleep(0.1)
            
        # Remove the row from the table widget:
        self.table_widget.removeRow(selected_row)


if __name__ == "__main__":
    # Create the application object:
    app = QApplication(sys.argv)

    # Create the process monitor object:
    monitor = ProcessMonitor()

    # Execute the application:
    sys.exit(app.exec_())
