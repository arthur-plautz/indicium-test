import convert as cv
import operations as op

tables = cv.get_tables(['contacts','companies','deals','sectors'])
x = 1
y = 1
while(x != 0):
    output_format = input('Digite o tipo de saída (Documento/Objeto): ')
    while(y != 0):
        try:
            mes = int(input('Para o segundo conjunto de saída, informe o mês referente à representatividade do setor (número): '))
            y = 0
        except:
            print('O mês precisa estar no formato de número')
    output_format = output_format.upper()
    output1 = [op.get_valor_contato(tables, ''),
                op.get_valor_mes(tables)]
    output2 = op.setor_mes(tables, mes)

    if(output_format == 'OBJETO'):
        print(output1[0])
        print('\n')
        print(output1[1])
        print('\n')
        print(output2)
        x = 0
    elif(output_format == 'DOCUMENTO'):
        cv.py_to_tsv(output1[0], 'valor_contato', ['contato','valorTotal'])
        cv.py_to_tsv(output1[1], 'valor_mes', ['mes','valorTotal'])
        fields = [
            ['titulo','valor'],
            ['contato','valorTotal','mes','valorTotal']
        ]
        cv.merge_csv('output_valor_contato_mes',['docs/output_valor_contato.csv','docs/output_valor_mes.csv'],fields)
        cv.py_to_tsv(output2, 'valor_setor', ['id','setor','representacao'])
        print('Os documentos podem ser encontrados no diretório "docs"')
        x = 0
    else:
        print('Formato de saída inválido')
