import numpy as np
from scipy import stats
marks=[]
def manu():
    
    print("Memu :")
    print("A . To Enter your Subject marks :")
    print("B ./To Calculate Mean :")
    print("C./ To Calculate Mode :")
    print("D./ To calculate variance :")
    print("X./ To exit the application ")
def all_marks():
    global marks
    student_marks=int(input("Your Marks  :"))
    marks=list(map(int ,student_marks.split(",")))
    print(f"your obtaine marks : {marks}")