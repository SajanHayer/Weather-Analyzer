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