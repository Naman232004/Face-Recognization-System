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

class attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

        img = Image.open(r"E:\Face Recognition System\Background Photos\Student_crowd.webp")
        img = img.resize((1550, 170), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        header_lbl = Label(self.root, image=self.photoimg)
        header_lbl.place(x=0, y=0, width=1550, height=170)

        img1 = Image.open(r"E:\Face Recognition System\Background Photos\background.jpg")
        img1 = img1.resize((1550, 600), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        backgrd_lbl = Label(self.root, image=self.photoimg1)
        backgrd_lbl.place(x=0, y=170, width=1550, height=600)

        # attendance title 
        title_lbl = Label(self.root,text="Attendace System", font=("times new roman", 35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=175,width=1540,height=45)

        #main frame
        main_frame = Frame(backgrd_lbl, bd=3)
        main_frame.place(x=5, y=50, width=1515, height=517)

        # left side frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=("times new roman", 14, "bold"))
        Left_frame.place(x=10, y=10, width=740, height=500)

        img_left = Image.open(r"E:\Face Recognition System\Background Photos\student_portal.png")
        img_left = img_left.resize((717, 100), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        Left_lbl = Label(Left_frame, image=self.photoimg_left)
        Left_lbl.place(x=10, y=0, width=717, height=100)


        # inside left frame 
        inside_left_frame = Frame(Left_frame, bd=2,relief=RIDGE,bg="white")
        inside_left_frame.place(x=10, y=110, width=717, height=360)


        # Attendance id
        attendance_ID = Label(inside_left_frame, text="Antendance ID", font=("times new roman", 12, "bold"))
        attendance_ID.grid(row=0, column=0, padx=10, pady=2)

        attendance_ID_entry = ttk.Entry(inside_left_frame, width=17, font=("times new roman", 15, "bold"))
        attendance_ID_entry.grid(row=0, column=1, padx=10, pady=2, sticky=W)

        # Name
        attendance_ID = Label(inside_left_frame, text="Name", font=("times new roman", 12, "bold"))
        attendance_ID.grid(row=0, column=2, padx=10, pady=2)

        attendance_ID_entry = ttk.Entry(inside_left_frame, width=17, font=("times new roman", 15, "bold"))
        attendance_ID_entry.grid(row=0, column=3, padx=10, pady=2, sticky=W)

        # Date
        attendance_ID = Label(inside_left_frame, text="Date", font=("times new roman", 12, "bold"))
        attendance_ID.grid(row=1, column=0, padx=10, pady=2)

        attendance_ID_entry = ttk.Entry(inside_left_frame, width=17, font=("times new roman", 15, "bold"))
        attendance_ID_entry.grid(row=1, column=1, padx=10, pady=2, sticky=W)

        # Department
        attendance_ID = Label(inside_left_frame, text="Department", font=("times new roman", 12, "bold"))
        attendance_ID.grid(row=1, column=2, padx=10, pady=2)

        attendance_ID_entry = ttk.Entry(inside_left_frame, width=17, font=("times new roman", 15, "bold"))
        attendance_ID_entry.grid(row=1, column=3, padx=10, pady=2, sticky=W)

        # Time
        attendance_ID = Label(inside_left_frame, text="Time", font=("times new roman", 12, "bold"))
        attendance_ID.grid(row=2, column=0, padx=10, pady=2)

        attendance_ID_entry = ttk.Entry(inside_left_frame, width=17, font=("times new roman", 15, "bold"))
        attendance_ID_entry.grid(row=2, column=1, padx=10, pady=2, sticky=W)

        # attendance status
        Label(inside_left_frame, text="Attendance Status", font=("times new roman", 12, "bold")).grid(row=2, column=2, padx=10, pady=2)
        attendance_status_combo = ttk.Combobox(inside_left_frame, font=("times new roman", 12, "bold"),
                                 width=19, state="readonly")
        attendance_status_combo["values"] = ("status", "Present", "Absent")
        attendance_status_combo.grid(row=2, column=3, padx=10, pady=2, sticky=W)
        attendance_status_combo.current(0)


        # Button frames
        btn_frame = Frame(inside_left_frame, bd=1, relief=RIDGE,bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        # buttons
        save_btn = Button(btn_frame, text="Import CSV",width=22, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=1, padx=5, pady=5)

        update_btn = Button(btn_frame, text="Export CSV",  width=22, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=5, pady=5)

        delete_btn = Button(btn_frame, text="Delete", width=22, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=3, padx=5, pady=5)

        reset_btn = Button(btn_frame, text="Reset", width=22, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=4, padx=5, pady=5)


        # right side frame 
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance", font=("times new roman", 14, "bold"))
        right_frame.place(x=770, y=10, width=740, height=500)

        table_frame = Frame(right_frame, bd=1, relief=RIDGE,bg="white")
        table_frame.place(x=5, y=5, width=715, height=455)

        # ===============scrollbar and table ===================
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendanceReportTable = ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendanceReportTable.xview)
        scroll_y.config(command=self.attendanceReportTable.yview)

        self.attendanceReportTable.heading("id", text="Attendance ID")
        self.attendanceReportTable.heading("name", text="Name")
        self.attendanceReportTable.heading("department", text="Department")
        self.attendanceReportTable.heading("time", text="Time")
        self.attendanceReportTable.heading("date", text="Date")
        self.attendanceReportTable.heading("attendance", text="Attendance")

        self.attendanceReportTable["show"] = "headings"
        
        self.attendanceReportTable.column("id",width=100)
        self.attendanceReportTable.column("name",width=100)
        self.attendanceReportTable.column("department",width=100)
        self.attendanceReportTable.column("time",width=100)
        self.attendanceReportTable.column("date",width=100)
        self.attendanceReportTable.column("attendance",width=100)

        self.attendanceReportTable.pack(fill=BOTH,expand=1)

    # ========================fetch data==============================

    def fetchData(self,rows):
        self.attendanceReportTable.delete(*self.attendanceReportTable.get_children())

        for i in rows :
            self.attendanceReportTable.insert("",END,values=i)
        


if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop() 