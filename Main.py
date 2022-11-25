import numpy as np
import matplotlib.pyplot


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
    xaxis = [1990,1995,2000,2005,2010,2015,2020]
    x_pos = [0,5,10,15,20,25,30]
    yaxis = []
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
        y = z.getAvgTempAnnually
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
        y = z.getMintempAnnually
        xaxis = []
        while i<len(y):
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
                yaxis.append(11)
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
                yaxis.append(11)
                i += 1
                break
            yaxis.append(y[i][1])
            i += 1
        y_pos = np.arange(len(yaxis))
        f.DrawBarChart(xaxis,yaxis,title,xlabel,ylabel,y_pos,x_pos)



if __name__ =='__main__':
    main()