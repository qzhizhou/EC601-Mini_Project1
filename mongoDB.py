import pymongo
import sys
import os

myclient = pymongo.MongoClient()

#create a db called Twitter
mydb = myclient.Twitter

twitterID = "gilbert_alfie"
count = 10
label1 = "dog"
label2 = "cat"
label3 = "human"
mydb.twitterInfo.insert_one(
    {"id":("%s")%(twitterID), "images": ("%s")%(count), "label1":("%s")%(label1), "label2":("%s")%(label2), "label3":("%s")%(label3)}
)

