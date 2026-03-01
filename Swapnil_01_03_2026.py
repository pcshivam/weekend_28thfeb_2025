from datetime import datetime
print('This is trial push operation to Git')


birth_year = 1999
current_year = datetime.now().year

leap_years = 0
total_days = 0

for year in range(birth_year, current_year+1):
  if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
    leap_years = leap_years+1
    total_days = total_days + 366

  else:
    total_days = total_days + 365

print(leap_years)
print(total_days)