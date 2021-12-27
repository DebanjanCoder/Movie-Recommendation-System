from datetime import datetime
import uuid

class LogRequest:
    def __init__(self, executed_by):
        self.executed_by = executed_by

    def log_start(self):
        log_data = {
            'execution_id': str(uuid.uuid4()),
            'executed_by': self.executed_by,
            'start_time': datetime.now()
        }
        #print(log_data)
        return log_data


    def log_stop(self, response_status, response_msg, function_name, input_details):
        log_data = {
            'stop_time': datetime.now(),
            'function_params': function_name + "(" + str(input_details) + ")",
            'response_status': response_status,
            'response_msg': response_msg
        }
        #print(log_data)
        return log_data

