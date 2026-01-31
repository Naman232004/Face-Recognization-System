from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System")

        # ================== Variables ======================
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_ID = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var1_radio1 = StringVar()

        # ---------- Header images (paths used from your original code) ----------
        img = Image.open(r"E:\Face Recognition System\Background Photos\Student_crowd.webp")
        img = img.resize((1550, 200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        header_lbl = Label(self.root, image=self.photoimg)
        header_lbl.place(x=0, y=0, width=1550, height=200)

        img1 = Image.open(r"E:\Face Recognition System\Background Photos\background.jpg")
        img1 = img1.resize((1550, 600), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        backgrd_lbl = Label(self.root, image=self.photoimg1)
        backgrd_lbl.place(x=0, y=200, width=1550, height=600)

        # main frame
        main_frame = Frame(backgrd_lbl, bd=3)
        main_frame.place(x=5, y=10, width=1505, height=560)

        # left side frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Deatils", font=("times new roman", 14, "bold"))
        Left_frame.place(x=10, y=10, width=720, height=530)

        img_left = Image.open(r"E:\Face Recognition System\Background Photos\student_portal.png")
        img_left = img_left.resize((710, 120), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        
        Left_lbl = Label(Left_frame, image=self.photoimg_left)
        Left_lbl.place(x=5, y=0, width=705, height=120)

        # current course frame
        current_course_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Current course", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=125, width=705, height=130)

        # Department
        dept_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"))
        dept_label.grid(row=0, column=0, padx=10)
        dept_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dept, font=("times new roman", 12, "bold"),
                                  width=17, state="readonly")
        dept_combo["values"] = ("Select Department", "CS", "ENTC", "Mech", "Civil")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 12, "bold"))
        course_label.grid(row=0, column=2, padx=10)
        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=("times new roman", 12, "bold"),
                                    width=17, state="readonly")
        course_combo["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 12, "bold"))
        year_label.grid(row=1, column=0, padx=10)
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"),
                                  width=17, state="readonly")
        year_combo["values"] = ("Select year", "2022-23", "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 12, "bold"))
        semester_label.grid(row=1, column=2, padx=10)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=("times new roman", 12, "bold"),
                                      width=17, state="readonly")
        semester_combo["values"] = ("Select Sem", "1st", "2nd")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=20, sticky=W)

        # class student information frame
        class_student_info_frame = LabelFrame(Left_frame, bd=2, relief=RIDGE, text="Class student information", font=("times new roman", 12, "bold"))
        class_student_info_frame.place(x=5, y=260, width=705, height=240)

        # Student ID
        Label(class_student_info_frame, text="Student ID", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=2)
        ttk.Entry(class_student_info_frame, textvariable=self.var_std_ID, width=20, font=("times new roman", 12, "bold")).grid(row=0, column=1, padx=10, pady=2, sticky=W)

        # Student Name
        Label(class_student_info_frame, text="Student Name", font=("times new roman", 12, "bold")).grid(row=0, column=2, padx=10, pady=2)
        ttk.Entry(class_student_info_frame, textvariable=self.var_std_name, width=20, font=("times new roman", 12, "bold")).grid(row=0, column=3, padx=10, pady=2, sticky=W)

        # Class Division
        Label(class_student_info_frame, text="Class Division", font=("times new roman", 12, "bold")).grid(row=1, column=0, padx=10, pady=2)
        Div_combo = ttk.Combobox(class_student_info_frame, textvariable=self.var_div, font=("times new roman", 12, "bold"),
                                 width=17, state="readonly")
        Div_combo["values"] = ("A", "B", "C", "D", "F")
        Div_combo.grid(row=1, column=1, padx=10, pady=2, sticky=W)
        Div_combo.current(0)

        # Roll No
        Label(class_student_info_frame, text="Roll No", font=("times new roman", 12, "bold")).grid(row=1, column=2, padx=10, pady=2)
        ttk.Entry(class_student_info_frame, textvariable=self.var_roll, width=20, font=("times new roman", 12, "bold")).grid(row=1, column=3, padx=10, pady=2, sticky=W)

        # Gender
        Label(class_student_info_frame, text="Gender", font=("times new roman", 12, "bold")).grid(row=2, column=0, padx=10, pady=2)
        Gender_combo = ttk.Combobox(class_student_info_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"),
                                    width=17, state="readonly")
        Gender_combo["values"] = ("M", "F")
        Gender_combo.current(0)
        Gender_combo.grid(row=2, column=1, padx=10, pady=2, sticky=W)

        # DOB
        Label(class_student_info_frame, text="DOB", font=("times new roman", 12, "bold")).grid(row=2, column=2, padx=10, pady=2)
        ttk.Entry(class_student_info_frame, textvariable=self.var_dob, width=20, font=("times new roman", 12, "bold")).grid(row=2, column=3, padx=10, pady=2, sticky=W)

        # Email
        Label(class_student_info_frame, text="Email", font=("times new roman", 12, "bold")).grid(row=3, column=0, padx=10, pady=2)
        ttk.Entry(class_student_info_frame, textvariable=self.var_email, width=20, font=("times new roman", 12, "bold")).grid(row=3, column=1, padx=10, pady=2, sticky=W)

        # Phone
        Label(class_student_info_frame, text="Phone", font=("times new roman", 12, "bold")).grid(row=3, column=2, padx=10, pady=2)
        ttk.Entry(class_student_info_frame, textvariable=self.var_phone, width=20, font=("times new roman", 12, "bold")).grid(row=3, column=3, padx=10, pady=2, sticky=W)

        # Address
        Label(class_student_info_frame, text="Address", font=("times new roman", 12, "bold")).grid(row=4, column=0, padx=10, pady=2)
        ttk.Entry(class_student_info_frame, textvariable=self.var_address, width=20, font=("times new roman", 12, "bold")).grid(row=4, column=1, padx=10, pady=2, sticky=W)

        # Teacher Name
        Label(class_student_info_frame, text="Teacher Name", font=("times new roman", 12, "bold")).grid(row=4, column=2, padx=10, pady=2)
        ttk.Entry(class_student_info_frame, textvariable=self.var_teacher, width=20, font=("times new roman", 12, "bold")).grid(row=4, column=3, padx=10, pady=2, sticky=W)

        # radio buttons
        radiobtn1 = ttk.Radiobutton(class_student_info_frame, variable=self.var1_radio1, text="Take photo sample", value="Yes")
        radiobtn1.grid(row=5, column=0)
        radiobtn2 = ttk.Radiobutton(class_student_info_frame, variable=self.var1_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1)

        # Button frames
        btn_frame = Frame(class_student_info_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=175, width=700, height=40)

        # buttons
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=10, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=1, padx=5, pady=5)

        update_btn = Button(btn_frame, text="Update", command=self.Update_Data, width=10, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2, padx=5, pady=5)

        delete_btn = Button(btn_frame, text="Delete", width=10,command=self.delete_data, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=3, padx=5, pady=5)

        reset_btn = Button(btn_frame, text="Reset",command=self.Reset_fun, width=10, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=4, padx=5, pady=5)

        take_photo_sample_btn = Button(btn_frame, text="photo sample",command=self.generate_data_set, width=10, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        take_photo_sample_btn.grid(row=0, column=5, padx=5, pady=5)

        update_photo_sample_btn = Button(btn_frame, text="update photo", width=10, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        update_photo_sample_btn.grid(row=0, column=6, padx=5, pady=5)

        # right side frame (table and search)
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Data", font=("times new roman", 14, "bold"))
        right_frame.place(x=770, y=10, width=720, height=530)

        img_right = Image.open(r"E:\Face Recognition System\Background Photos\right_frame.webp")
        img_right = img_right.resize((710, 120), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        right_lbl = Label(right_frame, image=self.photoimg_right)
        right_lbl.place(x=5, y=0, width=705, height=120)

        # Search frame
        Search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE, text="Search Frame", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=130, width=705, height=70)

        Label(Search_frame, text="Search By:", font=("times new roman", 12, "bold")).grid(row=0, column=0, padx=10, pady=2)
        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Roll No", "Phone", "Gender")
        search_combo.current(0)
        search_combo.grid(row=0, column=2, padx=2, pady=20, sticky=W)

        search_label = ttk.Entry(Search_frame, width=20, font=("times new roman", 12, "bold"))
        search_label.grid(row=0, column=3, padx=10, pady=2, sticky=W)

        search_btn = Button(Search_frame, text="Search", width=10, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=4, padx=5, pady=5)

        show_All_btn = Button(Search_frame, text="Show All", width=10, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        show_All_btn.grid(row=0, column=5, padx=5, pady=5)

        # table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=705, height=290)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        columns = ("Dept", "Course", "Year", "Semester", "Student_ID", "Name", "Division", "Roll No", "Gender", "DOB", "Email", "Phone", "Address", "Teacher", "PhotoSample")
        self.student_table = ttk.Treeview(table_frame, columns=columns, xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # headings
        for col in columns:
            self.student_table.heading(col, text=col)
            self.student_table.column(col, width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    # ----------------- Add Data -----------------
    def add_data(self):
        if self.var_dept.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_ID.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mh157974#", database="student_details")
            my_cursor = conn.cursor()
            sql = """INSERT INTO `student` (`Dept`,`Course`,`Year`,`Semester`,`Student_ID`,`Name`,`Division`,`Roll No`,`Gender`,`DOB`,`Email`,`Phone`,`Address`,`Teacher`,`PhotoSample`)
                     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            vals = (
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_ID.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var1_radio1.get()
            )
            my_cursor.execute(sql, vals)
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student Details Added Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("ERROR", f"Due to : {str(es)}", parent=self.root)

    # ----------------- Fetch Data -----------------
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mh157974#", database="student_details")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM `student`")
            data = my_cursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
            conn.close()
        except Exception as es:
            messagebox.showerror("ERROR", f"Due to : {str(es)}", parent=self.root)

    # ----------------- Get Cursor -----------------
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content.get("values", ())
        if not data:
            return
        # table order: Dept, Course, Year, Semester, Student_ID, Name, Division, Roll No, Gender, DOB, Email, Phone, Address, Teacher, PhotoSample
        self.var_dept.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_ID.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var1_radio1.set(data[14])

    # ----------------- Update Data -----------------
    def Update_Data(self):
        if self.var_dept.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_ID.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
            if update:
                conn = mysql.connector.connect(host="localhost", user="root", password="Mh157974#", database="student_details")
                my_cursor = conn.cursor()
                sql = """UPDATE `student`
                         SET `Dept`=%s, `Course`=%s, `Year`=%s, `Semester`=%s, `Name`=%s, `Division`=%s, `Roll No`=%s,
                             `Gender`=%s, `DOB`=%s, `Email`=%s, `Phone`=%s, `Address`=%s, `Teacher`=%s, `PhotoSample`=%s
                         WHERE `Student_ID`=%s"""
                vals = (
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var1_radio1.get(),
                    self.var_std_ID.get()
                )
                my_cursor.execute(sql, vals)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                self.fetch_data()
            else:
                return
        except Exception as es:
            messagebox.showerror("ERROR", f"Due to : {str(es)}", parent=self.root)

    # =========================== Delete Data =============================
    def delete_data(self):
        if self.var_std_ID.get()=="":
            messagebox.showerror("ERROR","Student ID must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete page","Do you want to delete this student",parent=self.root)
                if(delete>0):
                    conn = mysql.connector.connect(host="localhost", user="root", password="Mh157974#",database="student_details")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_ID=%s"
                    val= (self.var_std_ID.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return 
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully student details ",parent=self.root)
            except Exception as es:
                messagebox.showerror("ERROR", f"Due to : {str(es)}", parent=self.root)


    # ==================== Reset Function ===========================
    def Reset_fun(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_ID.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var1_radio1.set("")

    # ==============Generate Data set or take photo sample============================
    def generate_data_set(self):
        if self.var_dept.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_ID.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Mh157974#", database="student_details")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            my_result = my_cursor.fetchall()
            id = 0
            for x in my_result:
                id += 1
            sql = """UPDATE `student`
                         SET `Dept`=%s, `Course`=%s, `Year`=%s, `Semester`=%s, `Name`=%s, `Division`=%s, `Roll No`=%s,
                             `Gender`=%s, `DOB`=%s, `Email`=%s, `Phone`=%s, `Address`=%s, `Teacher`=%s, `PhotoSample`=%s
                         WHERE `Student_ID`=%s"""
            vals = (
                self.var_dept.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_semester.get(),
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_roll.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var1_radio1.get(),
                self.var_std_ID.get() 
            )
            my_cursor.execute(sql, vals)
            conn.commit()
            self.fetch_data()
            self.Reset_fun()
            conn.close()

            # hard to understand 
            # ========================= load predifined data on face frontal from open cv =====================
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray,1.3,5)
                # scaling factor = 1.3
                # minimum neighbour = 5

                for (x,y,w,h) in faces :
                    face_cropped = img[y:y+h,x:x+w]
                    return face_cropped
                
            # cap = cv2.VideoCapture(0)
            cap = None
            for i in range(5):
                temp_cap = cv2.VideoCapture(i)
                if temp_cap.isOpened():
                    cap = temp_cap
                    break
                
            if cap is None:
                messagebox.showerror("Error", "No camera detected")
                return

            img_id = 0

            while True:
                ret, m_frame = cap.read()
                if not ret:   # if frame not captured
                    break

                face = face_cropped(m_frame)   # call once and store result
                if face is not None:
                    img_id += 1
                    face = cv2.resize(face, (450,450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "Data/user." + str(id) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                    cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100: 
                    break


            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating Data Set Completed") 

        except Exception as es:
            messagebox.showerror("ERROR", f"Due to : {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
