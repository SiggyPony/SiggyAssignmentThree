from Charts.PieChart import *

class ChartCreator():
    chartTitle = None
    chartLabels = None
    chartValues = None
    sourceData = None
    tableName = None

    def setupChart(self, data):
        self.sourceData = data
        self.chartTitle = input("Input title for new chart>")
        if not self.getSourceTables():
            return False
        if not self.getLabelData():
            return False
        if not self.getValueData():
            return False
        return True

    def getSourceTables(self):
        self.tableName = input("Input source table name>")
        if not(self.tableName in self.sourceData.data.keys()):
            print("Table not found.")
            return False
        # Show columns
        listOfColumns = "Coloumns in " + self.tableName + ": "
        for col in range(0, len(self.sourceData.data[self.tableName][0])):
            listOfColumns = listOfColumns + \
                            (self.sourceData.data[self.tableName][col][0]) + " "
        print(listOfColumns)
        return True

    def getLabelData(self):
        chartLabels = input("Input column for labels>")
        chartLabelsData = None
        for col in range(0, len(self.sourceData.data[self.tableName][0])):
            if self.sourceData.data[self.tableName][col][0] == chartLabels:
                chartLabelsData = self.sourceData.data[self.tableName][col][:]
        if (chartLabelsData is None):
            print("Must give a valid column name.")
            return False
        del chartLabelsData[0]
        print(chartLabelsData)
        self.chartLabels = chartLabelsData
        return True

    def getValueData(self):
        chartValuesTemp = input("Input column for values>")
        for col in range(0, len(self.sourceData.data[self.tableName][0])):
            if self.sourceData.data[self.tableName][col][0] == chartValuesTemp:
                for item in range(1, len(self.sourceData.data[self.tableName]
                                         [col])):
                    if not(re.match('^[0-9]*$',
                                    self.sourceData.data[self.tableName][col]
                                    [item])):
                        print("False")
                        print("Column must only contain numbers")
                        return False
                chartValuesData = self.sourceData.data[self.tableName][col][:]
                del chartValuesData[0]
                print(chartValuesData)
                self.chartValues = chartValuesData
                return True
        print("Must give a valid column name.")
        return False

    def returnChart(self):
        pass


class  PieChartCreator(ChartCreator):
    def returnChart(self):
        tempReturnChart = PieChart((self.chartTitle, self.chartLabels, self.chartValues))
        return tempReturnChart




class BarChartCreator(ChartCreator):
    def returnChart(self):
        tempReturnChart = BarChart((self.chartTitle, self.chartLabels, self.chartValues))
        return tempReturnChart

