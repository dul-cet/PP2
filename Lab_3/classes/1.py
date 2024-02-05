"""
1. Define a class which has at least two methods:
`getString`: to get a string from console input
`printString`: to print the string in upper case.
"""

class StringOps:
    def getString(self):
        string = input()
        return string

    def printString(self, string):
        print(string.upper())

stringOps = StringOps()
string = stringOps.getString()
stringOps.printString(string)