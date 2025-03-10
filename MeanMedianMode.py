###############using python library
import numpy as np
from scipy import stats
marks=[]
def menu():
    
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
def calculate_mean():
    if not marks:
        print("First enter ypur marks ")
        return
    print(f"mean :{np.mean(marks)}")
def calculate_mode():
    if not marks:
        print("enter your marks first :")
        return
    print(f"mode :{np.mode(marks)}")    
def calculate_variance():
    if not marks:
        print("enter your marks first :")
        return
    print(f"mode :{np.var(marks)}")   
while True:
    menu()
    choice=input("Enter your choice :")
    if choice=='A':
        all_marks()
    elif choice=='A':
        calculate_mean()
    elif choice=='A':
        calculate_mode()
    elif choice=='A':
        calculate_variance() 
        break
    elif choice=='X':
        print("exit the application :")
    else:
        print("enter mraks first !")
#################        
        

