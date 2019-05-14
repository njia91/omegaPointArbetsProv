
class ValidityChecker:
    """ Configurable validity checker

    This class can be configured with multiple validity checkers
    that can confirm the validitiy the data given to its function
    checkvalidityOfData. When a validitychecker fails, it will log
    which validityChecker that failed and the data it attempted to
    validitate. 

    The validateData function will run the input data through all
    validate checkers that this object is configured with.
    
    The requirment of a validity checker is
    that it must implement a function validtateData().

    The class must also be supplied a logger, this object must
    implement a function called log(). When a validity check fails
    the log function will be called upon.
    """
    def __init__(self, logger, validityCheckers = []):
        """ __init__ function of ValidityChecker

        Args:
            logger: Object that implements a log() function
            
            validityCheckers: (list) List of ValidityCheckers,
                Each validityChecker must implement a validateData()
                and __str__ function. See Class header.

        """
        self.validityCheckers = []
        if type(validityCheckers) == list:
            self.validityCheckers.extend(validityCheckers)
        else:
            self.validityCheckers.append(validityCheckers)
        self.logger = logger

    def addValidityChecker(self, validiyChecker):
        self.validityCheckers.append(validiyChecker)

    def removeValidityChecker(self, validiyChecker):
        self.validityCheckers = [x for x in self.validityCheckers if not isinstance(x,type(validiyChecker))]


    def checkValidityOfData(self, data):
        allDataValid = True
        if self.validityCheckers is None or len(self.validityCheckers) is 0:
            raise ValueError("Please add a validityChecker before executing this function")
        for validityChecker in self.validityCheckers:
            if validityChecker.validateData(data) is False:
                self.logger.log(str(validityChecker), data)
                allDataValid = False
        return allDataValid
        
