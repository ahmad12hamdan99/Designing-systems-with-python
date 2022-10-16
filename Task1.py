from datetime import datetime
from datetime import time
import json
import pickle

class klassroom:
    def __init__(self, capacity, number, air_conditioner):
        self.capacity = capacity
        self.number = number
        self.air_conditioner = air_conditioner
        self.activities = dict()

    @property
    def capacity(self):
        return self._capacity

    # a setter function
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def number(self):
        return self._number

    # a setter function
    @number.setter
    def number(self, number):
        self._number = number

    @property
    def air_conditioner(self):
        return self._air_conditioner

    # a setter function
    @air_conditioner.setter
    def air_conditioner(self, air_conditioner):
        self._air_conditioner = air_conditioner

    # activities =dict()

    def assign_activity(self, activity, start_time, end_time):
        if (end_time >= start_time):
            for key in self.activities.keys():
                if (start_time > self.activities[key][0] and start_time < self.activities[key][1]) or (end_time > self.activities[key][0] and end_time < self.activities[key][1]):
                    print("sorry! the class is not available due to  overlap with another activity ")
                    return
            self.activities[activity] = [start_time, end_time]
            print("Activity added")

        else:
            print("invalid entry ")
            return

    def __str__(self):
        str=""
        str+=f'class room number {self.number}, capacity {self.capacity}, air conditioner {self.air_conditioner}\n'
        str+="list of activities today:\n"
        for key in self.activities:
            str+=f'{key} : from {(self.activities[key][0].hour):02d}:{(self.activities[key][0].minute):02d} to {(self.activities[key][1].hour):02d}:{(self.activities[key][1].minute):02d}\n'
        return str


class LectureAuditorium:
    def __init__(self, capacity, number, air_conditioner):
        self.capacity = capacity
        self.number = number
        self.air_conditioner = air_conditioner
        self.activities = dict()

    @property
    def capacity(self):
        return self._capacity

    # a setter function
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def number(self):
        return self._number

    # a setter function
    @number.setter
    def number(self, number):
        self._number = number

    @property
    def air_conditioner(self):
        return self._air_conditioner

    # a setter function
    @air_conditioner.setter
    def air_conditioner(self, air_conditioner):
        self._air_conditioner = air_conditioner

    def assign_activity(self, activity, start_time, end_time):
        if (end_time >= start_time):
            for key, value in self.activities:
                if (start_time > self.activities[key][0] and start_time < self.activities[key][1]) or (end_time > self.activities[key][0] and end_time < self.activities[key][1]):
                    print("sorry! the auditorium is not available due to  overlap with another activity ")
                    return

            self.activities[activity] = [start_time, end_time]

            print("Activity added")
        else:
            print("invalid entry ")
            return

    def __str__(self):
        str=""
        str+=f'class room number {self.number}, capacity {self.capacity}, air conditioner {self.air_conditioner}\n'
        str+="list of activities today:\n"
        for key in self.activities:
            str+=f'{key} : from {(self.activities[key][0].hour):02d}:{(self.activities[key][0].minute):02d} to {(self.activities[key][1].hour):02d}:{(self.activities[key][1].minute):02d}\n'
        return str


class EdInstitution:
    def __init__(self, name):
        self.name = name
        self.classrooms = []
        self.LectureAuditoriums = []

    @property
    def name(self):
        return self._name

    # a setter function
    @name.setter
    def name(self, name):
        self._name = name

    def get_classroom(self, number):
        for classR in self.classrooms:
            if classR.number == number:
                return classR
        print("there is no classroom with the specified number")
        return None

    def add_classroom(self, capacity, number, air_conditioner):
        for classR in self.classrooms:
            if classR.number == number:
                print("there is a class room with same number already. try another number")
                return
        class_room = klassroom(capacity, number, air_conditioner)
        self.classrooms.append(class_room)
        print(f'Classroom successfully added to {self.name}')

    def remove_classroom(self, number):
        for classR in self.classrooms:
            if classR.number == number:
                self.classrooms.remove(classR)
                print(f'Classroom  successfully removed from {self.name}')
                return
        print("there is no classroom with the specified number")

    def get_auditorium(self, number):
        for auditoriumR in self.LectureAuditoriums:
            if auditoriumR.number == number:
                return auditoriumR
        print("there is no auditorium with the specified number")
        return None

    def add_auditorium(self, capacity, number, air_conditioner):
        for auditoriumR in self.LectureAuditoriums:
            if auditoriumR.number == number:
                print("there is a auditorium with same number already. try another number")
                return
        auditorium = LectureAuditorium(capacity, number, air_conditioner)
        self.LectureAuditoriums.append(auditorium)
        print(f'Auditorium successfully added to {self.name}')

    def remove_auditorium(self, number):
        for auditoriumR in self.LectureAuditoriums:
            if auditoriumR.number == number:
                self.LectureAuditoriums.remove(auditoriumR)
                print(f'Auditorium  successfully removed from {self.name}')
                return
        print("there is no auditorium with the specified number")

    def __str__(self):
        avaliable_classrooms = 0
        avaliable_auditoriums = 0
        str=""
        #print(self.name)
        #print(f'\t Classrooms: {len(self.classrooms)}')
        #print(f'\t Auditorium(s): {len(self.LectureAuditoriums)}')
        str+=self.name+"\n"
        str+=f'\t Classrooms: {len(self.classrooms)}\n'
        str+=f'\t Auditorium(s): {len(self.LectureAuditoriums)}\n'

        now = datetime.now()
        flag1 = 1
        flag2 = 1
        for classR in self.classrooms:
            #print(classR.activities)
            if len(classR.activities) == 0:
                avaliable_classrooms += 1
            else:
                for key in classR.activities:
                    #print(now.hour)
                    #print(classR.activities[key][0].hour)
                    #print(classR.activities[key][1].hour)
                    if now.hour > classR.activities[key][0].hour and now.hour < classR.activities[key][1].hour:
                        flag1 = 0
                if flag1 == 1:
                    avaliable_classrooms += 1
                    flag1 = 0
        for auditoriumR in self.LectureAuditoriums:
            if len(auditoriumR.activities) == 0:
                avaliable_auditoriums += 1
            else:
                for key in auditoriumR.activities:
                    if now.hour > auditoriumR.activities[key][0].hour and now.hour < auditoriumR.activities[key][1].hour:
                        flag2 = 0
                if flag2 == 1:
                    avaliable_auditoriums += 1
                    flag2 = 0

        #print(f'\t Status for today (now) : {avaliable_classrooms} available classroom(s) and {avaliable_auditoriums} available auditoriums(s))')
        str+=f'\t Status for today (now) : {avaliable_classrooms} available classroom(s) and {avaliable_auditoriums} available auditoriums(s))'
        return str

    def saveToFile(self):
        #with open(f'{self.name}.json', 'w') as f:
        #   json.dump(self.__dict__, f)
        with open(f'{self.name}.pkl', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def restoreFromFile(self):
        with open(f'{self.name}.pkl', 'rb') as f:
            R= pickle.load(f)
            self=R
            #print(self.name)



universities_list=[]
new_institution = EdInstitution("Innppolis University")
universities_list.append(new_institution)

new_institution1 = EdInstitution("Kazan Federal University")
universities_list.append(new_institution1)

#print(universities_list[0])
#print(universities_list[1])

run=1
chosen_university=""
while(run):
    print("Choose one operation from below :")
    print("\t 1 : Add classroom or Auditorium to institution:")
    print("\t 2 : Print institution summary :")
    print("\t 3 : Assign activity to classroom :")
    print("\t 4 : Assign activity to LectureAuditorium :")
    print("\t 5 : Exit program")


    code=input()
    if not code.isdigit():
        print("Invalid Input")
        continue
    else:
        code=int(code)

    if code==1:
        print("Enter institution name :")
        universitiy_name=input()
        for u in universities_list:
            if u.name==universitiy_name:
                chosen_university=u
                #print(chosen_university.name)
                break
        print("No such a university in the database")
        continue
        loop_to_enter_room=1
        while(loop_to_enter_room==1):
            print("Enter(classroom - 1 or Auditorium - 2):")
            c = int(input())
            if c==1:
                print("Enter (capacity, number, air conditioner- yes/no):")
                capacity, number, air_conditioner = input().split()
                chosen_university.add_classroom(capacity,number,air_conditioner)
            else:
                print("Enter (capacity, number, air conditioner- yes/no):")
                capacity, number, air_conditioner = input().split()
                chosen_university.add_auditorium(capacity, number, air_conditioner)
            print("Add another Classroom or Auditorium to Innopolis University? (yes/no)")
            decision=input()
            if decision=="no":
                loop_to_enter_room=0
            else:
                loop_to_enter_room=1
    elif code==2:
        print("Enter institution name :")
        universitiy_name = input()
        for u in universities_list:
            if u.name == universitiy_name:
                chosen_university = u
                break
        #print(u)
    elif code==3:
        print("Choose classroom number:")
        classroom_n=(input())
        chosen_classroom=chosen_university.get_classroom(classroom_n)
        print(chosen_classroom.number)
        loop_to_enter_activity=1
        while(loop_to_enter_activity==1):
            print("Enter activity name, start time (hh:mm) and end time (hh:mm): ")
            activity_name, start_time, end_time = input().split()
            start_time_l=start_time.split(':')
            end_time_l=start_time.split(':')

            s = time(int(start_time_l[0]),int(start_time_l[1]), 00)
            e = time(int(end_time_l[0]),int(end_time_l[1]), 00)
            chosen_classroom.assign_activity(activity_name, s, e)
            print("Add another activity ? (yes/no)")
            decision = input()
            if decision == "no":
                loop_to_enter_activity = 0
            else:
                loop_to_enter_activity = 1
    elif code ==4:
        print("Choose auditorium number:")
        auditorium_n = (input())
        chosen_auditorium = chosen_university.get_auditorium(auditorium_n)
        print(chosen_auditorium.number)
        loop_to_enter_activity = 1
        while (loop_to_enter_activity == 1):
            print("Enter activity name, start time (hh:mm) and end time (hh:mm): ")
            activity_name, start_time, end_time = input().split()
            start_time_l = start_time.split(':')
            end_time_l = start_time.split(':')

            s = time(int(start_time_l[0]), int(start_time_l[1]), 00)
            e = time(int(end_time_l[0]), int(end_time_l[1]), 00)
            chosen_auditorium.assign_activity(activity_name, s, e)
            print("Add another activity ? (yes/no)")
            decision = input()
            if decision == "no":
                loop_to_enter_activity = 0
            else:
                loop_to_enter_activity = 1
    elif code==5:
        run = 0
        for uni in universities_list:
            print(uni)

