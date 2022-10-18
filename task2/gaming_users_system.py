import utils.parser as up
from data_loader import DriveAPI




functions = [up.base_case, up.get_status_parser, up.print_user_summary_parser, 
            up.predict_duration_parser, up.fetch_update_parser, up.get_top5_parser, up.exit_prog_parser]

obj = DriveAPI()

obj.FileDownload('2022_09_07', 'downloadedfromdrive')


while True:
    
    case = functions[0]()
    functions[case]()
    if case == '6':
        break