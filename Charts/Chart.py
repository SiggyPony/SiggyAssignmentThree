import matplotlib.pyplot as plt
import numpy as np
import re

class Chart:
    chartTitle = None
    chartLabels = None
    chartValues = None

    def __init__(self):
        pass

    def drawChart(self):
        pass

class PieChart(Chart):
    def __init__(self, chartData):
        self.chartTitle = chartData[0]
        self.chartLabels = chartData[1]
        self.chartValues = chartData[2]

    def drawChart(self):
        plt.pie(self.chartValues, None, self.chartLabels, None,
                autopct='%1.1f%%', pctdistance=0.90,
                shadow=True, startangle=90)
        plt.figtext(0.5, 0.965, self.chartTitle, ha='center',
                    color='black', weight='bold', size='large')
        plt.axis('equal')
        plt.show()


class BarChart(Chart):
    def __init__(self, chartData):
        self.chartTitle = chartData[0]
        self.chartLabels = chartData[1]
        self.chartValues = chartData[2]

    def drawChart(self):
        x = np.arange(len(self.chartValues))
        y = [int(i) for i in self.chartValues]
        width = 1/1.5
        plt.bar(x, y, width, color="green")
        plt.xticks(x + (width/2), self.chartLabels)
        plt.figtext(0.5, 0.965, self.chartTitle, ha='center',
                    color='black', weight='bold', size='large')
        plt.show()
