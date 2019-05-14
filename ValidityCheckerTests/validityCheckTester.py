import unittest
import sys
sys.path.append('../')
import os

from ValidityChecker.PersonnummerValidityCheck import *
from ValidityChecker.IsDataNotNullValidityCheck import *
from ValidityChecker.LoggToFile import *
from ValidityChecker.ValidityChecker import *

class TestValidityChecker(unittest.TestCase):

    def test_personnummerValidityChecker(self):
        pnumChecker = PersonummerValidityChecker()
        self.assertEqual(str(pnumChecker), "PersonnummerValidityCheck")
        self.assertFalse(pnumChecker.validateData("18232"))
        self.assertTrue(pnumChecker.validateData("19910605-4316"))
        self.assertTrue(pnumChecker.validateData("19780202-2389"))
        self.assertTrue(pnumChecker.validateData("197802022389"))
        self.assertTrue(pnumChecker.validateData("7802022389"))
        self.assertFalse(pnumChecker.validateData("19780202-2389.."))
        self.assertFalse(pnumChecker.validateData("19780202-23as89"))
        self.assertFalse(pnumChecker.validateData(None))
        self.assertFalse(pnumChecker.validateData("06054316"))

    def test_isDataNullValidityChecker(self):
        none = None
        nullChecker = IsDataNotNullValidityCheck()
        self.assertEqual(str(nullChecker), "IsDataNotNullValidityCheck")
        self.assertTrue(nullChecker.validateData("18232"))
        self.assertFalse(nullChecker.validateData(none))

    def test_validityChecker(self):
        filename = "test.txt"
        validityChecker = ValidityChecker(LoggToFile(filename), [IsDataNotNullValidityCheck(), PersonummerValidityChecker()])

        self.assertTrue(validityChecker.checkValidityOfData("199106054316"))
        self.assertFalse(validityChecker.checkValidityOfData("asd--11s"))
        self.assertFalse(validityChecker.checkValidityOfData(None))
        
        if os.path.exists(filename):
            with open(filename,"r") as file:
                fileStr = file.readline()
                self.assertTrue("asd--11s" in fileStr)
                self.assertFalse(str(IsDataNotNullValidityCheck()) in fileStr)
                self.assertTrue(str(PersonummerValidityChecker()) in fileStr)
            os.remove(filename)
        else:
            self.assertTrue(False, "No file was created, or it was created with incorrect name")

        #Remove PersonnummerValiditiyCheck
        validityChecker.removeValidityChecker(PersonummerValidityChecker())
        # Should pass since we removed PersonnummerValidator
        self.assertTrue(validityChecker.checkValidityOfData("asd--11s"))

    def test_emptyValidityChecker(self):
        filename = "test.txt"
        validityChecker = ValidityChecker(LoggToFile(filename))
        self.assertRaises(ValueError, validityChecker.checkValidityOfData, "123123123")
        if os.path.exists(filename):
            self.assertTrue(False, filename + " should not be created in this case.")


    def test_validityCheckerAddValidityChecker(self):
        filename = "test.txt"
        validityChecker = ValidityChecker(LoggToFile(filename))
        self.assertRaises(ValueError, validityChecker.checkValidityOfData, "test")
        validityChecker.addValidityChecker(IsDataNotNullValidityCheck())
        self.assertTrue(validityChecker.checkValidityOfData("test"))

    def test_validityCheckerInitWithOneChecker(self):
        filename = "test.txt"
        validityChecker = ValidityChecker(LoggToFile(filename), IsDataNotNullValidityCheck())
        self.assertTrue(validityChecker.checkValidityOfData("test"))

    def test_validityCheckerRemoveChecker(self):
        filename = "test.txt"
        validityChecker = ValidityChecker(LoggToFile(filename), IsDataNotNullValidityCheck())
        self.assertTrue(validityChecker.checkValidityOfData("test"))
        validityChecker.removeValidityChecker(IsDataNotNullValidityCheck())
        self.assertRaises(ValueError, validityChecker.checkValidityOfData, "test")

if __name__ == '__main__':
    unittest.main()