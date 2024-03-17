import matplotlib.pyplot as plt
from utils import geneate_others_group

def generate_bar_chart(labels, values,xlabel,ylabel,title,threshold=25,include_others=True):
    labels_new,values_new = geneate_others_group(labels, values,threshold,include_others)
    fig, ax = plt.subplots(figsize=(10, 6)) 
    bars = ax.bar(labels_new, values_new, color='skyblue') 
    for bar, value in zip(bars, values_new):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(value), ha='center', va='bottom')
    ax.set_xlabel(xlabel)  
    ax.set_ylabel(ylabel)  
    ax.set_title(title) 
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()  
    plt.show()

def generate_pie_chart(labels, values, title,threshold=25,include_others=True):
    labels_new,values_new = geneate_others_group(labels, values,threshold,include_others)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(values_new, labels=labels_new, autopct='%1.1f%%', colors=plt.cm.tab20.colors, startangle=30)
    ax.set_title(title)
    plt.show()


