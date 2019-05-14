class IsDataNotNullValidityCheck:

    def validateData(self, data):
        if data is None:
            return False
        return True

    def __str__(self):
        return "IsDataNotNullValidityCheck"