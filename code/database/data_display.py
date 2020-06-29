from PyQt5.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QTableView,QApplication
import sys

# Most code from: https://stackoverflow.com/questions/20993084/how-to-display-data-from-database-in-table-view-in-python

app = QApplication(sys.argv)

db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("proto-base.db")
db.open()

projectModel = QSqlQueryModel()
projectModel.setQuery("select * from test",db)

projectView = QTableView()
projectView.setModel(projectModel)

projectView.show()
app.exec_()