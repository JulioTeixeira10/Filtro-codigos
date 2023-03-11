with open("codigos.txt") as t:
    file = t.readlines()
    ls = []
    for row in file:      
        if row[0] != '7' and row[0] != '8':
            ls.append(row[0])
            print("ERRO NO PRIMEIRO DIGITO: ",ls, row)
        if len(row) != 8:
            print("ERRO NA QUANTIDADE DE DIGITOS: ",len(row), row)