""" ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range() # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
"""
import statistics
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
count = len(ages)
print(count)
sum = sum(ages)
print(sum)
print(min(ages))
print(max(ages))
age_range = max(ages) - min(ages)
print(age_range)
avg_age = statistics.mean(ages)
print(avg_age)
median_age = statistics.median(ages)
print(median_age)
mode_age = statistics.mode(ages)
print(mode_age)
stand_deviation = statistics.stdev(ages)
print(stand_deviation)
stand_var = statistics.variance(ages)
print(stand_var)
frequency = statistics.multimode(ages)
print(frequency)
from collections import Counter
freq_dist = Counter(ages)
print(freq_dist)

""" Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, 
total_expense, account_info, add_income, add_expense and account_balance methods. 
Incomes is a set of incomes and its description. The same goes for expenses.
"""
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.income = []
        self.expenses = []

    def add_income(self, amount, description):
        self.income.append({'amount': amount, 'description': description})

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})

    def total_income(self):
        return sum(item['amount'] for item in self.income)
    
    def total_expenses(self):
        return sum(item['amount'] for item in self.expenses)
    
    def account_balance(self):
        return self.total_income() - self.total_expenses()
    
    def account_info(self):
        return (f'name: {self.firstname} {self.lastname}\n'
                f'total income: {self.total_income()}\n'
                f'total expenses: {self.total_expenses()}\n'
                f'total balance: {self.account_balance()}\n')
    

person = PersonAccount('Kate', 'Diamond')
person.add_income(6000, 'basic salary')
person.add_income(350, 'incentives')
person.add_expense(200, 'house rent')
person.add_expense(3000, 'miscellenous')

print(person.account_info())


