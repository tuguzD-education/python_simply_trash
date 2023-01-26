import sys
from PyQt5.QtWidgets import QApplication, QWidget


app = QApplication(sys.argv)

window = QWidget()
window.resize(320, 240)

window.setWindowTitle('Hello World!')
window.show()

sys.exit(app.exec_())
