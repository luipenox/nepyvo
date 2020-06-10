from PyQt5 import QtWidgets, uic  # import for QMainWindow and loading designed UI
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('color_selector.ui', self)

        #  set a window title
        self.setWindowTitle('RGB Color Selector')

        #  show the window
        self.show()

        # connect the button to the function
        self.btn_show.clicked.connect(self.show_color)

        # set initial text to color line edit
        self.edit_red.setText('255')
        self.edit_green.setText('255')
        self.edit_blue.setText('255')

    # function to read values from line edit and show the color
    def show_color(self):
        red = self.edit_red.text()
        if not red:
            red = 0
        green = self.edit_green.text()
        if not green:
            green = 0
        blue = self.edit_blue.text()
        if not blue:
            blue = 0
        self.view_color.setStyleSheet(f"background-color: rgb({red}, {green}, {blue});")


# run application
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()
