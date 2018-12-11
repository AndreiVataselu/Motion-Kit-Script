from gpiozero import MotionSensor
import time
import pyrebase
import pygame
import pygame.camera
import pyimgur

config = {
    #CONFIG DICT FROM FIREBASE
}

IMGUR_CLIENT_ID = #CONFIG IMGUR Client ID
imgur = pyimgur.Imgur(IMGUR_CLIENT_ID)
firebase = pyrebase.initialize_app(config)
photo_name = 0
db = firebase.database()
pir = MotionSensor(21)
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()


while True:
    time.sleep(1)
    if pir.motion_detected:
        PATH = "/home/pi/Desktop/images/{}.jpg".format(photo_name)
        initialize_photo = cam.get_image()
        initialize_photo = cam.get_image()
        initialize_photo = cam.get_image()
        img = cam.get_image()
        pygame.image.save(img, PATH)
        time.sleep(1)
        uploaded_image = imgur.upload_image(PATH)
        time.sleep(1)
        db.child("detections").child(time.strftime("%e %b-%H:%M").strip()).push(uploaded_image.link)
        time.sleep(7)


