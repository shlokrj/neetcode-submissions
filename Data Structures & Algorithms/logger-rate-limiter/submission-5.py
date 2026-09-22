class Logger:

    def __init__(self):
        self.msgdict={}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:

        if message not in self.msgdict:
            self.msgdict[message] = timestamp

            return True

        if timestamp - self.msgdict[message] >= 10:
            self.msgdict[message] = timestamp
            
            return True
        
        else:
            return False