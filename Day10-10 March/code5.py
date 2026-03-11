import csv
from datetime import date
file = open('expense.csv','a+',newline='')

# w = csv.writer(file)
r = csv.reader(file)
# w.writerow([ 'DATE', 'CATEGORY', 'AMOUNT' ]) ## column name
# w.writerows([
#     [date.today(), 'travel', 6000],
#     [date.today(), 'food', 600],
#     [date.today(), 'Entertainment', 170]
# ])
file.seek(0)
print(list(r))

file.close()