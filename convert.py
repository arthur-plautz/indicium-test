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

def merge_csv(name, docs, fields):
    with open(docs[0], 'r', encoding='utf8') as csvfile1:
        reader1 = csv.DictReader(csvfile1)
        with open(docs[1],'r',encoding='utf8') as csvfile2:
            reader2 = csv.DictReader(csvfile2)
            with open('docs/' + name + '.csv','w',newline='',encoding='utf8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fields[0])
                writer.writerow({fields[0][0]:fields[1][0], fields[0][1]:fields[1][1]})
                for line1 in reader1:
                    line = {fields[0][0]: line1[fields[1][0]],fields[0][1]: line1[fields[1][1]]}
                    writer.writerow(line)
                writer.writerow({fields[0][0]:fields[1][2], fields[0][1]:fields[1][3]})
                for line2 in reader2:
                    line = {fields[0][0]: line2[fields[1][2]],fields[0][1]: line2[fields[1][3]]}
                    writer.writerow(line)

def get_tables(indexes):
    tables = {}
    for i in range(indexes.__len__()):
        document = 'docs/' + indexes[i] + '.tsv'
        table = np.transpose(tsv_to_py(document))
        tables[indexes[i]] = table
    return tables
