import sys
import pymongo
import os

def search():
    key = input("please input keyword: ")

    myclient = pymongo.MongoClient()
    mydb = myclient.Twitter

    myquery1 = {"label1" : ("%s") % (key)}
    data = mydb.twitterInfo.find(myquery1)
    for res in data:
        print(res)

    myquery2 = {"label2" : ("%s") % (key)}
    data = mydb.twitterInfo.find(myquery2)
    for res in data:
        print(res)

    myquery3 = {"label3" : ("%s") % (key)}
    data = mydb.twitterInfo.find(myquery3)
    for res in data:
        print(res)

if __name__ == "__main__":
    search()