from PySide2.QtWidgets import QApplication, QWidget, QErrorMessage
from ui.decrypt import Ui_DecryptWin
import sys
import autorun
import pystray
import PIL.Image


class MainWin(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_DecryptWin()
        self.ui.setupUi(self)
        self.error = QErrorMessage(self)
        self.ui.decryptButton.clicked.connect(self.decrypt)

    def ms_error(self, title, message, type_error):
        self.error.setWindowTitle(title)
        self.error.showMessage(message, type_error)

    def get_data(self):
        text = self.ui.lineInput.text()

        if self.ui.radioENG.isChecked():
            return text, 'eng'
        if self.ui.radioRUS.isChecked():
            return text, 'rus'

    def decrypt(self):
        try:
            self.ui.textOut.clear()
            text, key = self.get_data()
            out_text = ''

            RUS_lower = ('й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ',
                         'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', "э",
                         'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'ё')
            RUS_upper = ('Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ',
                         'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д', 'Ж', "Э",
                         'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', 'Ё')

            ENG_lower = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']',
                         'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'",
                         'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '`')
            ENG_upper = ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}',
                         'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"',
                         'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '~')

            if key == 'rus':
                for elem in text:
                    if elem in ENG_upper:
                        out_text += RUS_upper[ENG_upper.index(elem)]
                    elif elem in ENG_lower:
                        out_text += RUS_lower[ENG_lower.index(elem)]
                    else:
                        out_text += elem

            if key == 'eng':
                for elem in text:
                    if elem in RUS_upper:
                        out_text += ENG_upper[RUS_upper.index(elem)]
                    elif elem in RUS_lower:
                        out_text += ENG_lower[RUS_lower.index(elem)]
                    else:
                        out_text += elem

            self.ui.textOut.setText(out_text)
        except TypeError:
            self.ms_error('TypeError', 'Ключ не был распознан!', 'TypeError')


def start_program():
    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()
    win = MainWin()
    win.show()
    autorun.add_to_startup()
    app.exec_()


def on_clicked(icon, item):
    if str(item) == 'Открыть':
        start_program()
    if str(item) == 'Выход':
        icon.stop()


if __name__ == '__main__':
    image = PIL.Image.open('icon/qwerty.png')

    icon = pystray.Icon('Qwerty decryption', image, menu=pystray.Menu(
        pystray.MenuItem('Открыть', on_clicked),
        pystray.MenuItem('Выход', on_clicked)
    ))

    icon.run()
