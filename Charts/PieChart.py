import matplotlib.pyplot as plt
import re


class PieChart:
    chartTitle = None
    chartLabels = None
    chartValues = None
    sourceData = None

    def __init__(self, data):
        self.sourceData = data

    def setupChart(self):
        """
    Will ask for,
    Table title (for chart output)
    Source table (to take data from)
    Labels column (column in table to use as labels in Pie Chart)
    Data column (column in table to use as data for Pie Chart)
        must be numeric
        """
        self.tableTitle = input("Input title for new table>")
        tableName = input("Input source table name>")
        if not(tableName in self.sourceData.data.keys()):
            print("Table not found.")
            return False
        # Show columns
        listOfColumns = "Coloumns in " + tableName + ": "
        for col in range(0, len(self.sourceData.data[tableName][0])):
            listOfColumns = listOfColumns + \
                            (self.sourceData.data[tableName][col][0]) + " "
        print(listOfColumns)
        if not self.getLabelData(tableName):
            return False
        if not self.getValueData(tableName):
            return False
        return True

    def getLabelData(self, tableName):
        chartLabels = input("Input column for labels>")
        chartLabelsData = None
        for col in range(0, len(self.sourceData.data[tableName][0])):
            if self.sourceData.data[tableName][col][0] == chartLabels:
                chartLabelsData = self.sourceData.data[tableName][col][:]
        if (chartLabelsData is None):
            print("Must give a valid column name.")
            return False
        del chartLabelsData[0]
        print(chartLabelsData)
        self.chartLabels = chartLabelsData
        return True

    def getValueData(self, tableName):
        chartValuesTemp = input("Input column for values>")
        for col in range(0, len(self.sourceData.data[tableName][0])):
            if self.sourceData.data[tableName][col][0] == chartValuesTemp:
                for item in range(1, len(self.sourceData.data[tableName]
                                         [col])):
                    if not(re.match('^[0-9]*$',
                                    self.sourceData.data[tableName][col]
                                    [item])):
                        print("False")
                        print("Column must only contain numbers")
                        return False
                chartValuesData = self.sourceData.data[tableName][col][:]
                del chartValuesData[0]
                print(chartValuesData)
                self.chartValues = chartValuesData
                return True
        print("Must give a valid column name.")
        return False

    def drawChart(self):
        plt.pie(self.chartValues, None, self.chartLabels, None,
                autopct='%1.1f%%', pctdistance=0.90,
                shadow=True, startangle=90)
        plt.figtext(0.5, 0.965, self.chartTitle, ha='center',
                    color='black', weight='bold', size='large')
        plt.axis('equal')
        plt.show()
