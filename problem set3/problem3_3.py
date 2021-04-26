def problem3_3(month, day, year):

    months = ("January", "February", "March", "April", "May", "June", "July", \
              "August", "September", "October", "November", "December")
    monthStr = int(month) - 1
    print(months[monthStr], str(day) + ",", year)