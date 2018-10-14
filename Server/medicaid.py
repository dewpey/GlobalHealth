import csv

class Person():
    def __init__(self, p_household, p_state, p_income, p_pregnancy):
        self.household = p_household
        self.state = p_state
        self.income = p_income
        self.pregnancy = p_pregnancy

    def is_under_minimum(self, limit):
        minimum = ((12140 + ((self.household - 1)*4320))*float(limit))
        if self.income <= minimum:
            return True
        else:
            return False

    def expanded_medicaid_eligibility(self):
        with open('raw_data.CSV', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            for row in csv_reader:
                if row[0] == self.state and self.is_under_minimum(row[2]):
                    return True
                line_count += 1
        return False

    def pregnant_eligibility(self):
        with open('raw_data.CSV', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            for row in csv_reader:
                if row[0] == self.state and self.pregnancy == 1 and self.is_under_minimum(row[3]):
                    return True
                line_count += 1
        return False

    def chip_eligibility(self):
        with open('raw_data.CSV', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            for row in csv_reader:
                if row[0] == self.state and self.is_under_minimum(row[4]):
                    return True
                line_count += 1
        return False


# p1 = Person(10, "New Jersey", 20000, 0)
# print('Expanded Medicaid eligibility for adult:' + str(p1.expanded_medicaid_eligibility()))
# print('CHIP eligibility: ' + str(p1.chip_eligibility()))
# print('Pregnant woman Medicaid/CHIP eligibility: ' + str(p1.pregnant_eligibility()))
