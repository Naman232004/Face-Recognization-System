from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import numpy as np 

class Train:
    def __init__(self, root):
        
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

        title_lbl = Label(self.root,text="TRAIN DATA SET", font=("times new roman", 35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1540,height=45)

        img_top = Image.open(r"E:\Face Recognition System\Background Photos\training_data.png")
        img_top = img_top.resize((1540, 300), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Left_lbl = Label(self.root, image=self.photoimg_top)
        Left_lbl.place(x=0, y=45, width=1540, height=300)

        # button 
        b1_1 = Button(self.root,text="Train Data",cursor="hand2",command=self.train_classifier, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=0,y=370,width=1540,height=100)

        img_bottom = Image.open(r"E:\Face Recognition System\Background Photos\taining_data_2.jpg")
        img_bottom = img_bottom.resize((1540, 300), Image.Resampling.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Left_lbl = Label(self.root, image=self.photoimg_bottom)
        Left_lbl.place(x=0, y=500, width=1540, height=300)


    def train_classifier(self):
        data_dir = (r"E:\Face Recognition System\Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # gray scale image 
            image_np = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            ids.append(id)

            cv2.imshow("Training",image_np)
            cv2.waitKey(1)

        ids=np.array(ids)

        # ================== Train Classifier ===========================
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write(r"E:\Face Recognition System\classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Set Completed")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop() 