import matplotlib.pyplot as plt

def generate_bar_chart(labels, values,xlabel,ylabel,title):
    fig, ax = plt.subplots(figsize=(10, 6)) 
    ax.bar(labels, values, color='skyblue') 
    ax.set_xlabel(xlabel)  
    ax.set_ylabel(ylabel)  
    ax.set_title(title) 
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()  
    plt.show()

def generate_pie_chart(labels, values,title):
    fig, ax = plt.subplots(figsize=(8, 8))  

    ax.pie(values, labels=labels, autopct='%1.1f%%', colors=plt.cm.tab20.colors, startangle=30) 
    ax.set_title(title)
    plt.show()


