from logger_layer.log_progress import LogProgress
from data_access_layer.log_storage import LogStorage



def main_menu(execution_id):
    lp = LogProgress(execution_id=execution_id)
    log_progress = lp.log(message = "Inside main_menu")
    LogStorage().save_log_progress(log_progress=log_progress)
    print("\t\t**************MAIN MENU*****************")
    print("\n 1. User")
    print("\n 2. Movie")
    print("\n 3. Get Recommendation")
    print("\n 4. Exit")
    lp.log(message = "Waiting for user to provide input")
    choice = int(input("\n\n Please Enter Your Choice : "))
    lp.log(message= "Received input from user. Returning the input")
    return choice


def select_main_menu(execution_id,choice):
    return choice


def user_menu(execution_id):
   # lp = LogProgress(execution_id=execution_id)
   # lp.log(message="Inside user_menu")
    print("\t\t*************USER MENU******************")
    print("\n 1. Create User Data")
    print("\n 2. Read User Data")
    print("\n 3. Update User Data")
    print("\n 4. Delete User Data")
    print("\n 5. Read Entire User Data")
    print("\n 6. Back")
    print("\n 7. Exit")
    choice = int(input("\n\n Please Enter Your Choice : "))
   # lp.log(message="choice : " + str(choice))
    return choice


def movie_menu(execution_id):
   # lp = LogProgress(execution_id=execution_id)
   # lp.log(message="Inside movie_menu")
    print("\t\t*************MOVIE MENU*****************")
    print("\n 1. Create Movie Data")
    print("\n 2. Read Movie Data")
    print("\n 3. Update Movie Data")
    print("\n 4. Delete Movie Data")
    print("\n 5. Read Entire Movie Data")
    print("\n 6. Back")
    print("\n 7. Exit")
    choice = int(input("\n\n Please Enter Your Choice : "))
    #lp.log(message="choice : " + str(choice))
    return choice
