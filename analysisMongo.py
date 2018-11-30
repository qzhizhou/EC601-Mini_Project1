from google_vision import GoogleVision
import sys
import pymongo

def main():
    try:
        #get tweets information: # of pic, related labels
        twitterID = sys.argv[1]
        twitterAnalysis = GoogleVision()
        count = twitterAnalysis.getNumOfImages()
        print(count)
        labels = twitterAnalysis.getLabels()
        # for label in labels:
        #     print(label)
    except:
        print("google vision is out of order!")

    #connect to mongoDB:
    myclient = pymongo.MongoClient()
    mydb = myclient.Twitter
    try:
        mydb.twitterInfo.insert_one({"id":("%s")%(twitterID), "images": ("%s")%(count), "label1":("%s")%(labels[0]), "label2":("%s")%(labels[1]), "label3":("%s")%(labels[2])})
    except:
        print("can not insert columns")

if __name__ == "__main__":
    main()