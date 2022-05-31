import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from PyQt5.QtGui import QPixmap
from matplotlib import pyplot as plt

from VectorMatrixClass import Vector, Matrix 
from PobudzeniaClass import Pobudzenia 

class SymScreen(QDialog):

    def __init__(self):
        super(SymScreen,self).__init__()
        loadUi("ui//SymulacjaForm.ui",self)
        qpixmap = QPixmap('img//schemat.png')
        self.imglabel.setPixmap(qpixmap)
        self.OdpowiedzButton.clicked.connect(self.stabilitycheck)

    def timegroup_selected(self):

        items_time = self.timeBox.findChildren(QtWidgets.QRadioButton)
        for item in items_time:
            if item.isChecked(): return item.text()

    def ampgroup_selected(self):
        items_amp = self.ampBox.findChildren(QtWidgets.QRadioButton)
        for item in items_amp:
            if item.isChecked(): return item.text()
    
    def ugroup_selected(self):
        items_u = self.pobudzenieBox.findChildren(QtWidgets.QRadioButton)
        for item in items_u:
            if item.isChecked(): return item.text()

    def fgroup_selected(self):
        items_freq = self.freqBox.findChildren(QtWidgets.QRadioButton)
        for item in items_freq:
            if item.isChecked(): return item.text()

    def stabilitycheck(self):
        
        time = int(self.timegroup_selected())
        amp = int(self.ampgroup_selected())
        freq = float(self.fgroup_selected())
        pobudzenie = str(self.ugroup_selected())
        
        try:
            k = float(self.kfield.text())
            a = float(self.afield.text())
            A = float(self.Afield.text())
            m = float(self.mfield.text())

            if a > 0 and k * A * m > 0:
                self.stabilnyLabel.setText("")
                self.integration(k, a, A, m, pobudzenie, time, amp, freq)

            else:
                self.stabilnyLabel.setText("Układ nie jest stabilny")

        except:
            self.stabilnyLabel.setText("Wpisz wartości")


    def integration(self, k, a, A, m, pobudzenie, time, amp, freq):    # funkcja wykonujaca calkowanie
        
        jakiepobudzenie = Pobudzenia(time, amp, freq)

        if pobudzenie == 'Skok': u = jakiepobudzenie.pobudzenie_skok()
        if pobudzenie == 'Sinus': u = jakiepobudzenie.pobudzenie_sin()
        if pobudzenie == 'Prostokat': u = jakiepobudzenie.pobudzenie_prostokat()

        sim_steps = jakiepobudzenie.sim_steps
        h = jakiepobudzenie.h
        a1 = a
        a0 = k*A*m
        b0 = k*A

        # model stanowy
        state_A = Matrix(0, 1, -a0, -a1)
        state_B = Vector(0, 1)
        state_C = Vector(b0, 0)

        # zerowe warunki poczatkowe
        xi_1 = Vector(0, 0)

        Ax = Vector(0, 0)
        Bu = Vector(0, 0)
        xi = Vector(0, 0)
        Cx = 0
        y = []

        # glowna petla obliczen - TU COS SIE JEBLO
        for i in range(0, sim_steps):
            Ax = state_A * xi_1
            Bu = state_B * u[i]
            Cx = state_C * xi_1
            y.append(Cx)
            xi = Ax + Bu
            xi = xi * h
            xi = xi_1 + xi
            xi_1 = xi

        time_values = []
        for i in range(0, sim_steps):
            time_values.append(i * h)  # argumenty osi odcietych dla wykresu (czas)

        self.draw_plot(time_values, y)

    def draw_plot(self, dev_x, dev_y):

        plt.xlabel("t")
        plt.ylabel("y(t)")
        plt.title("Odpowiedz ukladu")
        plt.plot(dev_x, dev_y)
        plt.show()


if __name__ == '__main__':            

    app = QApplication(sys.argv)
    sym = SymScreen()
    widget = QStackedWidget()
    widget.addWidget(sym)
    widget.setWindowTitle("MMM")
    widget.setWindowIcon(QtGui.QIcon("img//manager.png"))
    widget.setFixedHeight(631)
    widget.setFixedWidth(761)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
    
    