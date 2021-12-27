class LogProgress:
    def __init__(self, execution_id):
        self.execution_id = execution_id

    def log(self, message):
        log_progress = {}
        log_progress[self.execution_id] = message
        return log_progress

