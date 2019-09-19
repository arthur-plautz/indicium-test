def get_valor_contato(tables, mes):
    valorContatos = {}

    for i in range(1, tables['contacts'].__len__()):
        contact = tables['contacts'][i]
        total = 0
        for j in range(1, tables['deals'].__len__()):
            deal = tables['deals'][j]
            if(contact[0] == deal[3]):
                if(mes):
                    data = deal[1].split('/')
                    mes_deal = data[0]
                    if(int(mes) == int(mes_deal)):
                        total += float(deal[2])
                else:
                    total += float(deal[2])
        if(contact[1] in valorContatos):
            valorContatos[ contact[1] ] += total
        else:
            value = {contact[1]: total }
            valorContatos.update(value)

    return valorContatos


def get_valor_mes(tables):
    valorMes = {'jan': 0, 'fev': 0, 'mar': 0, 'abr': 0, 'mai': 0, 'jun': 0,
                'jul': 0, 'ago': 0, 'set': 0, 'out': 0, 'nov': 0, 'dez': 0}
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
             'jul', 'ago', 'set', 'out', 'nov', 'dez']

    for i in range(0, meses.__len__()):
        total = 0
        for j in range(1, tables['deals'].__len__()):
            deal = tables['deals'][j]
            data = deal[1].split('/')
            mes = data[0]
            if(i+1 == int(mes)):
                total += float(deal[2])
        valorMes[meses[i]] = total

    return valorMes


def setor_mes(tables, mes):
    valorMes = get_valor_mes(tables)
    valorContatos = get_valor_contato(tables, mes)
    valorSetor = [0,0,0,0,0,0]

    for i in range(tables['contacts'].__len__()):
        for j in range(tables['companies'].__len__()):
            if(tables['contacts'][i][0] == tables['companies'][j][6]):
                valorSetor[int(tables['companies'][j][9])-1] += valorContatos[tables['contacts'][i][1]]
    soma = sum(valorSetor)

    for i in range(0,valorSetor.__len__()):
        sector = tables['sectors'][i+1]
        valorSetor[i] = {"id":sector[0],"setor":sector[1],"representacao": str('%.2f' % (valorSetor[i]/soma))}

    def valor(val):
        return val['representacao']
    valorSetor.sort(key = valor, reverse=True)

    return valorSetor
