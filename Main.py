import cmd
import argparse

from BadSmellThree.BadSmellThreeRefactored.Data import Data
from BadSmellThree.BadSmellThreeRefactored.Charts.PieChart import PieChart


class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.intro = 'Welcome to Siggy\'s Data Presentation Program - SDPP \n'
        self.prompt = '>'
        self.data = Data()

    def do_load_data(self, importString):
        """
Load data from the specified file and location: load_data ./data/data4.csv
Will ask for name of new table.
        """
        if not self.checkSingleParam(importString):
            return
        print('load_data')
        tableName = input("Input table name>")
        l = tableName.split()
        if len(l) != 1:
            print("Table name can't be blank and must not contain spaces.")
            return
        self.data.importData(importString, tableName)

    def do_save_project(self, saveString):
        """
Save project to the specified file and location: save_project myproject.dat
        """
        if not self.checkSingleParam(saveString):
            return
        print('save_project')
        self.data.saveProject(saveString)

    def do_load_project(self, loadString):
        """
Load project from the specified file and location: load_project myproject.dat
        """
        if not self.checkSingleParam(loadString):
            return
        print('load_project')
        self.data.loadProject(loadString)

    def do_show(self, line):
        """
Show the current loaded data tables: show
        """
        print('show')
        self.data.printData()

    def do_make_piechart(self, line):
        """
Will create Pie Chart.
        """
        pieChart = PieChart(self.data)
        if (pieChart.setupChart()):
            pieChart.drawChart()

    def do_exit(self, line):
        'Exit the program'
        return True

    def checkSingleParam(self, string):
        l = string.split()
        if len(l) != 1:
            print("Invalid number of arguments")
            return False
        return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--new', help='Start a new project',
                        action='store_true')
    parser.add_argument('-l', '--load', help='Load a saved project' +
                                             ' from LOAD')
    args = parser.parse_args()
    if args.new:
        cmd_temp = Controller()
        cmd_temp.cmdloop()
        return
    if args.load is not None:
        cmd_temp = Controller()
        cmd_temp.do_load_project(args.load)
        cmd_temp.cmdloop()
        return
    parser.print_help()


if __name__ == '__main__':
    main()
