#文本清洗代码，作者：lzh
import jieba

#加载停用词
stop_words=set()

with open('C:\\Users\\ASUS\\Desktop\\毕论\\stopwords list.txt','r', encoding='utf-8') as file:
    for line in file:
        stop_words.add(line.strip())

#打开要清洗的文本文件
with open('C:\\Users\\ASUS\\Desktop\\毕论\\爬取弹幕内容\\纯文本\\《国家宝藏》第四季第一期-弹幕.txt', 'r', encoding='utf-8') as file:
    with open('C:\\Users\\ASUS\\Desktop\\毕论\\爬取弹幕内容\\清洗版\\《国家宝藏》第四季第一期-弹幕（清洗版）.txt', 'w', encoding='utf-8') as output_file:
        for line in file:
            text = line.strip()
            seg_list = jieba.cut(text)
            filtered_text = [word for word in seg_list if word not in stop_words]
            cleaned_text = ' '.join(filtered_text)
            output_file.write(cleaned_text + '\n')

print("清洗完成")