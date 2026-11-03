import datetime
import os

x=datetime.datetime.now()

for i in range(10):
    date=x+datetime.timedelta(days=i)
    filename=date.strftime("%y-%m-%d")+".txt"
    with open(filename,"w")as f:
        f.write("this is my file")

        print(filename,"created")






# "https://api.sampleapis.com/coffee/hot
# https://dummyjson.com/products