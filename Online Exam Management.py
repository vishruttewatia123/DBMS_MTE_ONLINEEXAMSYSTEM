#Project on Online Exam Management
#--------------------------------------------------------------------------------
#MODULE : Online Exam Management
import Database
import Menulib
import Student
import Subject
import Exam

Database.DatabaseCreate()
Database.TablesCreate()


while True:
    print("\t\t\t Online Exam Management\n")
    print("=====================================================================")
    print("1. Student Management")
    print("2. Subject Management")
    print("3. Exam Management")
    print("4. Exit")
    choice = int(input("Enter Choice between 1 to 4 -------> : "))
    if choice == 1:
        Menulib.MenuStudent()
    elif choice == 2:
        Menulib.MenuSubject()
    elif choice == 3:
        Menulib.MenuExam()
    elif choice == 4:
    	break
    else:
        print("Wrong Choice.....Enter Your Choice again")
        x = input("Press any key to continue")
