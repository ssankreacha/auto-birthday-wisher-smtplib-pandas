import datetime as dt

# date time module
# datetime is a class
# datetime is the module, and datetime is the class therefore we say as dt
current_info = dt.datetime.now()               # now() = current date and time
year = current_info.year
month = current_info.month
day = current_info.day
# print(month)

date_of_birth = dt.datetime(year=1998, month=3, day=1, hour=7)
print(date_of_birth)