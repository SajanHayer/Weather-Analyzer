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
        td.append(f"The maximum temperature between 1990-2019 was: {temp} during July, {year}")
        return td
    
    def MaxtempAnnually(self):
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
                y =[x.Year()[i],10.99363636]
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
                y =[x.Year()[i],11.00090909]
                q.append(y)
                k += 1
                break 
            y = [x.Year()[k],td[k]]
            q.append(y)
            k += 1
        return q