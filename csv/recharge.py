import csv

# 输入输出文件路径
input_file = 'ro.csv'
output_file = 'output.csv'

# 要转换的字段名
target_column = '连续登录天数'

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    for row in reader:
        try:
            # 将连续登录天数转为二进制字符串
            days = int(row[target_column])
            row[target_column] = bin(days)[2:]  # 去掉 '0b' 前缀
        except ValueError:
            # 如果转换失败，比如字段为空，就保留原值
            pass
        writer.writerow(row)

print("转换完成，已保存为:", output_file)
