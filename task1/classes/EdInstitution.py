
from datetime import time, datetime
import os.path
import pickle


from classes.Klassroom import klassroom
from classes.LectureAuditorium import LectureAuditorium


class EdInstitution:
    '''
    this class define educational institution
    properties:
    - name: name of institution
    - classrooms: list of classrooms in the institution
    - lectureAuditoriums: list of auditoriums in the institution
    methods:
    - get_classroom: get classroom from the classrooms list by number
    - add_classroom: add classroom to the classrooms list
    - remove_classroom: remove classroom from the classrooms list
    - get_auditorium: get auditorium from the auditoriums list by number
    - add_auditorium: add auditorium to the auditoriums list
    - remove_auditorium: remove auditorium from the auditoriums list
    - saveToFile: save the institution object to pickle file
    - restoreFromFile: restore institution object from pickle file
    - print: print summary of the institution
    '''
    def __init__(self, name):
        self._name = name
        self.classrooms = []
        self.lectureAuditoriums = []

    @property
    def name(self):
        return self._name

    # a setter function
    @name.setter
    def name(self, name):
        self._name = name


    def get_classroom(self, number):
        '''
        get classroom from the classrooms list by number
        :param number: the number of the classroom
        :return: klassroom object
        '''
        for classR in self.classrooms:
            if classR.number == number:
                return classR
        print("there is no classroom with the specified number")
        return None

    def add_classroom(self, capacity, number, air_conditioner):
        '''
        add new classroom to the classrooms list in the institution
        :param capacity: capacity of the classroom
        :param number: the number of the classroom
        :param air_conditioner: a string value (yes/no) define if the classroom has air conditioner or not
        '''
        for classR in self.classrooms:
            if classR.number == number:
                print("there is a class room with same number already. try another number")
                return
        class_room = klassroom(capacity, number, air_conditioner)
        self.classrooms.append(class_room)
        print(f'Classroom successfully added to {self.name}')

    def remove_classroom(self, number):
        '''
        remove classroom from classrooms list in the institution
        :param number: the number of the classroom
        '''
        for classR in self.classrooms:
            if classR.number == number:
                self.classrooms.remove(classR)
                print(f'Classroom  successfully removed from {self.name}')
                return
        print("there is no classroom with the specified number")

    def get_auditorium(self, number):
        '''
        get auditorium from the auditoriums list by number
        :param number: the number of the auditorium
        :return: Auditorium object
        '''
        for auditoriumR in self.lectureAuditoriums:
            if auditoriumR.number == number:
                return auditoriumR
        print("there is no auditorium with the specified number")
        return None

    def add_auditorium(self, capacity, number, air_conditioner):
        '''
        add new auditorium to the auditoriums list in the institution
        :param capacity: capacity of the auditorium
        :param number: the number of the auditorium
        :param air_conditioner: a string value (yes/no) define if the auditorium has air conditioner or not
        '''
        for auditoriumR in self.lectureAuditoriums:
            if auditoriumR.number == number:
                print("there is a auditorium with same number already. try another number")
                return
        auditorium = LectureAuditorium(capacity, number, air_conditioner)
        self.lectureAuditoriums.append(auditorium)
        print(f'Auditorium successfully added to {self.name}')

    def remove_auditorium(self, number):
        '''
        remove auditorium from auditoriums list in the institution
        :param number: the number of the auditorium
        '''
        for auditoriumR in self.lectureAuditoriums:
            if auditoriumR.number == number:
                self.lectureAuditoriums.remove(auditoriumR)
                print(f'Auditorium  successfully removed from {self.name}')
                return
        print("there is no auditorium with the specified number")

    def __str__(self):
        '''
        operator overloading of print function. print a summary of this institution: name, number of classrooms
        number of auditoriums and the number if available classrooms and auditoriums right now
        :return: string
        '''
        avaliable_classrooms = 0
        avaliable_auditoriums = 0
        str=""
        str += self.name+"\n"
        str += f'\t Classrooms: {len(self.classrooms)}\n'
        str += f'\t Auditorium(s): {len(self.lectureAuditoriums)}\n'
        now = datetime.now()
        flag1 = 1
        flag2 = 1
        if now.time()<time(8,00,00) or now.time()>time(21,00,00):
            avaliable_classrooms=0
            avaliable_auditoriums=0
        else:
            for classR in self.classrooms:
                if len(classR.activities) == 0:
                    avaliable_classrooms += 1
                else:
                    for key in classR.activities:
                        if now.time() > classR.activities[key][0] and now.time() < classR.activities[key][1]:
                            flag1 = 0
                    if flag1 == 1:
                        avaliable_classrooms += 1
                        flag1 = 0
            for auditoriumR in self.lectureAuditoriums:
                if len(auditoriumR.activities) == 0:
                    avaliable_auditoriums += 1
                else:
                    for key in auditoriumR.activities:
                        if now.time() > auditoriumR.activities[key][0] and now.time() < auditoriumR.activities[key][1]:
                            flag2 = 0
                    if flag2 == 1:
                        avaliable_auditoriums += 1
                        flag2 = 0

        str+=f'\t Status for today (now) : {avaliable_classrooms} available classroom(s) and {avaliable_auditoriums} available auditoriums(s))'
        return str

    def saveToFile(self):
        '''
        save institution object to pickle file
        '''
        with open(f'{self.name}.pkl', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def restoreFromFile(self):
        '''
        restore institution object to pickle file
        '''

        def restoreFromFile(self):
            '''
            restore institution object to pickle file
            '''
            if os.path.exists(f'{self.name}.pkl'):
                try:
                    with open(f'{self.name}.pkl', 'rb') as f:
                        R = pickle.load(f)
                        return R
                except Exception as e:
                    print(e)
