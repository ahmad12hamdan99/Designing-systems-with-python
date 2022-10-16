import datetime as dt
import numpy as np

#_______________System Class____________________
class System:
    def __init__(self):
        self.users = {}
    
    def add_user(self,user):
        self.users['user.id'] = user
    
   
def mode(lst):
    d = {}
    for a in lst:
        if not a in d:
            d[a]=1
        else:
            d[a]+=1
    return [k for k,v in d.items() if v==max(d.values())]

#_____________User Class_________________________
class User:
    def __init__(self,id):
        self.id = id
        self.sessions = []
        self.devices = []
        self.timeStamps = []
        self.user_measurements = {}
        self.user_measurements
        self.super = False
        
    def add_session(self,new_session):
        self.sessions.append(new_session) 
        self.user_measurements[new_session.id] = {}
        self.user_measurements[new_session.id]['DF']=[]
        self.user_measurements[new_session.id]['FPS']=[]
        self.user_measurements[new_session.id]['bitrate']=[]
        self.user_measurements[new_session.id]['RTT']=[]
        
    def add_device(self,new_device):
        self.devices.append(new_device)
        
    def add_timeStamp(self,timeStamp):
        self.timeStamps.append(timeStamp)
        
        
    def add_measurements(self,session_id,DF,FPS,bitrate,RTT):
        self.user_measurements[session_id]['DF'].append(DF)
        self.user_measurements[session_id]['FPS'].append(FPS)
        self.user_measurements[session_id]['bitrate'].append(bitrate)
        self.user_measurements[session_id]['RTT'].append(RTT)
        
    def update_sessions_info(self):
        ST = []
        for s in self.sessions:
            ST.append(s.spent_time)
        self.avg_time_per_session = np.mean(ST)
        
    def update_devices_info(self):
        self.most_freq_used_device = mode(self.devices)[0]
        

#______________________Session Class___________________________
class Session:
    def __init__(self,id,timeStamp):
        self.id = id
        date_time = dt.datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S')
        self.start_time_stamp = date_time
        self.start_date = date_time.date()
        self.start_day = date_time.timetuple()[2]
        self.spent_time = 0
        sTime = date_time.timetuple()
        self.start_time = sTime[3:6]
        self.end_time_stamp = None
        
    def add_end_time(self,timeStamp):
        date_time = dt.datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S')
        self.end_time_stamp = date_time
        
        
    def update_session_time(self,timeStamp):
        date_time = dt.datetime.strptime(timeStamp, '%Y-%m-%d %H:%M:%S')
        sTime = date_time.timetuple()
        current_time = sTime[3:6]
        current_h = current_time[0]
        start_h = self.start_time[0]
        diff_h_min = (current_h-start_h)*60
        current_min = current_time[1]
        start_min = self.start_time[1]
        diff_min = (current_min-start_min)
        current_s = current_time[2]
        start_s = self.start_time[2]
        diff_s_min = (current_s-start_s)/60
        self.spent_time = diff_h_min + diff_min + diff_s_min
        if self.end_time_stamp==None:
            self.end_time_stamp = date_time
        
#______________________Logger Class____________________________

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class Logger:
    def __init__(self):
        self.users_summaries = {}
        
    
    def update_users_summaries(self,user,isNew,stats_calculator):
        if isNew:
            self.users_summaries[user.id] = {}
         
            
            
            
        self.users_summaries[user.id]['session_numbers'] = len(user.sessions)
        self.users_summaries[user.id]['date_of_first_session'] = user.sessions[0].start_date
        self.users_summaries[user.id]['date_of_most_rescent_session'] = user.sessions[-1].start_date
        user = stats_calculator.find_avg_time_per_session(user)
        self.users_summaries[user.id]['avg_spent_time_per_session'] = user.avg_time_per_session
        self.users_summaries[user.id]['most_freq_used_device'] = user.most_freq_used_device
        self.users_summaries[user.id]['devices_used'] = user.devices
        user = stats_calculator.find_avg_DF(user)
        user = stats_calculator.find_avg_FPS(user)
        user = stats_calculator.find_avg_bitrate(user)
        user = stats_calculator.find_avg_RTT(user)
        self.users_summaries[user.id]['avg_DF'] = user.avg_DF
        self.users_summaries[user.id]['avg_FPS'] = user.avg_FPS
        self.users_summaries[user.id]['avg_bitrate'] = user.avg_bitrate
        self.users_summaries[user.id]['avg_RTT'] = user.avg_RTT
        self.users_summaries[user.id]['total_num_bad_sessions'] = 0 # to found by ML model
        user = stats_calculator.determine_super_user(user)
        self.users_summaries[user.id]['super'] = user.super
        user.next_sess_est_time = stats_calculator.estimate_next_session_time(user)
        self.users_summaries[user.id]['next_sess_est_time'] = user.next_sess_est_time
        return user
        
        
class Stats_Calculator:
    
    def find_avg_DF(self,user):
        arr = np.array([])
        for sess in user.sessions:
            df = user.user_measurements[sess.id]['DF']
            f = [float(d) for d in df]
            arr = np.concatenate((arr,np.array(f)),axis=0)
        user.avg_DF = np.mean(arr)

        return user
    
    def find_avg_FPS(self,user):
        arr = np.array([])
        for sess in user.sessions:
            fps = user.user_measurements[sess.id]['FPS']
            f = [float(d) for d in fps]
            arr = np.concatenate((arr,np.array(f)),axis=0)
        user.avg_FPS = np.mean(arr)
        return user
    
    def find_avg_bitrate(self,user):
        arr = np.array([])
        for sess in user.sessions:
            br = user.user_measurements[sess.id]['bitrate']
            f = [float(d) for d in br]
            arr = np.concatenate((arr,np.array(f)),axis=0)
        user.avg_bitrate = np.mean(arr)
        return user
    
    def find_avg_RTT(self,user):
        arr = np.array([])
        for sess in user.sessions:
            rtt = user.user_measurements[sess.id]['RTT']
            f = [float(d) for d in rtt]
            arr = np.concatenate((arr,np.array(f)),axis=0)
        user.avg_RTT = np.mean(arr)
        return user
    
    def find_avg_time_per_session(self,user):

            spent_times = []
            for sess in user.sessions:
                spent_times.append(sess.spent_time)
            
            user.avg_time_per_session = np.mean(spent_times)
            return user
        
    def estimate_next_session_time(self,user):

            spent_times = []
            for sess in user.sessions:
                spent_times.append(sess.spent_time)
            
            
            return np.mean(spent_times)
        
    def determine_super_user(self,user):
        if user.super:
            return user
        else:
            start_day = user.sessions[0].start_time_stamp.timetuple()[2]
            spent_time = 0
            for sess in user.sessions:
                spent_time = spent_time + sess.spent_time
                if spent_time>60:
                    end_day = sess.end_time_stamp.timetuple()[2]
                    period_per_days = end_day - start_day
                    if period_per_days <= 7:
                        user.super = True
            return user
    
#_______________________ML Class____________________________________________

# class Predict_Stream_Quality:
#     def __init__(self,)
            
            
        
        
      
        
        