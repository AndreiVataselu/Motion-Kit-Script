# Motion-Kit-Script
The script for Raspberry PI. Uses a webcam and a PIR HC-SR501 for motion detection. Whenever motion is detected, the webcam will take a picture, upload it on imgur and push the link along with the timestamp the motion was found, to a Firebase database. 

I put this script on crontab so whenever I power up my Raspberry PI, the scripts starts automatically.

iOS App to vizualize the data from Pi in realtime here: https://github.com/AndreiVataselu/Motion-Kit-App
