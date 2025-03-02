import sys
import time
import psutil
from functools import partial
from threading import Thread, Event
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QCheckBox, QLabel, QPushButton, 
    QLineEdit, QMessageBox
)
from PyQt5.QtGui import QIcon

def get_stylesheet():
    font_size = 14
    return f"""
            QWidget {{
                background-color: #1e1e1e;
                color: #fff;
                font-family: Arial, sans-serif;
            }}
            QPushButton, QCheckBox, QLineEdit {{
                background-color: #2e2e2e;
                color: white;
                border-radius: 5px;
                font-size: {font_size}px;
                padding: 10px;
            }}
            QLabel {{
                color: #fff;
                font-size: {font_size}px;
            }}
        """

def process_name_checker(proc, names: list):
    """Checks if a process name matches any in the provided list."""
    if isinstance(names, str):
        names = [names]
    try:
        return any(name.lower() in (proc.info['name'] or "").lower() for name in names)
    except KeyError:
        return False

def kill_processes(names: list):
    """Kills all processes that match the names in the provided list."""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if process_name_checker(proc, names):
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

class AppSwitch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App Switch")
        self.setGeometry(100, 100, 350, 200)
        self.setWindowIcon(QIcon("on-off.png"))

        # Dictionary to track which applications should be killed
        self.killList = {
            "steam": False, 
            "discord": False, 
            "epic": False,
            "meta": False,
            "overwolf": False,
        }
        
        self.layout = QVBoxLayout()

        # Input field for custom applications
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter app name (e.g., chrome)")
        self.layout.addWidget(self.input_field)

        # Button to add user-defined apps
        self.add_button = QPushButton("Add App", self)
        self.add_button.clicked.connect(self.add_custom_app)
        self.layout.addWidget(self.add_button)

        # Add existing checkboxes
        for key in self.killList.keys():
            self.add_checkbox(key)

        self.setLayout(self.layout)
        self.setStyleSheet(get_stylesheet())

        self.stop_event = Event()
        
        # Background thread to continuously monitor and kill selected apps
        self.kill_thread = Thread(target=self.kill_loop, daemon=True)
        self.kill_thread.start()

    def add_checkbox(self, app_name):
        """Adds a new checkbox for an app to the UI."""
        checkbox = QCheckBox(f"{app_name.capitalize()} Kill Switch")
        checkbox.setTristate(False)  # Ensures only two states (checked/unchecked)
        checkbox.stateChanged.connect(partial(self.toggle, app_name))
        self.layout.addWidget(checkbox)

    def add_custom_app(self):
        """Adds a user-defined application to the kill list."""
        app_name = self.input_field.text().strip().lower()
        if not app_name:
            return
        if app_name in self.killList:
            QMessageBox.warning(self, "Duplicate", f"{app_name.capitalize()} is already in the list!")
            return
        self.killList[app_name] = False
        self.add_checkbox(app_name)
        self.input_field.clear()

    def closeEvent(self, event):
        """Ensures the background thread is stopped before closing the app."""
        self.stop_event.set()
        self.kill_thread.join()
        event.accept()

    def kill_loop(self):
        """Continuously checks and kills selected applications."""
        while not self.stop_event.is_set():
            to_kill = [app for app, active in self.killList.items() if active]
            if to_kill:
                kill_processes(to_kill)  # Kill all at once instead of multiple function calls
            time.sleep(0.2)  # Reduce CPU usage while maintaining effectiveness

    def toggle(self, var, state):
        """Updates the kill list based on the checkbox state."""
        self.killList[var] = state == 2  # Only toggle when fully checked

app = QApplication(sys.argv)
window = AppSwitch()
window.show()
sys.exit(app.exec_())
