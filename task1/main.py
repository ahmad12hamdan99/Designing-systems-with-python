from datetime import time
import os.path
import re

from classes.EdInstitution import EdInstitution
from utils.helper import validate_input

if __name__ == "__main__":

    # define a list of institutions
    institutions_list=[]
    new_institution = EdInstitution("Innopolis University")
    institutions_list.append(new_institution)

    new_institution1 = EdInstitution("Kazan Federal University")
    institutions_list.append(new_institution1)

    # restore institutions data
    for u in institutions_list:
        u.restoreFromFile()


    run=1
    chosen_institution=""
    while(run):
        print("\nChoose one operation from below :")
        print("\t 1 : Add classroom or Auditorium to institution:")
        print("\t 2 : Print institution summary :")
        print("\t 3 : Assign activity to classroom :")
        print("\t 4 : Assign activity to LectureAuditorium :")
        print("\t 5 : Exit program")

        code=input()
        print()
        if validate_input("digit1to5",code):
            code=int(code)
        else:
            continue

        if code==1:
            print("Enter institution name :")
            chosen_institution=None
            institutions_name=input()
            print()
            for u in institutions_list:
                if u.name.lower() == institutions_name.lower():
                    chosen_institution=u
                    break
            if chosen_institution==None:
                print("No such a university in the database")
                continue
            print("Enter(classroom - 1 or Auditorium - 2):")
            c = input()
            print()
            while not validate_input("choice1or2",c):
                c=input()
                print()
            c=int(c)

            if c==1:
                loop_to_enter_classroom = 1
                while (loop_to_enter_classroom == 1):
                    print("Enter (capacity, number, air conditioner- yes/no):")
                    capacity, number, air_conditioner = input().split()
                    print()
                    while not capacity.isdigit() or not number.isdigit() or not validate_input("decision",air_conditioner):
                        if not capacity.isdigit():
                            print("capacity should be integer")
                        if not number.isdigit():
                            print("classroom number should be integer")
                        capacity, number, air_conditioner = input().split()
                        print()
                    chosen_institution.add_classroom(capacity,number,air_conditioner)
                    print(f'Add another classroom {chosen_institution.name}? (yes/no)')

                    decision = input()
                    print()
                    while not validate_input("decision", decision):
                        decision = input()
                        print()

                    if decision == "no":
                        loop_to_enter_classroom = 0
                    else:
                        loop_to_enter_classroom = 1
            else:
                loop_to_enter_auditorium = 1
                while (loop_to_enter_auditorium == 1):
                    print("Enter (capacity, number, air conditioner- yes/no):")
                    capacity, number, air_conditioner = input().split()
                    print()
                    while not capacity.isdigit() or not number.isdigit() or not validate_input("decision",air_conditioner):
                        if not capacity.isdigit():
                            print("capacity should be integer")
                        if not number.isdigit():
                            print("auditorium number should be integer")
                        capacity, number, air_conditioner = input().split()
                        print()
                    chosen_institution.add_auditorium(capacity, number, air_conditioner)
                    print(f'Add another auditorium {chosen_institution.name}? (yes/no)')
                    decision=input()
                    print()
                    while not validate_input("decision", decision):
                        decision = input()
                        print()

                    if decision=="no":
                        loop_to_enter_auditorium=0
                    else:
                        loop_to_enter_auditorium=1
        elif code==2:
            print("Enter institution name :")
            universitiy_name = input()
            print()
            for u in institutions_list:
                if u.name.lower() == universitiy_name.lower():
                    chosen_institution = u
                    break
            print(chosen_institution)
        elif code==3:
            print("Choose classroom number:")
            classroom_n=(input())
            print()
            chosen_classroom=chosen_institution.get_classroom(classroom_n)
            if chosen_classroom != None:
                loop_to_enter_activity=1
                while(loop_to_enter_activity==1):
                    print("Enter activity name, start time (hh:mm) and end time (hh:mm): ")
                    activity_name, start_time, end_time = input().split()
                    print()
                    if not validate_input("time",start_time) or not validate_input("time",end_time):
                        activity_name, start_time, end_time = input().split()
                        print()

                    start_time_l=start_time.split(':')
                    end_time_l=start_time.split(':')

                    s = time(int(start_time_l[0]),int(start_time_l[1]), 00)
                    e = time(int(end_time_l[0]),int(end_time_l[1]), 00)
                    chosen_classroom.assign_activity(activity_name, s, e)
                    print("Add another activity ? (yes/no)")
                    decision = input()
                    print()
                    if decision == "no":
                        loop_to_enter_activity = 0
                        print(chosen_classroom)
                    else:
                        loop_to_enter_activity = 1
        elif code ==4:
            print("Choose auditorium number:")
            auditorium_n = (input())
            print()
            chosen_auditorium = chosen_institution.get_auditorium(auditorium_n)
            if chosen_auditorium != None:
                loop_to_enter_activity = 1
                while (loop_to_enter_activity == 1):
                    print("Enter activity name, start time (hh:mm) and end time (hh:mm): ")
                    activity_name, start_time, end_time = input().split()
                    print()
                    start_time_l = start_time.split(':')
                    end_time_l = start_time.split(':')

                    s = time(int(start_time_l[0]), int(start_time_l[1]), 00)
                    e = time(int(end_time_l[0]), int(end_time_l[1]), 00)
                    chosen_auditorium.assign_activity(activity_name, s, e)
                    print("Add another activity ? (yes/no)")
                    decision = input()
                    print()
                    if decision == "no":
                        loop_to_enter_activity = 0
                        print(chosen_auditorium)
                    else:
                        loop_to_enter_activity = 1

        elif code==5:
            print("Are you sure you want to exit")
            decision=input()
            print()
            while not validate_input("decision", decision):
                decision = input()
                print()
            if decision=="yes":
                run = 0
                for uni in institutions_list:
                    print(uni)
                    print()
                    uni.saveToFile()
            else:
                continue
