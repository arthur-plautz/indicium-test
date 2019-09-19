import csv
import numpy as np

def tsv_to_py(table):
    with open(table, encoding='utf8') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        table = []
        for row in reader:
            length = row.__len__()
            for i in range(length):
                if(table.__len__() != length):
                    table.append([])
                table[i].append(row[i])
        return table


def py_to_tsv(output, name, fields):
    with open('docs/output_' + name + '.csv', 'w', newline='', encoding='utf8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for key in output:
            if(name == 'valor_setor'):
                item = key
            else:
                item = {fields[0]: key, fields[1]: output[key]}
            writer.writerow(item)

def get_tables(indexes):
    tables = {}
    for i in range(indexes.__len__()):
        document = 'docs/' + indexes[i] + '.tsv'
        table = np.transpose(tsv_to_py(document))
        tables[indexes[i]] = table
    return tables
