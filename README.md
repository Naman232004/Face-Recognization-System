# 🎓 Face Recognition Attendance System

## 📌 Project Overview

The Face Recognition Attendance System is a desktop-based application developed using Python, Tkinter, OpenCV, and MySQL.  
It automatically identifies students using facial recognition and marks their attendance without manual intervention.

This system reduces manual work, prevents proxy attendance, and improves accuracy.

---

## 🚀 Features

- Student registration system  
- Automatic face data capture using webcam  
- Face dataset generation  
- Face training using LBPH algorithm  
- Real-time face recognition  
- Automatic attendance marking  
- Attendance stored in CSV file  
- MySQL database integration  
- User-friendly GUI using Tkinter  

---

## 🧠 Technologies Used

### Programming Language
- Python 3.x

### Libraries
- Tkinter  
- OpenCV  
- Pillow  
- NumPy  
- MySQL Connector  
- OS  
- DateTime  

### Database
- MySQL

---

## 📂 Project Structure

Face-Recognition-System/
│
├── Background Photos/
├── Data/
│   └── user.id.image.jpg
│
├── attendance.csv
├── classifier.xml
├── haarcascade_frontalface_default.xml
│
├── main.py
├── student_details.py
├── train.py
├── face_recognization.py
├── attendance.py
│
└── README.md

---

## ⚙️ System Workflow

1. Register student details  
2. Capture face images  
3. Train face dataset  
4. Detect face in real time  
5. Mark attendance automatically  

---

## 🧪 Face Recognition Algorithm

- LBPH (Local Binary Pattern Histogram)
- Fast and accurate for real-time applications

---

## 🗃️ Database Setup

### Database Name
student_details

### Table Name
student

### Required Columns
- Dept
- Course
- Year
- Semester
- Student_ID
- Name
- Division
- Roll No
- Gender
- DOB
- Email
- Phone
- Address
- Teacher
- PhotoSample

---

## ▶️ How to Run the Project

### Install required libraries

pip install opencv-python  
pip install opencv-contrib-python  
pip install pillow  
pip install mysql-connector-python  
pip install numpy  

---

### Create MySQL Database

CREATE DATABASE student_details;

USE student_details;

CREATE TABLE student (
  Dept VARCHAR(50),
  Course VARCHAR(50),
  Year VARCHAR(50),
  Semester VARCHAR(50),
  Student_ID INT PRIMARY KEY,
  Name VARCHAR(100),
  Division VARCHAR(10),
  `Roll No` VARCHAR(20),
  Gender VARCHAR(10),
  DOB VARCHAR(20),
  Email VARCHAR(100),
  Phone VARCHAR(20),
  Address VARCHAR(255),
  Teacher VARCHAR(100),
  PhotoSample VARCHAR(20)
);

---

### Run Application

python main.py

---

## 📊 Output

- Real-time face recognition
- Attendance automatically saved in CSV file
- Date and time recorded

---

## 🚧 Future Enhancements

- Cloud database integration  
- Admin login system  
- Mobile application  
- Attendance analytics dashboard  

---

## 👨‍💻 Developed By

Naman Lalwani  
B.E. Electronics & Telecommunication Engineering  
  

---

## 📜 License

This project is for educational purposes only.
