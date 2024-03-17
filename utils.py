import re

def geneate_others_group(labels, values,treshold=25,include_others=True):
    grouped_labels = []
    grouped_values = []
    others_value = 0
    for label, value in zip(labels, values):
        if value < treshold:
            others_value += value
        else:
            grouped_labels.append(label)
            grouped_values.append(value)
    if others_value > 0 and include_others:
        grouped_labels.append("Others")
        grouped_values.append(others_value)
    return grouped_labels, grouped_values

def create_label_value_dict(data, field):
    label_value_dict = {}
    for item in data:
        valuation = re.sub(r'%|B|\$', '', item['Valuation'])
        valuation_number = int(valuation)
        if (item[field] not in label_value_dict):
            label_value_dict.update({item[field]: valuation_number})
        else:
            label_value_dict[item[field]] += valuation_number
    return label_value_dict
