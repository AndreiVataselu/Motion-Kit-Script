# Motion-Kit-Script
The script for Raspberry PI. Uses a webcam and a PIR HC-SR501 for motion detection. Whenever motion is detected, the webcam will take a picture, upload it on imgur and push the link along with the timestamp the motion was found, to a Firebase database. 

I put this script on the crontab so whenever I power up my Raspberry PI, the scripts starts automatically.

Will upload soon a iOS App which uses the data from Firebase and sends a push notification whenever the Pi pushes to database. You will be able to view the image directly from the app.
