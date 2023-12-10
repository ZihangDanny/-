import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 读取词频统计结果的Excel文件
excel_path = "C:\\Users\\ASUS\\Desktop\\毕论\\文本词频统计\\第二季第二期弹幕文本词频统计-筛选版.xlsx"  # 替换为你的词频统计结果Excel文件路径
df = pd.read_excel(excel_path)

# 创建无向图
G = nx.Graph()

# 添加节点和边
for i, row in df.iterrows():
    word = row.iloc[0]  # 获取第一列的词语名称
    frequency = row['Frequency']
    G.add_node(word, frequency=frequency)  # 添加节点
    if i < len(df) - 1:
        for j in range(i + 1, len(df)):
            related_word = df.at[j, 'Word']
            related_frequency = df.at[j, 'Frequency']
            G.add_edge(word, related_word, weight=related_frequency)  # 添加边
# 调整节点位置
pos = nx.spring_layout(G, seed=28, k=0.5, iterations=200)  # 调整布局算法的参数

# 设置节点标签
node_labels = {node: node for node in G.nodes}  # 使用词语名称作为节点标签

# 创建节点标签大小字典
node_sizes = [node_data['frequency'] for _, node_data in G.nodes(data=True)]

# 定义节点颜色
node_color = 'blue'
edge_color = 'grey'
font_color = 'black'

# 绘制网络图
plt.figure(figsize=(12, 8))

# 绘制节点
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, alpha=0.8, node_color=node_color)

# 绘制边
nx.draw_networkx_edges(G, pos, width=0.5, alpha=0.3, edge_color=edge_color)

# 调整节点标签的位置
offset = 0.05  # 垂直偏移量
for node, label in node_labels.items():
    x, y = pos[node]
    plt.text(x, y + offset, label, ha='center', va='bottom', fontsize=8, fontweight='bold', fontfamily='Microsoft YaHei', color=font_color)

plt.axis('off')
plt.title('')
plt.rcParams['font.sans-serif'] = ['SimHei']

# 上移整个图形
plt.subplots_adjust(top=0.95)  # 调整 top 的值来上移图形

output_path = "C:\\Users\\ASUS\\Desktop\\毕论\\社会网络关系图\\第二季第二期弹幕关键词社会网络关系图.png"  # 替换为你要保存图像的路径和文件名
plt.savefig(output_path)
plt.show()

print('社会网络图制作完成')