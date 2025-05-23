a =1 
b = 0
try:
    c = a / b
except ZeroDivisionError:   #捕获的特定异常类型，如果try中的代码，如果 try 块中发生了 ZeroDivisionError 异常，这里的代码会执行
    print("hello")
    #print(c)


a =1 
b = 0
try:
    c = a / b
except ZeroDivisionError as ex:   #获取异常对象本身，方便查看错误信息
    print(f"Exception occurred: {ex}")
    c= 0 
print(c)


# try:
#     try:
#         raise ValueError('something happened')
#     except ValueError as ex:
#         log(ex)
#         raise
# except Exception as ex:
#     print(f'ignoring: {ex}')


# try:
#     open_database_connection()
#     start_transaction()
#     write_data()
#     commit_transaction()
# except WriteException as ex:
#     rollback_transaction()
#     raise
# finally:
#     close_database_connection()

