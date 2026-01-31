
from tkinter import *           # for basic GUI
from tkinter import ttk         # for better styling 
from PIL import Image,ImageTk   # image open and edit images. and ImageTK converts an image into a format Tkinter can use inside GUI.
from student_details import Student
from train import Train
from face_recognization import Face_Recognition 
from attendance import attendance
import os 

class Face_Recogization_system :
    def __init__(self,root):
        self.root = root 
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System") 

        #first image
        img = Image.open(r"E:\Face Recognition System\Background Photos\updated_header.png")  #open image to given path
        img = img.resize((1550,200),Image.Resampling.LANCZOS) # size given for image 
        self.photoimg = ImageTk.PhotoImage(img) # converted into form which can understandale to PIL

        header_lbl = Label(self.root,image = self.photoimg) # image given to label of window 
        header_lbl.place(x=0, y=0, width=1550, height= 200) # size of label 

        #background image
        img1 = Image.open(r"E:\Face Recognition System\Background Photos\background.jpg")  
        img1 = img1.resize((1550,600),Image.Resampling.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)

        backgrd_lbl = Label(self.root,image = self.photoimg1)
        backgrd_lbl.place(x=0, y=200, width=1550, height= 600)

        #student Details 
        img2 = Image.open(r"E:\Face Recognition System\Background Photos\student_button.png")  
        img2 = img2.resize((220,220),Image.Resampling.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(backgrd_lbl,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=220,y=30,width=220,height=220)

        b1_1 = Button(backgrd_lbl,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=220,y=220,width=220,height=40)


        #Face Detector
        img3 = Image.open(r"E:\Face Recognition System\Background Photos\student face regiter.jpg")  
        img3 = img3.resize((220,220),Image.Resampling.LANCZOS)  
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(backgrd_lbl,image=self.photoimg3,cursor="hand2",command=self.Face_data)
        b1.place(x=500,y=30,width=220,height=220)

        b1_1 = Button(backgrd_lbl,text="Face Detector",cursor="hand2",command=self.Face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=220,width=220,height=40)
      
        #Attendance
        img4 = Image.open(r"E:\Face Recognition System\Background Photos\attendance.jpg")  
        img4 = img4.resize((220,220),Image.Resampling.LANCZOS)  
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(backgrd_lbl,image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b1.place(x=780,y=30,width=220,height=220)

        b1_1 = Button(backgrd_lbl,text="Attendance",cursor="hand2",command=self.attendance_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=780,y=220,width=220,height=40)

        #Help Desk
        img6 = Image.open(r"E:\Face Recognition System\Background Photos\Help desk.jpg")  
        img6 = img6.resize((220,220),Image.Resampling.LANCZOS)  
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(backgrd_lbl,image=self.photoimg6,cursor="hand2")
        b1.place(x=1060,y=30,width=220,height=220)

        b1_1 = Button(backgrd_lbl,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1060,y=220,width=220,height=40)


        #Train Data
        img10 = Image.open(r"E:\Face Recognition System\Background Photos\train data.jpg")  
        img10 = img10.resize((220,220),Image.Resampling.LANCZOS)  
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(backgrd_lbl,image=self.photoimg10,cursor="hand2",command=self.Train_Data)
        b1.place(x=220,y=300,width=220,height=220)

        b1_1 = Button(backgrd_lbl,text="Train Data",cursor="hand2",command=self.Train_Data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=220,y=490,width=220,height=40)

        #Photos
        img9 = Image.open(r"E:\Face Recognition System\Background Photos\photsos.jpg")  
        img9 = img9.resize((220,220),Image.Resampling.LANCZOS)  
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(backgrd_lbl,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=300,width=220,height=220)

        b1_1 = Button(backgrd_lbl,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=490,width=220,height=40)

        #Developer
        img8 = Image.open(r"E:\Face Recognition System\Background Photos\developer.png")  
        img8 = img8.resize((220,220),Image.Resampling.LANCZOS)  
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(backgrd_lbl,image=self.photoimg8,cursor="hand2")
        b1.place(x=780,y=300,width=220,height=220)

        b1_1 = Button(backgrd_lbl,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=780,y=490,width=220,height=40)


        #Exit
        img7 = Image.open(r"E:\Face Recognition System\Background Photos\exit.jpg")  
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)  
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(backgrd_lbl,image=self.photoimg7,cursor="hand2")
        b1.place(x=1060,y=300,width=220,height=220)

        b1_1 = Button(backgrd_lbl,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1060,y=490,width=220,height=40)
    
    def open_img(self):
        os.startfile("E:\Face Recognition System\Data")

    # ==============Function Buttons=================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app = Student(self.new_window)

    def Train_Data(self):
        self.new_window=Toplevel(self.root)
        self.app = Train(self.new_window)

    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app = attendance(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recogization_system(root)
    root.mainloop() #Keeps the GUI running until you close it manually
