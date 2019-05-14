
class LoggToFile:
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, validityCheckStr, data):
        with open(self.filename, "a+") as file:
            file.write("Failed Validity Check:" + validityCheckStr +". Data used: " + str(data) +"\n")
