from datetime import datetime
s=input()
s=datetime.strptime(s, '%I:%M:%S%p')
print(s.strftime('%H:%M:%S'))
# from datetime import datetime
# time_str = input("Enter time in 12-hour AM/PM format (e.g. 11:30:45PM): ")

# def convert_to_military_time(time_str):
#     dt = datetime.strptime(time_str, '%I:%M:%S%p')
#     return dt.strftime('%H:%M:%S')
# print(convert_to_military_time(time_str))