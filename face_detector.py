from ast import While
import cv2
from random import randrange

#Seçilen Resimdeki Yüzlerin Bulunması

#Opencv'ye haar cascade algoritmasıyla daha önceden eğitilmiş yüz verilerini yükledim
# trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Yüz tanıma için bir resim seçtim
# img = cv2.imread('Robert.jfif')

#Yüz tanımanın gerçekleşebilmesi için önce resimi siyah beyaza dönüştürdüm
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Yüzün Tanımlanması
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
##print(face_coordinates)

#Yüzün etrafına dörtgen çizilmesi
# for (x, y, w, h) in face_coordinates:
#     cv2.rectangle(img, (x, y), (x+w, x+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)

#Resmin Gösterilmesi
# cv2.imshow('Yuz Tanimlama', img)

#Birşeye tıklayana kadar resmin gösterilmeye devam etmesi
# cv2.waitKey()

# print('Code Completed')




#Yüklenilen video veya Webcam'dan Yüzlerin tespit edilmesi

#Opencv'ye haar cascade algoritmasıyla daha önceden eğitilmiş yüz verilerini yükledim
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Webcam'dan video çekebilmek için
webcam = cv2.VideoCapture(0)

while True:
    
    #Geçerli Karenin Okunması
    successful_frame_read, frame = webcam.read()

    #Yüz Okuma için siyah beyaza çevirme
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Yüzün Tanımlanması
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    #Yüzün etrafına dörtgen çizilmesi
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, x+h), (randrange(128,256), randrange(128,256), randrange(128,256)), 2)

    cv2.imshow('Yuz Tanıma', frame)
    key = cv2.waitKey(1)
    
    # Q'ya basıp uygulamadan çıkmaya yarar.
    if key == 81 or key == 113:
        break

webcam.release()






