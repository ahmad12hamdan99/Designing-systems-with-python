

def base_case():
    '''
    base case of the console with choices of actions
    '''
    print('Choose one operation from below :')
    print('\t1 : Get status for the past 7 days')
    print('\t2 : Print user summary')
    print('\t3 : Predict user next session duration')
    print('\t4 : Fetch new data and update users data and ML model')
    print('\t5 : Get top 5 users based on time spent gaming')
    print('\t6 : Exit program')
    print('\n')
    n = int(input())
    return n


def print_user_summary_parser(sys,logger):
    user_id = input('Enter user id:')
    #print(sys.users.keys())
    print()
    p = input('\nEnter period (yy/mm/dd - yy/mm/dd) :\n')
    # print("FCfFRwt:",sys.users.values())
    #change that to work with class
    #call needed function from class
    if user_id in sys.users.keys():
        print("User Found!")
        print("User with id : ",user_id)
        #print(sys.users.keys())
        print("     Number of sessions : ",logger.users_summaries[user_id]['session_numbers'])
        print("     Date of first session :",logger.users_summaries[user_id]['date_of_first_session'])
        print("     Average time spent per session : ",logger.users_summaries[user_id]['avg_spent_time_per_session'])
        print("     Date of most recent session : ",logger.users_summaries[user_id]['date_of_most_rescent_session'])
        print("     Most frequently used device : ",logger.users_summaries[user_id]['most_freq_used_device'])
        print("     Devices used : ",logger.users_summaries[user_id]['devices_used'])
        print("     Estimated next session time : ",logger.users_summaries[user_id]['next_sess_est_time'])
        print("     Super user : ",logger.users_summaries[user_id]['super'])
    else:
        print("Sorry User NOT Found!")


    print()
    more = input('Find another user ? (yes/No)')
    if more.lower() == 'yes':
        print_user_summary_parser(sys,logger)

def predict_duration_parser(sys,logger):
    '''
    Predict user next session duration
    '''
    user_id = input('Enter user id:')
    print()
    if user_id in sys.users.keys():
        print("User Found!")
        print("     Estimated next session time : ",logger.users_summaries[user_id]['next_sess_est_time'])

def get_status_parser(sys,logger):
    '''
    Get status for the past 7 days
    '''
    user_id = input('Enter user id:')
    if user_id in sys.users.keys():
        print("User Found!")
        print("     User status for the past 7 days ",logger.users_summaries[user_id]['user_status_per_last_7_days'])
    else:
        print("Sorry User NOT Found")
    print()
    

def fetch_update_parser():
    '''
    Fetch new data and update users data and ML model
    '''
    # already tha data is fetched !!

def get_top5_parser(sys,logger):
    '''
    Get top 5 users based on time spent gaming
    '''

def exit_prog_parser():
    '''
    Upon exit the system should display the summary for the past 7 days 
    (number of sessions for all sessions, average time spent per session, 
    sum of hours spent by all users) and option to save it to file
    '''
    #print summary

    flag = input("Save summary ? (yes/no)\n")
    if flag.lower() == 'yes':
        #save to file
        pass
    print('Good bye!!')