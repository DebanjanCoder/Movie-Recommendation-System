from entity_layer.user import User
from data_access_layer.user_storage import UserStorage
import re

class UserOperation:

    def is_valid_user(self, user:User, execution_id):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        gender = ['male','female','m','f','other','o']
        error_msg = ""
        UserStorage()
        if (re.fullmatch(regex, user.user_email)):
            if (user.user_age > 4):
                if (str(user.user_gender).lower() in gender):
                    error_msg = "success"
                    return error_msg
                else:
                    error_msg = "Gender not correct. Please enter correct gender."
            else:
                error_msg = "Age not valid. Please enter a valid age."
        else:
            error_msg = "Email not valid. Please enter a valid email."
        return error_msg

    def get_liked_movie_list(self, user: User):
        pass

    def get_disliked_movie_list(self, user: User):
        pass
