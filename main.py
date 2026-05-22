import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class HelloWorldApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Hello World")
        self.setMinimumSize(300, 100)

        # Create a central widget and a layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a label with "Hello World"
        self.label = QLabel("Hello World", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Add some basic styling
        self.label.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        
        layout.addWidget(self.label)

def main():
    app = QApplication(sys.argv)
    window = HelloWorldApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
