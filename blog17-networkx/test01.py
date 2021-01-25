# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
 
#定义有向图
DG = nx.DiGraph() 

#添加五个节点(列表)
DG.add_nodes_from(['A', 'B', 'C', 'D', 'E'])
print(DG.nodes())

#添加边(列表)
DG.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('D','A'),('E','A'),('E','D')])
print(DG.edges())

#绘制图形 设置节点名显示\节点大小\节点颜色
colors = ['red', 'green', 'blue', 'red', 'yellow']
nx.draw(DG, with_labels=True, node_size=900, node_color = colors)
plt.show()
