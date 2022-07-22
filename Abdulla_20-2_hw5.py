import re
class ValidCarNumber:
    def __init__(self, number):
        self.number = number
    def is_valid(self):
        is_number = re.search(r"(0[0-9]{1}KG([0-9]{3}([A-Z]{3})))", self.number)
        try:
            if self.number[is_number.start():is_number.end()] == self.number:
                 return f"Is Valid number!"
        except:
            return f"Is InValid number!"
number = input("Введите номер машины: ")
num = ValidCarNumber(number)