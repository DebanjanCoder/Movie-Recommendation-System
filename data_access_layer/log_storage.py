import sqlite3
from exception_layer.generic_exception import GenericException as LogStorageException
import sys


class LogStorage:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('movie.db')
            self.c = self.conn.cursor()
        except Exception as e:
            log_storage_exception = LogStorageException(
                "Failed to create object of LogStorage in module [{0}] class [{1}] method [{2}]"
                .format(LogStorage.__module__.str(), LogStorage.__name__, "__init__"))

            raise Exception(log_storage_exception.error_message_detail(str(e), sys)) from e

    def save_log_start_request(self, log_start_data):
        try:
            execution_id = log_start_data['execution_id']
            executed_by = log_start_data['executed_by']
            start_time = str(log_start_data['start_time'])

            query = "insert or ignore into logrequest values(?, ?, ?, ?, ?, ?, ?);"
            self.c.execute(query, (start_time, None,execution_id, executed_by, None, None, None))
            self.conn.commit()
            if  self.c.execute(query, (start_time, None,execution_id, executed_by, None, None, None)):
                print("success")
            else:
                print("failure")
            self.c.close()
            self.conn.close()

        except Exception as e:
            log_storage_exception = LogStorageException(
                "Error occured in module [{0}] class [{1}] method [{2}]"
                .format(LogStorage.__module__.__str__(), LogStorage.__name__,
                        self.save_log_start_request.__name__))
            raise Exception(log_storage_exception.error_message_detail(str(e), sys))

    def save_log_stop_request(self, log_stop_data, execution_id):
        try:
            stop_time = log_stop_data['stop_time']
            function_params = log_stop_data['function_params']
            response_status = log_stop_data['response_status']
            response_msg = log_stop_data['response_msg']
            query = "update logrequest set stop_time = ?, function_params = ?, response_status = ?, response_msg = ? where execution_id = ?"
            self.c.execute(query, (stop_time, function_params, response_status, response_msg, execution_id))
            self.conn.commit()
            if self.c.execute(query, (stop_time, function_params, response_status, response_msg, execution_id)):
                print("success")
            else:
                print("failure")
            self.c.close()
            self.conn.close()

        except Exception as e:
            log_storage_exception = LogStorageException(
                "Error occured in module [{0}] class [{1}] method [{2}]"
                    .format(LogStorage.__module__.__str__(), LogStorage.__name__,
                            self.save_log_start_request.__name__))
            raise Exception(log_storage_exception.error_message_detail(str(e), sys))

    def get_log_request(self):
        try:

            query = "select * from logrequest;"
            self.c.execute(query)
            self.conn.commit()
            print(self.c.fetchall())
            if self.c.execute(query):
                return True
            else:
                return False
        except Exception as e:
            log_storage_exception = LogStorageException(
                "Error occurred in module [{0}] class [{1}] method [{2}]"
                    .format(LogStorage.__module__.__str__(), LogStorage.__name__,
                            self.save_user.__name__))
            raise Exception(log_storage_exception.error_message_detail(str(e), sys)) from e

    def save_log_progress(self, log_progress):
        #try:
            execution_id = log_progress.keys()
            message = log_progress.values()

            print(execution_id[0]," ", message[0])
            '''
            query = "insert or ignore into logrequest values(?, ?, ?, ?, ?, ?, ?);"
            self.c.execute(query, (start_time, None,execution_id, executed_by, None, None, None))
            self.conn.commit()
            if  self.c.execute(query, (start_time, None,execution_id, executed_by, None, None, None)):
                print("success")
            else:
                print("failure")
            self.c.close()
            self.conn.close()

        except Exception as e:
            log_storage_exception = LogStorageException(
                "Error occured in module [{0}] class [{1}] method [{2}]"
                .format(LogStorage.__module__.__str__(), LogStorage.__name__,
                        self.save_log_start_request.__name__))
            raise Exception(log_storage_exception.error_message_detail(str(e), sys))
        
            '''

