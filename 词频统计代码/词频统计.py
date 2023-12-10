import pandas as pd
import jieba
import re
from collections import Counter

def clean_text(text):
    # 去除文本中的非中文字符
    cleaned_text = re.sub(r'[^\u4e00-\u9fa5]+', ' ', text)
    return cleaned_text

def tokenize_text(text, stop_words):
    # 使用jieba对文本进行分词，并过滤停用词
    tokens = jieba.cut(text)
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def count_word_frequency(tokens):
    # 统计词频
    word_frequencies = Counter(tokens)
    return word_frequencies

def save_to_excel(word_frequencies, excel_path):
    # 转换为DataFrame格式
    df = pd.DataFrame.from_dict(word_frequencies, orient='index', columns=['Frequency'])
    df.index.name = 'Word'

    # 保存到Excel文件
    df.to_excel(excel_path)

# 自定义路径的txt文本文件
file_path = "C:\\Users\\ASUS\\Desktop\\毕论\\爬取弹幕内容\\纯文本\\《国家宝藏》第一季第七期-弹幕.txt"  # 替换为你的文本文件路径

# 自定义路径的Excel文件
excel_path = "C:\\Users\\ASUS\\Desktop\\毕论\\文本词频统计\\第一季第七期弹幕文本词频统计.xlsx" # 替换为你的输出Excel文件路径

# 自定义路径的停用词文件
stop_words_path = "C:\\Users\\ASUS\\Desktop\\毕论\\stopwords list.txt"  # 替换为你的停用词文件路径

# 读取停用词文件内容
with open(stop_words_path, 'r', encoding='utf-8') as file:
    stop_words = file.read().splitlines()

# 读取文本文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 清洗文本
cleaned_text = clean_text(text)

# 分词并过滤停用词
tokens = tokenize_text(cleaned_text, stop_words)

# 统计词频
word_frequencies = count_word_frequency(tokens)

# 将结果保存到Excel表格中
save_to_excel(word_frequencies, excel_path)

print('词频统计完成')