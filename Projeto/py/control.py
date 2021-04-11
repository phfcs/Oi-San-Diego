from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView
from sandiego import Ui_MainWindow
from dijkstra import *
import sys



#Classes


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)


#Função


def search():
	_translate = QtCore.QCoreApplication.translate
	numbers = []
	graph = {}
	predecessor_isdigit = False
	count = -1

	data = open("data/db_amostra.txt", "r")

	in_search = main.ld_search.text()

	for line in data:
		graph.setdefault(int(line.split()[0]), {}).update({int(line.split()[1]) : abs(int(line.split()[1]) - int(line.split()[0]))})
	data.close()

	if in_search != "":
		for ch in in_search:
			if ch.isdigit() and predecessor_isdigit == False:
				numbers.append(ch)
				predecessor_isdigit = True
				count += 1
			elif ch.isdigit() and predecessor_isdigit == True:
				numbers[count] = numbers[count] + ch
			else:
				predecessor_isdigit = False

		for i in range(len(numbers)):
			numbers[i] = int(numbers[i])

		if len(numbers) == 2:
			distance, path = dijkstra(graph, numbers[0], numbers[1])

			if distance != -1 and path != -1:
				main.lb_result.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Resultados da Pesquisa</span></p><p align=\"center\">A <span style=\" font-weight:600;\">distância mais curta</span> entre <span style=\" font-weight:600;\">{numbers[0]}</span> e <span style=\" font-weight:600;\">{numbers[1]} interseção</span> é: <span style=\" font-weight:600;\">{distance} metros</span>.</p><p align=\"center\">O <span style=\" font-weight:600;\">caminho mais curto</span> entre <span style=\" font-weight:600;\">{numbers[0]}</span> e <span style=\" font-weight:600;\">{numbers[1]} interseção</span> é:</p><p align=\"center\"><span style=\" font-weight:600;\">{path}</span></p></body></html>"))
				main.fr_result.show()
			else:
				main.lb_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Resultados da Pesquisas</span></p><p align=\"center\">Desculpa, o caminho <span style=\" font-weight:600;\">é inalcançavel</span>. 😭 </p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
				main.fr_result.show()
		else:
			main.lb_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Resultados da Pesquisa</span></p><p align=\"center\">Por Favor, <span style=\" font-weight:600;\">insira</span> os <span style=\" font-weight:600;\">números de cruzamentos</span></p><p align=\"center\">que você deseja pesquisar!</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))			
			main.fr_result.show()

	else:
		main.lb_result.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Resultados da Pesquisa</span></p><p align=\"center\">Por Favor, <span style=\" font-weight:600;\">insira</span> sua pesquisa!</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>"))
		main.fr_result.show()

	main.btn_close.clicked.connect(lambda: main.fr_result.hide())


#App


if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)    
    main = MainWindow()
    main.fr_result.hide()
    main.btn_search.clicked.connect(lambda: search())
    main.show()
    sys.exit(app.exec_())