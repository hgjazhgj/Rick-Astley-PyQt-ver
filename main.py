import sys
import time
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QMenu, QFileDialog


from MainWindow import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.SCR_1.verticalScrollBar().setValue(
            self.SCR_1.verticalScrollBar().maximum())
        self.menu = QMenu(self)
        self.menu.addAction("Your")
        self.menu.addAction(QIcon("heart.png"), "hearts")
        self.menu.addAction("been")
        self.menu.addAction("aching")
        self.menu.addSeparator()
        submenu = QMenu("But", self)
        submenu.addAction("you're")
        submenu.addAction("too")
        submenu.addAction("shy")
        submenu.addAction("to")
        submenu.addAction("say")
        submenu.addAction("it")
        self.menu.addMenu(submenu)
        self.WID_1.customContextMenuRequested.connect(self.fx)
        self.qwqDlg = [QMessageBox(QMessageBox.Icon.NoIcon, "QwQ", "QwQ",
                                   QMessageBox.StandardButton.Ok, self) for _ in range(18)]
        for dlg in self.qwqDlg:
            dlg.setModal(False)

    def fx(self, x):
        self.menu.exec(self.mapToGlobal(
            QPoint(0, self.menubar.height()))+self.WID_1.pos()+x)

    def f1(self, x):
        self.CBB_1.setText(["no", "yes"][int(bool(x))])

    def f2(self):
        QMessageBox.information(
            self, "", "You wouldn't get get this from any other guy")

    def f3(self, x):
        self.TXT_1.setText(["understand", "confused"][x])

    def f4(self, x):
        self.LBL_2.setCursor(Qt.CursorShape.WaitCursor)

    def f5(self):
        self.BTN_1.setEnabled(False)
        self.BTN_2.setEnabled(True)

    def f6(self):
        self.BTN_1.setEnabled(True)
        self.BTN_2.setEnabled(False)

    def f7(self, x):
        self.LBL_1.setText(["never", "gonna", "make", "you", "cry"][x])

    def f8(self):
        QFileDialog.getOpenFileName(
            self, "Open File", "data/", "All Files (*.*);;Don't (*tell*);;me (*you're*);;too (*blind*);;to (*see*)")

    def f9(self):
        for _ in range(18):
            self.move(self.pos()+QPoint(0, -10))
            time.sleep(0.05)

    def f10(self):
        for _ in range(18):
            self.move(self.pos()+QPoint(0, 10))
            time.sleep(0.05)

    def f11(self):
        self.close()
        time.sleep(0.2)
        self.show()
        time.sleep(0.2)
        self.close()
        time.sleep(0.2)
        self.show()

    def f12(self, x):
        for i, dlg in enumerate(self.qwqDlg):
            dlg.move(self.mapToGlobal(
                QPoint(self.width()//2+i*20, self.height()//2+i*20)))
            dlg.show()
            time.sleep(0.05)

    def f13(self):
        for dlg in reversed(self.qwqDlg):
            dlg.close()
            time.sleep(0.05)

    def f14(self):
        self.LBL_3.setCursor(Qt.CursorShape.WaitCursor)


app = QApplication(sys.argv)
myWin = MyMainWindow()
myWin.show()
sys.exit(app.exec())
