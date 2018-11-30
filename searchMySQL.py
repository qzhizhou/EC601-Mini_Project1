import pymysql
import sys
import os

def search():
    key = input("please input keyword: ")
    db = pymysql.connect("localhost", "root", "123456789", "twitter")
    myCursor = db.cursor()

    #choose from table at label1
    sql1 = "SELECT * FROM tweetsInfomation \
           WHERE label1 LIKE '%s'" % (key)
    myCursor.execute(sql1)
    myResult = myCursor.fetchall()
    for res in myResult:
        print(res)
    
    #choose from table at label2
    sql2 = "SELECT * FROM tweetsInfomation \
           WHERE label2 LIKE '%s'" % (key)
    myCursor.execute(sql2)
    myResult = myCursor.fetchall()
    for res in myResult:
        print(res)

    #choose from table at label3
    sql3 = "SELECT * FROM tweetsInfomation \
           WHERE label3 LIKE '%s'" % (key)
    myCursor.execute(sql3)
    myResult = myCursor.fetchall()
    for res in myResult:
        print(res)

if __name__ == "__main__":
    search()