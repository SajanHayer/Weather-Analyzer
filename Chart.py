import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

class Chart:
    def DrawLineChart(self,xaxis,yaxis,title,xlabel,ylabel):
        fig = pyplot.figure()
        pyplot.title(title)
        pyplot.ylabel(ylabel)
        pyplot.xlabel(xlabel)

        pyplot.plot(xaxis, yaxis, marker ='o')
        pyplot.show()

    def DrawBarChart(self,xaxis,yaxis,title,xlabel,ylabel,y_pos,x_pos):
        
        plt.bar(y_pos, yaxis, align='center', alpha=0.5)
        plt.xticks(x_pos, xaxis)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        plt.title(title)

        plt.show()


#xaxis = ['June','July','August','September']
#yaxis = [1,2,3,4]
#y_pos = np.arange(len(yaxis)) #defines lenght of bar graph
#x_pos = [0,1,2,3]
#title = "Test run"
#xlabel = 'Months'
#ylabel = 'Numbers'
#f = Chart()
#f.DrawLineChart(xaxis,yaxis,title,xlabel,ylabel)
#f.DrawBarChart(xaxis,yaxis,title,xlabel,ylabel,y_pos,x_pos)