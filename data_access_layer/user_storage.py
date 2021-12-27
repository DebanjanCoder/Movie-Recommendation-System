from entity_layer.user import User
import sqlite3
import os, sys
from exception_layer.generic_exception import GenericException as UserStorageException


class UserStorage:
    def __init__(self):
        """
        Orgnization: iNeuron Intelligence Private Limited
        author: Depanjan@ineuron.ai
        created date:
        =================================================
        description:


        =================================================
        :param
        :returns



        """
        try:
            self.conn = sqlite3.connect('movie.db')
            self.c = self.conn.cursor()
        except Exception as e:
            user_storage_exception = UserStorageException(
                "Failed to create object of UserStorage  in module [{0}] class [{1}] method [{2}]"
                    .format(UserStorage.__module__.__str__(), UserStorage.__name__,
                            "__init__"))
            raise Exception(user_storage_exception.error_message_detail(str(e), sys)) from e

    def save_user(self, user: User, execution_id):
        """

        :param user:
        :return:
        """
        try:
            user_id = str(user.user_id)
            user_name = user.user_name
            user_email = user.user_email
            user_age = int(user.user_age)
            user_gender = user.user_gender

            query = "insert or ignore into user values(?, ?, ?, ?, ?);"
            self.c.execute(query, (user_id, user_name, user_email, user_age, user_gender))
            self.conn.commit()
            if self.c.execute(query, (user_id, user_name, user_email, user_age, user_gender)):
                return True
            else:
                return False
        except Exception as e:
            user_storage_exception = UserStorageException(
                "Error occurred in module [{0}] class [{1}] method [{2}]"
                    .format(UserStorage.__module__.__str__(), UserStorage.__name__,
                            self.save_user.__name__))
            raise Exception(user_storage_exception.error_message_detail(str(e), sys)) from e

    def get_user(self):
        """

        :param user:
        :return:
        """
        try:

            query = "select * from user;"
            self.c.execute(query)
            self.conn.commit()
            print(self.c.fetchall())
            if self.c.execute(query):
                return True
            else:
                return False
        except Exception as e:
            user_storage_exception = UserStorageException(
                "Error occurred in module [{0}] class [{1}] method [{2}]"
                    .format(UserStorage.__module__.__str__(), UserStorage.__name__,
                            self.save_user.__name__))
            raise Exception(user_storage_exception.error_message_detail(str(e), sys)) from e

