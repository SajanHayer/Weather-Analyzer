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


#x = Date()

#print (x.Month()[12],x.Year()[29])