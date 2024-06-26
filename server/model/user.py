from pydantic import BaseModel
from typing import Optional, Dict
import persistent

import datetime

class certification(persistent.Persistent):
      courseName: str
      teacherName: str
      Date: str
      userName: str

# abstract class User and two clases, student and teacher, inherit from it
class User(persistent.Persistent):
      def __init__(self, username, name, password, role):
            self.username = username
            self.name = name
            self.password = password
            self.role = role

      def edit_details(self, name, password):
            self.name = name

            self.password = password

class Student(User, persistent.Persistent):
      def __init__(self, username, name, password, role,  enrolledCourseList):
            super().__init__(username, name, password, role)
            # store the courseName, teacherName in the certification
            self.certificationList = [] # [certification1, certification2, certification3]
            self.enrolledCourseList = enrolledCourseList

      def enroll_course(self, courseCode):
            self.enrolledCourseList.append(courseCode)

      def unenroll_course(self, courseCode):
            self.enrolledCourseList.remove(courseCode)

      def checkCourse_ByCourseCode(self, courseCode):
            if courseCode in self.enrolledCourseList:
                  return True
            else:
                  return False
            
      # add the courseName, teacherName, Date to the certification
      def add_certification(self, courseName, teacherName, userName):

            today_Date = datetime.datetime.today()
            formatted_date = today_Date.strftime("%B %d, %Y")
            certification = {
                  "courseName": courseName, 
                  "teacherName": teacherName, 
                  "Date": str(formatted_date),
                  "userName": self.name
                  }

            self.certificationList.append(certification)
            self.print_details()

      def print_details(self):
            print("Username:", self.name)
            print("Role:", self.role)
            print("Enrolled Courses:", self.enrolledCourseList)
            print("Certification List:", self.certificationList)

      

class Teacher(User, persistent.Persistent):
      def __init__(self, username, name, password, role,  ownedCourseList):
            super().__init__(username, name, password, role)

            self.ownedCourseList = ownedCourseList          # List of courses by courseCode
      # check course by courseCode
      def checkCourse_ByCourseCode(self, courseCode):
            if courseCode in self.ownedCourseList:
                  return True
            else:
                  return False

      def print_details(self):
            print("Username:", self.name)
            print("Role:", self.role)
            print("Owned Courses:", self.ownedCourseList)