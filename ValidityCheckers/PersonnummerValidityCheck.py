class PersonummerValidityChecker:

    def validateData(self, data):
        if not isinstance(data, str):
            data = str(data)
        try:
            data = data.replace('-','') # Make sure data only consist of integers.
            dataLen = len(data)
            checkDigit = int(data[dataLen - 1])
            offset = 2
            evenSum = 0
            if dataLen == 10: # Adjust if the Personnummer is 12 or 10 digits
                offset = 0
            oddSum = sum(int(n) for n in data[offset + 1:dataLen - 1:2])
            evens = [2 * int(n) for n in data[offset:dataLen - 1:2]]
            for n in evens:
                if n >= 10: # If True, take sum of seperate digits
                    digits = str(n)
                    evenSum += int(digits[0]) + int(digits[1])
                else: # If single digit
                    evenSum += n
            # Validate against checkDigit
            totalSum = evenSum + oddSum
            return (10 - (totalSum % 10)) % 10 == checkDigit
        except ValueError:
            print("Please give a string or an integer as input.")
        return False
            
    def __str__(self):
        return "PersonnummerValidityCheck"

