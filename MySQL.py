import pymysql

#create a database
# db = pymysql.connect("localhost", "root", "123456789")
#     myCursor = db.cursor()
#     myCursor.execute("CREATE DATABASE twitter")

# connect to the database
db = pymysql.connect("localhost", "root", "123456789", "twitter")

myCursor = db.cursor()

#create a table called tweetsInfo to store name, #of images, labels
myCursor.execute("CREATE TABLE tweetsInfomation (name VARCHAR(255), images INTEGER(10), label1 VARCHAR(255), label2 VARCHAR(255), label3 VARCHAR(255))")