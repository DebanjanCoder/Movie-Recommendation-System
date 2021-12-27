from data_access_layer.db_table_create import check_database_exist, moviedb
from presentation_layer.user_input import user_input
from entity_layer.user import User
from business_logic_layer.user_operation import UserOperation
from data_access_layer.user_storage import UserStorage
from presentation_layer.movie_input import movie_input
from entity_layer.movie import Movie
from data_access_layer.movie_storage import MovieStorage
from presentation_layer.main_menu import main_menu, user_menu, movie_menu
from logger_layer.log_request import LogRequest
from data_access_layer.log_storage import LogStorage

if __name__ == "__main__":

    result = check_database_exist()
    if result == False:
        moviedb()
    else:
        pass

    while True:
        lr = LogRequest(executed_by="debanjan@gmail.com")
        log_start_data = lr.log_start()
        LogStorage().save_log_start_request(log_start_data=log_start_data)
        choice = main_menu(execution_id=log_start_data['execution_id'])
        log_stop_data = lr.log_stop(response_status="ok", response_msg= "success",function_name="main_menu", input_details={"choice": choice})
        LogStorage().save_log_stop_request(log_stop_data=log_stop_data, execution_id=log_start_data['execution_id'])
  #      LogStorage().get_log_request()
        while True:
            if choice == 1:
                log_start_data = lr.log_start()
                LogStorage().save_log_start_request(log_start_data=log_start_data)
                choice = user_menu(execution_id=log_start_data['execution_id'])
                log_stop_data = lr.log_stop(response_status="ok", response_msg= "success",function_name="user_menu", input_details={"choice": choice})
                LogStorage().save_log_stop_request(log_stop_data=log_stop_data,
                                                   execution_id=log_start_data['execution_id'])

                if choice == 1:
                    log_start_data = lr.log_start()
                    LogStorage().save_log_start_request(log_start_data=log_start_data)
                    user_id, user_name, user_email, user_age, user_gender = user_input(execution_id=log_start_data['execution_id'])
                    log_stop_data = lr.log_stop(response_status="ok", response_msg="success", function_name="user_input",
                                input_details={"user_id": user_id, "user_name": user_name, "user_email": user_email,
                                            "user_age": user_age, "user_gender": user_gender})
                    LogStorage().save_log_stop_request(log_stop_data=log_stop_data,
                                                       execution_id=log_start_data['execution_id'])
                    log_start_data = lr.log_start()
                    LogStorage().save_log_start_request(log_start_data=log_start_data)
                    user = User(user_id, user_name, user_email, user_age, user_gender, execution_id=log_start_data['execution_id'])
                    log_stop_data = lr.log_stop(response_status="ok", response_msg="success", function_name="User.__init__",
                                input_details={"user_id": user_id, "user_name": user_name, "user_email": user_email,
                                               "user_age": user_age, "user_gender": user_gender})
                    LogStorage().save_log_stop_request(log_stop_data=log_stop_data,
                                                       execution_id=log_start_data['execution_id'])
                    log_start_data = lr.log_start()
                    LogStorage().save_log_start_request(log_start_data=log_start_data)
                    result = UserOperation().is_valid_user(user, execution_id=log_start_data['execution_id'])
                    if result == "success":
                        log_stop_data = lr.log_stop(response_status="ok", response_msg="success",
                                    function_name="UserOperation().is_valid_user", input_details={"user": user})
                        LogStorage().save_log_stop_request(log_stop_data=log_stop_data,
                                                           execution_id=log_start_data['execution_id'])
                        log_start_data = lr.log_start()
                        LogStorage().save_log_start_request(log_start_data=log_start_data)
                        result = UserStorage().save_user(user, execution_id=log_start_data['execution_id'])
                        if result == True:
                            print("User Data Inserted Successfully")
                            choice = 1
                            log_stop_data = lr.log_stop(response_status="ok", response_msg="success",
                                        function_name="UserOperation().save_user", input_details={"user": user})
                            LogStorage().save_log_stop_request(log_stop_data=log_stop_data,
                                                               execution_id=log_start_data['execution_id'])
                            LogStorage().get_log_request()
                            continue
                        else:
                            print("Error Inserting User Data")
                            choice = 1
                            log_stop_data = lr.log_stop(response_status="failed", response_msg="failure",
                                        function_name="UserOperation().save_user", input_details={"user": user})
                            LogStorage().save_log_stop_request(log_stop_data=log_stop_data,
                                                               execution_id=log_start_data['execution_id'])
                            continue
                    else:
                        print(result)
                        log_stop_data = lr.log_stop(response_status="failed", response_msg="failure",
                                    function_name="UserOperation().is_valid_user", input_details={"user": user})
                        LogStorage().save_log_stop_request(log_stop_data=log_stop_data,
                                                           execution_id=log_start_data['execution_id'])
                        continue

                elif choice == 2:
                    UserStorage().get_user()
                    choice = 1
                    continue
                elif choice == 3:
                    pass
                elif choice == 4:
                    pass
                elif choice == 5:
                    pass
                elif choice == 6:
                    break
                elif choice == 7:
                    exit(0)
                else:
                    print("Invalid Choice!!! Please Enter Again")
                    continue

            elif choice == 2:
                choice = movie_menu(execution_id=execution_id)
                if choice == 1:
                    movie_id, movie_name, movie_genre, movie_description, movie_director, movie_actors, movie_language, movie_category = movie_input()
                    movie = Movie(movie_id, movie_name, movie_genre, movie_description, movie_director, movie_actors,
                              movie_language, movie_category)
                    result = MovieStorage().save_movie(movie)
                    if result == True:
                        print("Movie Data Inserted Successfully")
                        choice = 2
                        continue
                    else:
                        print("Error Inserting Movie Data")
                        choice = 2
                        continue
                elif choice == 2:
                    pass
                elif choice == 3:
                    pass
                elif choice == 4:
                    pass
                elif choice == 5:
                    pass
                elif choice == 6:
                    break
                elif choice == 7:
                    exit(0)

                else:
                    print("Invalid Choice!!! Please Enter Again")
                    continue
            elif choice == 3:
                pass
            elif choice == 4:
                exit(0)
            else:
                print("Invalid Choice!!! Please Enter Again")
                continue

