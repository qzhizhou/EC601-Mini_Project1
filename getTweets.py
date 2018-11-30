from Tweepy_images import TweepyAPI
import sys

class getTweets():
    def __init__(self,name):
        self.name = name
    
    def runAndStore(self):
        try:
            downloadImages = TweepyAPI(self.name)
            downloadImages.download()
        except:
            EOFError

def main():
    try:
        twitterID = sys.argv[1]
        db = getTweets(twitterID)
        db.runAndStore()
    except:
        print("Plese include the twitter id in command line!")

if __name__ == "__main__":
    main()