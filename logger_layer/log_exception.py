class LogException:
    def __init__(self, execution_id):
        self.execution_id = execution_id

    def log_error_message(self,message):
        print(self.execution_id,message)

