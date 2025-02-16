#Task1
'''
from datetime import datetime, timedelta
current_date = datetime.now()
new_data = current_date - timedelta(days=5) 
print (current_date)
print (new_data)
'''

#Task2
'''
from datetime import datetime, timedelta
date_today= datetime.now()
date_yesterday = date_today - timedelta(days=1)
date_tomorrow = date_today + timedelta(days=1)

print (date_yesterday)
print (date_today)
print (date_tomorrow)
'''
#Task3
'''
from datetime import datetime
current_date= datetime.now()
new_date = current_date.replace(microsecond=0)
print (new_date)
'''
#task4
from datetime import datetime
date1 = input("Enter the first date:")
date2 = input("Enter the second date:")
datetime1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
datetime2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
difference = abs((datetime2 - datetime1).total_seconds())
print(f"Difference between the two dates is {difference} seconds.")
