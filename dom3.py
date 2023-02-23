from datetime import datetime
dt_1 = datetime(1996, 7, 19)
dt_2 = datetime(1992, 10, 22)
if dt_1.year>dt_2.year:
    print("человек 2 старше")
elif dt_1.month>dt_2.month:
    print("человек 2 старше")
elif dt_1.day>dt_2.day:
    print("человек 2 старше")
else:
    print("человек 1 старше")