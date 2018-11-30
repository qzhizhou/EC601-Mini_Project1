from google_vision import GoogleVision
import sys
import pymysql

def main():
    try:
        #get tweets information: # of pic, related labels
        twitterID = sys.argv[1]
        twitterAnalysis = GoogleVision()
        count = twitterAnalysis.getNumOfImages()
        print(count)
        labels = twitterAnalysis.getLabels()
        for label in labels:
            print(label)
    except:
        print("google vision is out of order!")

    #connect to the database
    db = pymysql.connect("localhost", "root", "123456789", "twitter")
    myCursor = db.cursor()
    print(db)
    myCursor.execute("SHOW TABLES") 
    for tb in myCursor:
        print(tb)
        
    #insert colunms into table tweetsInfomation
    try:
        sqlFormula = "INSERT INTO tweetsInfomation (name, images, label1, label2, label3) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')" % (twitterID, count, labels[0], labels[1], labels[2])
        #twitterInformation = [(str(twitterID), count, str(labels))]
        myCursor.execute(sqlFormula)
        db.commit() #save and make changes to the table
    except:
        print("can not insert columns")
        db.rollback()
        db.close()

if __name__ == "__main__":
    main()
