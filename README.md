# EC601-Project1- Twitter API & Google Vision

It is to build a library (in python) that downloads images from a twitter feed, convert them to a video and describe the   content of the images in the video.

## 1. Use Tweepy to Download Images:

### 1.1 Get the Twitter API Credential:

Go to https://developer.twitter.com/content/developer-twitter/en.html and apply for a Twitter developer account. Once you haved finished, you will recieve the keys and tokens. Mark them down and keep them safe! 

### 1.2 Install Tweepy:  

Installing Tweepy is pretty easy:  

	pip install tweepy  
  
### 1.3 Run the Tweepy-images.py:  
Once you have got all the credential files in the directory where you download this git, you now can try to download images from Twitter:  

	python Tweepy-images.py  
		
But before you run, please open the Tweepy-images.py file, and input you keys and tokens.  
In line 24, you will need to input the Twitter account you want to access, and also you can change the limit number of images by changing the number after "count="
  
## 2.Use Google Vision to analyze Images:  
  
  ### 2.1 Set up the Google Vision environment:  
  Go to https://cloud.google.com/vision/docs/quickstart-client-libraries and follow the instructions.  
   Please make sure that the path and the credenstial files are all located in your current directory!  
      
  ### 2.2 Run the google_vision.py:  
  In line 17 and 69, please change the path to your current directory.  
  And now you can run:  
    
	python google_vision.py  
	  
Go to your current directory and view all the images. Labels now are printed on images.  
  
## 3. Use FFMPEG to Convert Images into Videos:  
  
	1>> install brew ffmpeg
	2>> ffmpeg -loop 1 -y -i %d.jpg -i WE-WILL-ROCK-YOU.mp3 -r 1 -t 18 -absf aac_adtstoasc output.mp4   
	
Please enjoy the output.mp4!  
  
 ## 4. Run the Tweepy_GoogleVersion.py:
 The Tweepy_GoogleVersion.py file is a combination of the .py files above.  
 Before you run this python program, please redo the PATH steps mentioned above.   
   
    python Tweepy_GoogleVersion.py  
    
Once you successfully run the program, you gain the accesss to every valid Twitter account to download the images they uploaded and analyze what the pics are about and view them in an awesome video!


