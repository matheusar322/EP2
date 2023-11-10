valor = True
i=0
soma1=0
soma2=0
lista1=[]
lista2=[]

while valor:
    desejados = input('Valor desejado:')
    vendas = input('Valor da venda:')
    if desejados == '' or vendas == '':
        x =0
        somatoria1 = 0
        somatoria2 = 0
        while x<len(lista1):
            somatoria1 += (lista1[x]-soma1/i)**2
            somatoria2 += (lista2[x]-soma2/i)**2
            x+=1
        s1 = (1/(i-1)*somatoria1)**0.5
        s2 = (1/(i-1)*somatoria2)**0.5
        print('MÉDIA: desejado [{0:.2f}] venda [{1:.2f}]'.format(soma1/i , soma2/i))
        print('DESVIO PADRÃO AMOSTRAL: desejado [{0:.2f}] venda [{1:.2f}]'.format(s1,s2))
        y = 0
        somadst = 0
        while y < len(lista1):
            somadst += (lista1[y]-lista2[y])**2
            y+=1
        dst =(1/i*somadst)**0.5
        if dst > 0.05*(soma1 + soma2)/(2*i):
            print('Anomalia: SIM')
        else:
            print('Anomalia: NÃO')
        valor = False
    else:
        desejado = float(desejados)
        venda = float(vendas)
        if desejado > venda:
            print('entradas desconsideradas pois valor desejado maior que o valor da venda, tente novamente!')
        elif venda >= desejado:
            i+=1
            soma1+= desejado
            soma2+= venda
            lista1.append(desejado)
            lista2.append(venda)