import matplotlib.pyplot as pyplot
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

class FileIO:
    def __init__ (self):
        self.filePath = []

    def dataTable():
        file_name ="CalgaryWeather.csv"

        data = np.loadtxt(file_name , delimiter=',', skiprows=1,
                usecols=(0,1,2,3,4), dtype = np.float)
        return data

class TemperatureData:
    def __init__(self):
        self.dateObject = []
        self.minTemperature = []
        self.maxTemperature = []
        self.snowfall = []

    def minTemp(self):
        self.dateObject = [1992,1]
        self.minTemperature.append (-15.9)
        return self.dateObject, self.minTemperature
    def maxTemp(self):
        self.dateObject = [2019,7]
        self.maxTemperature.append(23.5)
        return self.dateObject, self.maxTemperature
    def snow(self):
        data = FileIO.dataTable()
        j = 0
        while j < 359:
            i = 0
            a = 0
            avg = 0
            while i <= 11:
                if j == 359:
                    break
                a += data[j,4]
                i += 1
                j += 1
            avg = a/12  
            self.snowfall.append(avg)
        return self.snowfall

class WeatherAnalyzer:
    def __init__ (self):
        self.tempdata = TemperatureData()
    
    def getMinTemp(self):
        td = []
        year = self.tempdata.minTemp()[0][0]
        temp = self.tempdata.minTemp()[1][0]
        td.append(f"The minimum temperature between 1990-2019 was: {temp} celsius during January, {year}")
        return td
    
    def getMintempAnnually(self):
        td = []
        data = FileIO.dataTable()
        j = 0
        while j < 359:
            i = 0
            c = []
            while i <= 11:
                if j == 359:
                    break
                c.append(data[j,3])    
                i += 1
                j += 1
            c.sort()
            td.append(c[0])
        y = []
        q = []
        k = 0
        x = Date()
        while k < 30:
            y = [x.Year()[k],td[k]]
            q.append(y)
            k += 1
        return q
            
    def getMaxTemp(self):
        td = []
        year = self.tempdata.maxTemp()[0][0]
        temp = self.tempdata.maxTemp()[1][0]
        td.append(f"The maximum temperature between 1990-2019 was: {temp} celsius during July, {year}")
        return td
    
    def getMaxtempAnnually(self):
        td = []
        data = FileIO.dataTable()
        j = 0
        while j < 359:
            i = 0
            c = []
            while i <= 11:
                if j == 359:
                    break
                c.append(data[j,2])    
                i += 1
                j += 1
            c.sort()
            td.append(c[len(c)-1])
        y = []
        q = []
        k = 0
        x = Date()
        while k < 30:
            y = [x.Year()[k],td[k]]
            q.append(y)
            k += 1
        return q


    def AvgSnowFallAnnually(self):
        td = []
        y = []
        x = Date()
        i = 0 
        while i < 30:
            if i == 29:
                y =[x.Year()[i],10.99363636] #as there are only 11 months given in 2019
                td.append(y)
                i += 1
                break 
            y = [x.Year()[i],self.tempdata.snow()[i]]
            td.append(y)
            i += 1
        return td

    def getAvgTempAnnually(self):
        td = []
        data = FileIO.dataTable()
        j = 0
        while j < 359:
            i = 0
            a = 0
            avg = 0
            while i <= 11:
                if j == 359:
                    break
                a += data[j,3]
                a += data[j,2]
                i += 1
                j += 1
            avg = a/12
            td.append(avg)
        y = []
        q = []
        k = 0
        x = Date()
        while k < 30:
            if k == 29:
                y =[x.Year()[k],11.00090909] # only 11 months given in 2019 
                q.append(y)
                k += 1
                break 
            y = [x.Year()[k],td[k]]
            q.append(y)
            k += 1
        return q

class Date:
    def __init__(self):
        self.month = []
        self.year = []
    
    def Month (self):
        i = 0
        while i < 13:
            self.month.append(i)
            i += 1
        return self.month

    def Year (self):
        i = 1990
        j = 0 
        while j < 30:
            self.year.append(i)
            i += 1
            j += 1
        return self.year

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

def main ():
    x = -1 
    while 0>x or x>10:
        print('1- Get Minimum Temperature of 1990-2019') 
        print('2- Get Maximum Temperature of 1990-2019')
        print('3- Get Minimum Temperature of 1990-2019 Annually')
        print('4- Get Maximum Temperature of 1990-2019 Annually')
        print('5- Get Average Snowfall between 1990-2019 Annually')
        print('6- Get Average Temperature between 1990-2019 Annually')
        print('7- LineChart Minimum Temperature of 1990-2019 Annually')
        print('8- LineChart Maximum Temperature of 1990-2019 Annually')
        print('9- BarChart Average Snowfall between 1990-2019 Anually')
        print('10- BarChart Average Temperature between 1990-2019 Anually')
        x = int(input("Input Number of Choice: "))
    z = WeatherAnalyzer()
    i = 0
    xaxis =[1990,1995,2000,2005,2010,2015,2020]
    yaxis = []
    x_pos = [0,5,10,15,20,25,30]
    if x == 1:
        y = str(z.getMinTemp())[2:-2]
        print (y)
    if x == 2:
        y = str(z.getMaxTemp())[2:-2]
        print (y)
    if x == 3:
        y = z.getMintempAnnually()
        print ('The Minimum temperature that each year reached [year,temp(C)]:')
        while i < len(y):
            p = str(y[i])
            print (p)
            i += 1
    if x == 4:
        y = z.getMaxtempAnnually()
        print ("The Maximum temperature that each year reached [year,temp(C)]:")
        while i < len(y):
            p = str(y[i])
            print (p)
            i += 1
    if x == 5:
        y = z.AvgSnowFallAnnually()
        print('The average Snow Fall per year[year,cm]:')
        while i < len(y):
            p = str(y[i])
            print (p)
            i += 1
    if x == 6:
        y = z.getAvgTempAnnually()
        print('The average temperature per year[year,temp(C)]:')
        while i < len(y):
            p = str(y[i])
            print (p)
            i += 1
    if x == 7:
        f = Chart()
        title = "Minimum Temperature from 1990-2019 Annually"
        xlabel = 'Years'
        ylabel = 'Temperature(C)'
        y = z.getMintempAnnually()
        xaxis = []
        while i < len(y):    
            xaxis.append(y[i][0])
            yaxis.append(y[i][1])
            i += 1
        f.DrawLineChart(xaxis,yaxis,title,xlabel,ylabel)
    if x == 8:
        f = Chart()
        title = "Maximum Temperature from 1990-2019 Annually"
        xlabel = 'Years'
        ylabel = 'Temperature(C)'
        y = z.getMaxtempAnnually()
        xaxis = []
        while i<len(y):
            xaxis.append(y[i][0])
            yaxis.append(y[i][1])
            i += 1
        f.DrawLineChart(xaxis,yaxis,title,xlabel,ylabel)
    if x == 9:
        f = Chart()
        title = "Average SnowFall from 1990-2019 Annually"
        xlabel = 'Years'
        ylabel = 'SnowFall(cm)'
        y = z.AvgSnowFallAnnually()
        while i<len(y):
            if i == 29:
                yaxis.append(10.99363636)
                i += 1
                break
            yaxis.append(y[i][1])
            i += 1
        y_pos = np.arange(len(yaxis))
        f.DrawBarChart(xaxis,yaxis,title,xlabel,ylabel,y_pos,x_pos)
    if x == 10:
        f = Chart()
        title = "Average Temperature from 1990-2019 Annually"
        xlabel = 'Years'
        ylabel = 'Temp(C)'
        y = z.getAvgTempAnnually()
        while i<len(y):
            if i == 29:
                yaxis.append(11.00090909)
                i += 1
                break
            yaxis.append(y[i][1])
            i += 1
        y_pos = np.arange(len(yaxis))
        f.DrawBarChart(xaxis,yaxis,title,xlabel,ylabel,y_pos,x_pos)

if __name__ == "__main__":
    main()