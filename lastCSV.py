from collections import defaultdict
from csv import reader 
with open("csvv.csv") as file:
    dat = reader(file)
    header = next(dat)
    data = list(dat)
    
    date = header.index("date")
    cost = header.index("cost")
    product_name = header.index("product_name")
    

    def allSums():
        all = defaultdict(int)
        for i in data:
            all[i[product_name]]+=1
        return all
    
    def sums():
        all = defaultdict(float)
        for i in data:
            all[i[product_name]] += float(i[cost])
        return all

    print(sums())
                


    

   