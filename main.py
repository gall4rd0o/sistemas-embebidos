import sys
import receiver
import PyQt5.QtWidgets as pw
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import pyqtSlot
import pyqtgraph as pg

class MainWindow(pw.QMainWindow):
    def __init__(self):
        super().__init__()
        #Setting initial window parameters
        self.title = 'Visualizador información de BME'
        self.left = 50
        self.top = 50
        self.width = 320
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Input line that takes a value for window size
        windowLine = pw.QLineEdit('0', self)
        windowLine.setValidator(QIntValidator())

        # Button that sets window size
        windowBtn = pw.QPushButton('Cambiar ventana de datos', self)
        windowBtn.clicked.connect(lambda: self.update_window_size(int(windowLine.text())))

        # Current Window size
        self.windowLabel = pw.QLabel()
        self.windowLabel.setText('Tamaño de ventana de datos es ' + str(DATA_WINDOW_SIZE))

        # Button that requests the data
        requestBtn = pw.QPushButton('Solicitar datos', self)
        requestBtn.clicked.connect(self.request)

        # Button that closes connection
        closeBtn = pw.QPushButton('Cerrar conexión', self)
        closeBtn.clicked.connect(self.end)

        # Graphs
        plotGraph = pg.PlotWidget()
        plotGraph.plot(TEMP, PRESS)

        # Metrics
        self.tempRMS = pw.QLabel()
        self.tempRMS.setText('RMS de temperatura ' + str(TEMP_RMS))
        self.pressRMS = pw.QLabel()
        self.pressRMS.setText('RMS de presión ' + str(PRESS_RMS))

        # Create layouts
        mainLayout = pw.QVBoxLayout()
        btnLayout = pw.QGridLayout()
        graphLayout = pw.QGridLayout()


        # Add widgets
        btnLayout.addWidget(windowLine, 0, 0)
        btnLayout.addWidget(windowBtn, 0, 1)
        btnLayout.addWidget(self.windowLabel, 1, 0, 2, 0)
        btnLayout.addWidget(requestBtn, 2, 0, 2, 0)
        btnLayout.addWidget(closeBtn, 3, 0, 2, 0)
        graphLayout.addWidget(plotGraph, 0, 0)
        graphLayout.addWidget(self.tempRMS, 1, 0, 2, 0)
        graphLayout.addWidget(self.pressRMS, 1, 1)

        mainLayout.addLayout(btnLayout)
        mainLayout.addLayout(graphLayout)        

        #Set layout
        widget = pw.QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)
    
    @pyqtSlot()
    def request(self):
        #data_list = receiver.recieve_window_data(DATA_WINDOW_SIZE)
        #print(data_list)
        # Añadir los datos a TEMP, PRESS, TEMP_RMS y PRESS_RMS
        print("Request")
    
    @pyqtSlot()
    def end(self):
        #receiver.restart_ESP()
        print("Close")
        self.close()
    
    @pyqtSlot()
    def update_window_size(self, window):
        #if receiver.set_window_size(window):
            #DATA_WINDOW_SIZE = window
        self.windowLabel.setText('Tamaño de ventana de datos es ' + str(DATA_WINDOW_SIZE))
        print("Update")

DATA_WINDOW_SIZE = 10
PRESS = [0]
PRESS_RMS = 0
TEMP = [0]
TEMP_RMS = 0

if __name__ == '__main__':
    app = pw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
