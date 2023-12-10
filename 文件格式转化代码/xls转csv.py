import pandas as pd

# 读取xls文件
xls_file = pd.ExcelFile('C:\\Users\\ASUS\\Desktop\\毕论\\爬取弹幕内容\\爬取版\\《国家宝藏》第二季第一期-弹幕.xls')

# 获取xls文件的所有sheet名称
sheet_names = xls_file.sheet_names

# 遍历每个sheet，并将其转换为csv文件
for sheet_name in sheet_names:
    # 读取sheet内容
    df = xls_file.parse(sheet_name)

    # 获取原文件的路径和文件名
    file_path = 'C:\\Users\\ASUS\\Desktop\\毕论\\爬取弹幕内容\\爬取版\\《国家宝藏》第二季第一期-弹幕.xls'
    file_name = file_path.split('/')[-1].split('.')[0]

    # 构造csv文件的路径和文件名
    csv_file_name = f'{file_name}_{sheet_name}.csv'

    # 将sheet内容保存为csv文件
    df.to_csv(csv_file_name, index=False)

print('输出完成')