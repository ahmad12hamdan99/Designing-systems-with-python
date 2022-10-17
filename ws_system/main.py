import classes
import csv
import datetime as dt
import copy
from utils import parser as up


from data_loader import DriveAPI




functions = [up.base_case, up.get_status_parser, up.print_user_summary_parser, 
            up.predict_duration_parser, up.fetch_update_parser, up.get_top5_parser, up.exit_prog_parser]

S = classes.System()
logger = classes.Logger()
stats_calculator = classes.Stats_Calculator()
    ############################

def p1():
    obj = DriveAPI()

    obj.FileDownload('2022_09_01', '2022_09_02')   
    
def p2():
    with open("./raw_2022_09_01.csv", 'r') as file:
        csvreader = csv.reader(file)
        c = 0
        prev_user_id = " "
        prev_session_id = " "
        prev_device = " "
        first_id = ' '
        prev_session = None
        #print(csvreader)   
        for row in csvreader:
            if row[0]=="client_user_id":
                continue 
            
            #print(row)
                
            new_user_data = row
            time_stamp = new_user_data[-2]     
            if prev_user_id != new_user_data[0]:
                user_id = new_user_data[0]
                user = classes.User(user_id)
                isNew = True
                S.add_user(user,time_stamp)
                # if c==100000:
                #     first_id = user_id
                # else:
                #     first_id = first_id
                    
                    
                
            if prev_session_id != new_user_data[1]:
                if prev_session_id != " ":
                    new_session.add_end_time(time_stamp)
                user_session_id = new_user_data[1]
                new_session  = classes.Session(user_session_id,time_stamp)
                user.add_session(new_session) 
                S.add_session(new_session)
            else:
                new_session.update_session_time(time_stamp)
                
            
            new_device = new_user_data[-1]
            if new_device != prev_device or isNew:
                user.add_device(new_device)
                user.update_devices_info()
                
                #print(row)
            user.add_timeStamp(time_stamp)
            
                
                # user measurements
            dropped_frames = new_user_data[2]
            FPS = new_user_data[3]
            bitrate = new_user_data[4]
            RTT = new_user_data[5]
                
            user.add_measurements(new_session.id,dropped_frames,FPS,bitrate,RTT)
                
                
            user = logger.update_users_summaries(user,isNew,stats_calculator)
            prev_user_id = copy.copy(user_id)
            prev_session_id = copy.copy(user_session_id)
            prev_device = copy.copy(new_device)
            isNew  = False
            # c += 1
            # if c>60:
            # #     print(logger.users_summaries[first_id])
            #     break
            
            
            
    while True:

        case = functions[0]()
        functions[case](S,logger)
        if case == '6':
            break
        
    #_______________________________________________________
    # if c>100000:
    #     print(logger.users_summaries[first_id])
    # c += 1
    # if c==135340:
    #     break
      


        
   
