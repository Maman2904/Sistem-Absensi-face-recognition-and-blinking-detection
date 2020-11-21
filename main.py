import tkinter as tk
import cv2
import csv
import os
import dlib
import face_recognition
import time
import datetime
import numpy as np
from math import hypot
from tkinter import *

def jam():
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
    dtString = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

def show_frame(frame):
    frame.tkraise()

window = tk.Tk()
window.attributes('-zoom', True)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)


frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)


for fra in (frame1, frame2, frame3):
    fra.grid(row=0,column=0,sticky='nsew')

gambar = tk.PhotoImage(file = 'design/it.png')
bgLabel = tk.Label(frame1, image = gambar)
bgLabel.place (relwidth = 1, relheight =1 )

gambar1 = tk.PhotoImage(file = 'design/tech2.png')
bgLabel = tk.Label(frame2, image = gambar1)
bgLabel.place (relwidth = 1, relheight =1 )

gambar2 = tk.PhotoImage(file = 'design/tech.png')
bgLabel = tk.Label(frame3, image = gambar2)
bgLabel.place (relwidth = 1, relheight =1 )

gambar3 = tk.PhotoImage(file = 'design/register.png')
bgLabel.place (relwidth = 1, relheight =1 )

gambar4 = tk.PhotoImage(file = 'design/absen.png')
bgLabel.place (relwidth = 1, relheight =1 )


frame1_title= tk.Label(frame1, text='ABSENSI SYSTEM', bg='gray')
frame1_title.pack(fill='x')

message = tk.Label(frame1, text="SISTEM ABSENSI KEHADIRAN DETEKSI WAJAH \n"
                              "PT KARYA KOMPONEN PRESISI", bg="green", fg="white", width=100, height=3,
                   font=('times', 30,
                         'bold underline'))
message.place(x=0, y=20)

wel = tk.Label(frame1, text="SELAMAT DATANG", bg="blue",fg="white", font=('times', 50))
wel.place(x=680, y=200)

sell = tk.Label(frame1, text="Silahkan Registrasi Atau Absen Sekarang", bg="blue",fg="white", font=('times', 30))
sell.place(x=650, y=270)

labreg = tk.Label(frame1, text="REGISTRASI", bg="blue", fg="white",font=('times', 25))
labreg.place(x=570, y=420)

lababs = tk.Label(frame1, text="ABSEN SEKARANG", bg="blue", fg="white",font=('times', 25))
lababs.place(x=1080, y=420)

reg = tk.Button(frame1,image = gambar3, text="", command=lambda:show_frame(frame2), bg="red", fg="black", activebackground="yellow",
                font=('times', 50, 'bold'))
reg.place(x=530, y=480)

abs = tk.Button(frame1, image = gambar4, text="ABSEN NOW", command=lambda:show_frame(frame3), bg="yellow", fg="black",activebackground="red",
                font=('times', 50, 'bold'))
abs.place(x=1100, y=480)


###############################################################################################

frame2_title= tk.Label(frame2, text='REGISTRASI', bg='gray')
frame2_title.pack(fill='x')
lbl = tk.Label(frame2, text="SISTEM ABSENSI KEHADIRAN DETEKSI WAJAH \n"
                                  "PT KARYA KOMPONEN PRESISI", bg="green", fg="white", width=50, height=3,
                       font=('times', 30,
                             'bold underline'))
lbl.place(x=470, y=20)

wel = tk.Label(frame2, text="REGISTRASI", bg="blue",fg="white", font=('times', 50))
wel.place(x=780, y=180)

lblnpk = tk.Label(frame2, text="NPK", width=20, height=2, bg="white", fg="black", font=('times', 15, 'bold'))
lblnpk.place(x=600, y=300)

txt = tk.Entry(frame2, width=30, bg="white", fg="black", font=('times', 15, 'bold'))
txt.place(x=850, y=310)

lblname = tk.Label(frame2, text="NAMA", width=20, height=2, bg="white", fg="black", font=('times', 15, 'bold'))
lblname.place(x=600, y=400)

txt2 = tk.Entry(frame2, width=30, bg="white", fg="black", font=('times', 15, 'bold'))
txt2.place(x=850, y=410)

lblnotif = tk.Label(frame2, text="Notification :", width=20, height=2, bg="white", fg="black",
                        font=('times', 15, 'bold underline'))
lblnotif.place(x=600, y=550)

pesan = tk.Label(frame2, text="", bg="white", fg="red", width=48, height=2, activebackground="yellow",
                       font=('times', 15, 'bold'))
pesan.place(x=850, y=550)

def clear():
    txt.delete(0, 'end')
    res = ""
    pesan.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = ""
    pesan.configure(text=res)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def Register():
    Id = (txt.get())
    name = (txt2.get())
    if (is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        #harcascadePath = "haarcascade_frontalface_default.xml"
        #detector = cv2.CascadeClassifier(harcascadePath)
        #sampleNum = 1
        while (True):
            ret, img = cam.read()
            #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #faces = detector.detectMultiScale(gray, 1.3, 5)
            '''for (x, y, w, h) in faces:
                cropped = img[y:y + h, x:x + w]
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2, cv2.LINE_AA)'''
                #sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                # display the frame'''
            cv2.imshow('frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite("DataGambar/" + Id +"_"+ name + ".jpeg", img)
                break
            # break if the sample number is morethan 100
           # elif sampleNum > 1:
               # break
        cam.release()
        cv2.destroyAllWindows()
        res = "Data disimpan dengan NPK : " + Id + " Name : " + name
        row = [Id, name]
        with open('DataKaryawan/KaryawanDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        pesan.configure(text=res)
    else:
        if (is_number(Id)):
            res = "Masukan Huruf Pada Kolom Nama"
            pesan.configure(text=res)
        if (name.isalpha()):
            res = "Masukan Angka Pada Kolom NPK "
            pesan.configure(text=res)
        if (is_number(Id) & name.isalpha()):
            res = "Masukan Huruf Pada Kolom Nama \n dan \n Masukan Angka pada kolom NPK "
            pesan.configure(text=res)


    return (Register)

hapus = tk.Button(frame2, text="Hapus", command=clear, bg="white", fg="black", activebackground="violet",
                  font=('times', 15, 'bold'))
hapus.place(x=1250, y=310)

hapus2 = tk.Button(frame2, text="Hapus", command=clear2, bg="white", fg="black", activebackground="violet",
                   font=('times', 15, 'bold'))
hapus2.place(x=1250, y=410)

register = tk.Button(frame2, text="INPUT DATA GAMBAR", command=Register, bg="blue", fg="black",
                         activebackground="violet",font=('times', 15, 'bold'))
register.place(x=880, y=480)

quit = tk.Button(frame2, text="back", command=lambda:show_frame(frame1), bg="white", fg="black", activebackground="violet",
                 font=('times', 15, 'bold'))
quit.place(x=1400, y=750)

##########################################################################################################

frame3_title = tk.Label(frame3, text='Absen Now', bg='gray')
frame3_title.pack(fill='x')
message = tk.Label(frame3, text="SISTEM ABSENSI KEHADIRAN DETEKSI WAJAH \n"
                                  "PT KARYA KOMPONEN PRESISI", bg="green", fg="white", width=50, height=3,
                       font=('times', 30,
                             'bold underline'))
message.place(x=470, y=20)

wel = tk.Label(frame3, text="ABSEN SEKARANG", bg="blue",fg="white", font=('times', 50))
wel.place(x=670, y=180)

sell = tk.Label(frame3, text="Silahkan Pilih ABSEN MASUK Atau ABSEN PULANG", bg="blue",fg="yellow", font=('times', 30))
sell.place(x=510, y=270)

def listPulang():
    path = 'DataGambar'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):
        with open('Data_Absen/Pulang.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
            dtString = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            f.writelines(f'\n{name},{dtString},{date}')
            return nameList


    #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
    # def captureScreen(bbox=(300,300,690+300,530+300)):
    #     capScr = np.array(ImageGrab.grab(bbox))
    #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    #     return capScr

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    count = 0

    def midpoint(p1, p2):
        return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

    font = cv2.FONT_HERSHEY_COMPLEX

    def get_blinking_ratio(eye_points, facial_landmarks):
        left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
        right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
        center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
        center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

        hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
        ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

        hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
        ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

        ratio = hor_line_lenght / ver_line_lenght
        return ratio

    attendance = ("Ok Anda Sudah Absen Pulang Dengan NPK :")

    while True:
        success, frame = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        faces = detector(imgS)

        for face, encodeFace, faceLoc in zip(faces, encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                landmarks = predictor(imgS, face)

                left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
                right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
                blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

                if blinking_ratio > 5.7:
                    cv2.putText(frame, "HIDUP", (50, 150), font, 3, (0, 0, 255))
                    count = count + 1


        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if count > 1:
            markAttendance(name)
            break

    cap.release()
    cv2.destroyAllWindows()


    res = attendance + name
    message2.configure(text=res)

def listMasuk():
    path = 'DataGambar'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):
        with open('Data_Absen/Masuk.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            ts = time.time()
            date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%y')
            dtString = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            f.writelines(f'\n{name},{dtString},{date}')
            return nameList


    #### FOR CAPTURING SCREEN RATHER THAN WEBCAM
    # def captureScreen(bbox=(300,300,690+300,530+300)):
    #     capScr = np.array(ImageGrab.grab(bbox))
    #     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    #     return capScr

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    count = 0

    def midpoint(p1, p2):
        return int((p1.x + p2.x) / 2), int((p1.y + p2.y) / 2)

    font = cv2.FONT_HERSHEY_COMPLEX

    def get_blinking_ratio(eye_points, facial_landmarks):
        left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
        right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
        center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
        center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

        hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
        ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

        hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
        ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

        ratio = hor_line_lenght / ver_line_lenght
        return ratio

    attendance = ("Ok Anda Sudah Absen Masuk dengan NPK :")

    while True:
        success, frame = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        faces = detector(imgS)

        for face, encodeFace, faceLoc in zip(faces, encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                landmarks = predictor(imgS, face)

                left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
                right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
                blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

                if blinking_ratio > 5.7:
                    cv2.putText(frame, "BLINKING", (50, 150), font, 3, (0, 0, 255))
                    count = count + 1


        cv2.imshow('Webcam', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if count > 1:
            markAttendance(name)
            break

    cap.release()
    cv2.destroyAllWindows()


    res = attendance + name
    message2.configure(text=res)

masuk = tk.Button(frame3, text="ABSEN MASUK", command=listMasuk, bg="white", fg="black", activebackground="violet",
                  font=('times', 15, 'bold'))
masuk.place(x=860, y=380)

pulang = tk.Button(frame3, text="ASBSEN PULANG", command=listPulang, bg="white", fg="black", activebackground="violet",
                   font=('times', 15, 'bold'))
pulang.place(x=850, y=480)

message2 = tk.Label(frame3, text="", bg="white", fg="red", width=60, height=4, activebackground="yellow",
                        font=('times', 15, 'bold'))
message2.place(x=650, y=600)

back = tk.Button(frame3, text="back", command=lambda:show_frame(frame1), bg="white", fg="black", activebackground="violet",
                 font=('times', 15, 'bold'))
back.place(x=1400, y=650)

show_frame(frame1)
window.mainloop()