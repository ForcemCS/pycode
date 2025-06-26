from datetime import datetime

#code1
date_str = "2023-10-27"
format_str = "%Y-%m-%d"  # 描述：年-月-日

dt_object = datetime.strptime(date_str, format_str)

print(dt_object)
print(type(dt_object))
# 验证一下
print(f"年份是: {dt_object.year}")
print(f"月份是: {dt_object.month}")
print(f"日期是: {dt_object.day}")

#code2

datetime_str = "2023-10-27 15:45:30"
format_str = "%Y-%m-%d %H:%M:%S" # 描述：年-月-日<空格>时:分:秒

dt_object = datetime.strptime(datetime_str, format_str)

print(dt_object)
print(f"小时是 (24小时制): {dt_object.hour}")

#code3
complex_str = "27/Oct/2023, 03:30 PM"
# 格式需要完全匹配：日/缩写月/年, 时(12h):分 AM/PM
format_str = "%d/%b/%Y, %I:%M %p" 

dt_object = datetime.strptime(complex_str, format_str)

print(dt_object)