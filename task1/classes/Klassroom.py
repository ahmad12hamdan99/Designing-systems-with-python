
from datetime import time

class klassroom:
    '''
    this class define classroom in educational institution
    properties:
    - capacity: number of seats in the classroom
    - number: id number of the classroom
    - air_conditioner: a string value (yes/no) define if the classroom has air conditioner or not
    - activities : dictionary on activities assigned to this classroom: key:"activity name", value:[start_time,end_time]
    methods:
    - assign_activity: assign an activity to this classroom takes activity name, start time and end time as parameters
    - print: print summary of the classroom
    '''
    def __init__(self, capacity, number, air_conditioner):
        self._capacity = capacity
        self._number = number
        self._air_conditioner = air_conditioner
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
        '''
        assign an activity to classroom
        :param activity: activity name (string)
        :param start_time: start time of the activity in the form hh:mm
        :param end_time: end time of the activity in the form hh:mm
        '''
        if (start_time > time(21, 00, 00) or start_time< time(8, 00, 00))or(end_time >time(21, 00, 00) or end_time<time(8, 00, 00)):
            print("Sorry activities are allowed only during working hours from 08:00 till 21:00")
            return
        else:
            if (end_time >= start_time):
                for key in self.activities.keys():
                    if (start_time > self.activities[key][0] and start_time < self.activities[key][1]) or (end_time > self.activities[key][0] and end_time < self.activities[key][1]) or (start_time > self.activities[key][0] and end_time < self.activities[key][1])or (start_time < self.activities[key][0] and end_time > self.activities[key][1]):
                        print("sorry! the class is not available due to  overlap with another activity ")
                        return
                self.activities[activity] = [start_time, end_time]
                print("Activity added")
            else:
                print("invalid entry ")
                return


    def __str__(self):
        '''
        operator overloading of print function. print a summary of this classroom: number, capacity,air conditioner and
        a list of activities assigned to this classroom today
        :return: string
        '''
        str = ""
        str += f'class room number {self.number}, capacity {self.capacity}, air conditioner {self.air_conditioner}\n'
        if len(self.activities) !=0:
            str += "list of activities today:\n"
            for key in self.activities:
                str += f'{key} : from {(self.activities[key][0].hour):02d}:{(self.activities[key][0].minute):02d} to {(self.activities[key][1].hour):02d}:{(self.activities[key][1].minute):02d}\n'
            return str
        else:
            str += "No activities assigned to this class room"
            return str

