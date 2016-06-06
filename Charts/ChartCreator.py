from Charts.Chart import *

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
        if not self.getExtraInfo():
            return False

        return True

    def getSourceTables(self):
        raise NotImplementedError

    def getLabelData(self):
        raise NotImplementedError

    def getValueData(self):
        raise NotImplementedError

    def returnChart(self):
        raise NotImplementedError

    def getExtraInfo(self):
        raise NotImplementedError



class  PieChartCreator(ChartCreator):
    def getSourceTables(self):
        self.tableName = input("Input source table name for PieChart data>")
        if not(self.tableName in self.sourceData.data.keys()):
            print("Table not found.")
            return False
        self.sourceData.printData(self.tableName)
        return True

    def getLabelData(self):
        chartLabels = input("Input data column to be used for labels>")
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
        chartValuesTemp = input("Input data column to be used for values>")
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

    def getExtraInfo(self):
        return True

    def returnChart(self):
        tempReturnChart = PieChart((self.chartTitle, self.chartLabels, self.chartValues))
        return tempReturnChart




class BarChartCreator(ChartCreator):
    def getSourceTables(self):
        self.tableName = input("Input source table name for BarChart data>")
        if not(self.tableName in self.sourceData.data.keys()):
            print("Table not found.")
            return False
        self.sourceData.printData(self.tableName)
        return True

    def getLabelData(self):
        chartLabels = input("Input data column to be used for labels>")
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
        chartValuesTemp = input("Input data column to be used for values>")
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

    def getExtraInfo(self):
        return True

    def returnChart(self):
        tempReturnChart = BarChart((self.chartTitle, self.chartLabels, self.chartValues))
        return tempReturnChart

