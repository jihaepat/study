# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import uic


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("main_ui.ui")
        self.ui.show()
        self.init_obj()
        self.set_click_event()

    def init_obj(self):
        self.add_todo_btn = self.ui.__dict__['add_todo']
        self.all_label_view = self.ui.__dict__['all_label']
        self.text_edit_pannel = self.ui.__dict__['textEdit']
        self.out_todo_btn = self.ui.__dict__['out_todo']

    def set_click_event(self):
        self.add_todo_btn.clicked.connect(self.add_todo)
        self.out_todo_btn.clicked.connect(self.out_todo)

    def add_todo(self):
        all_label_view = self.all_label_view
        current_TODO = all_label_view.text()
        new_TODO = self.text_edit_pannel.toPlainText()
        all_label_view.setText('{}\n{}'.format(new_TODO, current_TODO))

    def out_todo(self):
        all_label_view = self.all_label_view
        with open('todo_list.txt', 'w') as f:
            f.write(all_label_view.text())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
