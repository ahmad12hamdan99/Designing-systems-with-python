

def read_day_data():
    c = 0
    prev_user_id = " "
    prev_session_id = " "
    prev_device = " "
    first_id = ' '
    prev_session = None

    for row in csvreader:
        if row[0]=="client_user_id":
            continue 

        
        new_user_data = row
        if prev_user_id != new_user_data[0]:
            user_id = new_user_data[0]
            user = classes.User(user_id)
            isNew = True
            S.add_user(user)
        # if c==100000:
        #     first_id = user_id
        # else:
        #     first_id = first_id
            
            
        time_stamp = new_user_data[-2]     
        if prev_session_id != new_user_data[1]:
            if prev_session_id != " ":
                new_session.add_end_time(time_stamp)
            user_session_id = new_user_data[1]
            new_session  = classes.Session(user_session_id,time_stamp)
            user.add_session(new_session) 
        else:
            new_session.update_session_time(time_stamp)
            
                
                
                
            
        
        new_device = new_user_data[-1]
        if new_device != prev_device or isNew:
            user.add_device(new_device)
            user.update_devices_info()
        
        # print(row)
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
        