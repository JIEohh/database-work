#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dayu_widgets.qt import QWidget,QVBoxLayout,QHBoxLayout,QTreeWidget,QRect,QTreeWidgetItem,SIGNAL,SLOT
from dayu_widgets import dayu_theme
from dayu_widgets.tool_button import MToolButton
from dayu_widgets.field_mixin import MFieldMixin
from dayu_widgets import MLabel,MPushButton,MLineEdit



class MainWindow(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('test')
        self._init_ui()


    def _init_ui(self):
        self.resize(250, 350)
        self.button_login = MToolButton().svg('user_line.svg').text_beside_icon()
        self.button_login.setText('Login')
        self.button_login.clicked.connect(self.onclick)
        button_lay = QVBoxLayout()

        button_lay.addWidget(self.button_login)

        self.tree=QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.setHeaderHidden(1)
        self.tree.setGeometry(QRect(1,1,250,500))

        new_widget_1 = QTreeWidgetItem(self.tree)
        new_widget_1.setText(0,u'技能培训')

        new_widget_2 = QTreeWidgetItem(self.tree)
        new_widget_2.setText(0, u'企业培训')

        new_widget_3 = QTreeWidgetItem(self.tree)
        new_widget_3.setText(0, u'职业技能培训')

        new_widget_3_1 = QTreeWidgetItem(new_widget_3)
        new_widget_3_1.setText(0, u'餐饮厨艺')
        new_widget_3_2 = QTreeWidgetItem(new_widget_3)
        new_widget_3_2.setText(0, u'家庭服务')
        new_widget_3_3 = QTreeWidgetItem(new_widget_3)
        new_widget_3_3.setText(0, u'运输与物流')


        tree_layout = QVBoxLayout()
        tree_layout.addWidget(self.tree)

        main_lay = QVBoxLayout()
        main_lay.addLayout(button_lay)
        main_lay.addLayout(tree_layout)
        main_lay.addStretch()
        self.setLayout(main_lay)


    def testt(self):
        print 'aaaa'

    def onclick(self):
        self.login = Login()
        self.login.show()
        dayu_theme.apply(self.login)

class Login(QWidget):
    def __init__(self,parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle('Login')
        self.resize(250,150)
        main_layout = QVBoxLayout()
        name_layout = QHBoxLayout()
        password_layout = QHBoxLayout()
        name_layout.addWidget(MLabel('Name:'), 1, 0)
        name_layout.addWidget(MLineEdit())
        password_layout.addWidget(MLabel('Password:'), 1, 0)
        password_layout.addWidget(MLineEdit())
        main_layout.addLayout(name_layout)
        main_layout.addLayout(password_layout)
        query_button = MPushButton(text='Query').primary()
        main_layout.addWidget(query_button)
        self.setLayout(main_layout)


if __name__ == '__main__':
    import sys
    from dayu_widgets.qt import QApplication
    app = QApplication(sys.argv)
    test = MainWindow()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())