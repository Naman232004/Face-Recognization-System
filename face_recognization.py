from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import numpy as np 
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

        title_lbl = Label(self.root,text="FACE RECOGNIZATION", font=("times new roman", 35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1540,height=45)

        #first image
        img_top = Image.open(r"E:\Face Recognition System\Background Photos\Screenshot 2025-10-03 164803.png")
        img_top = img_top.resize((730, 700), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        Left_lbl = Label(self.root, image=self.photoimg_top)
        Left_lbl.place(x=0, y=45, width=730, height=700)

        # second image 
        img2_top = Image.open(r"E:\Face Recognition System\Background Photos\face_recognization.jpg")
        img2_top = img2_top.resize((800, 700), Image.Resampling.LANCZOS)
        self.photoimg_img2 = ImageTk.PhotoImage(img2_top)

        right_lbl = Label(self.root, image=self.photoimg_img2)
        right_lbl.place(x=730, y=45, width=800, height=700)

        b1_1 = Button(right_lbl,text="Detect Face",cursor="hand2",command=self.face_recog,font=("times new roman",15,"bold"),bg="red",fg="white")
        b1_1.place(x=400,y=600,width=200,height=50)

    # mark attendance 
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","a+",newline="\n") as f :
            f.seek(0)
            my_data_list = f.readlines()
            name_list = []
            for line in my_data_list:
                entry = line.split((","))
                name_list.append(entry[0]) 

            if((i not in name_list )) :
                now = datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")

    #face recognization 

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                
                # Predict face
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int(100 * (1 - predict / 300))

                conn = mysql.connector.connect(host="localhost", user="root", password="Mh157974#", database="student_details")
                my_cursor = conn.cursor() 

                my_cursor.execute("select Name from student where Student_ID="+str(id))
                n=my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select `Roll No` from student where Student_ID="+str(id))
                r=my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Dept from student where Student_ID="+str(id))
                d=my_cursor.fetchone()
                d = "+".join(d)

                my_cursor.execute("select Student_ID from student where Student_ID="+str(id))
                i=my_cursor.fetchone()
                i = "+".join(i)


                if confidence > 77:
                    cv2.putText(img,f"Student_ID:{i}",org=(x,y-75),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.8,color=(0,0,255),thickness=3)
                    cv2.putText(img,f"Roll No:{r}",org=(x,y-55),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.8,color=(0,0,255),thickness=3)
                    cv2.putText(img,f"Name:{n}",org=(x,y-30),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.8,color=(0,0,255),thickness=3)
                    cv2.putText(img,f"Department:{d}",org=(x,y-5),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.8,color=(0,0,255),thickness=3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), color=(0,0,255), thickness=3)
                    cv2.putText(img,"Unknown Face",org=(x,y-5),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.8,color=(255,255,255),thickness=3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,scaleFactor=1.1,minNeighbors=10,color=(255,255,255),text="Face",clf=clf)
            return img
        
        facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        
        while(True):
            ret,img=video_cap.read()
            img= recognize(img,clf,facecascade)
            cv2.imshow("Welcome to Face Recognization",img)

            if(cv2.waitKey(1)==13):
                break  
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop() 