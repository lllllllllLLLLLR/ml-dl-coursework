import pandas as pd

# 定义一个函数，将不同格式的时间统一为"分.秒"
def sanitize(time_string): 
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    elif '.' in time_string:
        splitter = '.'
    else:
        return None  # 如果不包含有效分隔符，直接返回 None

    parts = time_string.split(splitter)
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():  # 确保分割后是两部分且都为数字
        return f"{parts[0]}:{parts[1]}"
    else:
        return None  # 如果格式不符合要求，返回 None

# 读取每位选手的时间，并计算最快的3个不同时间
def get_fastest_times(file_name):
    with open(file_name, 'r') as file:
        # 将每一行的内容分割成列表
        data = file.read().strip().split(',')
        # 跳过文件中的姓名和日期部分
        sanitized_times = [sanitize(time.strip()) for time in data[2:]]  # 从第3个元素开始处理时间
        sanitized_times = [time for time in sanitized_times if time is not None and time != '']
        sanitized_times = list(sanitized_times)  # 先转为列表试一下吧
 
        # 利用 Pandas 的 Series 进行处理
        times_series = pd.Series(sanitized_times)
        # 删除重复值
        unique_times = times_series.drop_duplicates()
        # 排序
        sorted_times = unique_times.sort_values()
        # 获取最快的三个时间
        fastest_times = sorted_times.head(3)
        # 返回Series对象
        return fastest_times

if __name__ == '__main__':
    # 获取每位选手的最快时间
    james_fastest = get_fastest_times('james.txt')
    sarah_fastest = get_fastest_times('sarah.txt')
    julie_fastest = get_fastest_times('julie.txt')
    mikey_fastest = get_fastest_times('mikey.txt')

    # 打印结果
    print(f"James Lee's fastest times are: {james_fastest.values}")
    print(f"Julie Johns's fastest times are: {julie_fastest.values}")
    print(f"Mikey McManus's fastest times are: {mikey_fastest.values}")
    print(f"Sarah Sweeney's fastest times are: {sarah_fastest.values}")
