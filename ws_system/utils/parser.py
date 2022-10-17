

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


def print_user_summary_parser():
    user_id = input('Enter user id:')
    print()
    p = input('\nEnter period (yy/mm/dd - yy/mm/dd) :\n')
    print()
    #change that to work with class
    #call needed function from class
    
    print()
    more = input('Find another user ? (yes/No)')
    if more.lower() == 'yes':
        print_user_summary_parser()

def predict_duration_parser():
    '''
    Predict user next session duration
    '''

def get_status_parser():
    '''
    Get status for the past 7 days
    '''

def fetch_update_parser():
    '''
    Fetch new data and update users data and ML model
    '''

def get_top5_parser():
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