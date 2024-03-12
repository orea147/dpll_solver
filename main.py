def ler_cnf(arquivo_cnf):
    # Abre o arquivo CNF e lê suas linhas
    with open(arquivo_cnf, 'r') as arquivo:
        linhas = arquivo.readlines()
    clausulas = []
    # Processa cada linha do arquivo CNF
    for linha in linhas:
        # Ignora linhas de comentário e declaração do problema
        if linha.startswith('c') or linha.startswith('p'):
            continue
        # Converte a linha em uma cláusula e adiciona à lista de cláusulas
        clausula = list(map(int, linha.split()[:-1]))
        clausulas.append(clausula)
    return clausulas

def simplifica(clausulas):
    # Simplifica a fórmula CNF removendo cláusulas unitárias e simplificando cláusulas que contêm o literal unitário.
    while True:
        encontrou_clausula_unitaria = False
        # Verifica se há cláusulas unitárias
        for c in clausulas:
            if len(c) == 1:  
                encontrou_clausula_unitaria = True
                unitaria = c[0]
                break
        if not encontrou_clausula_unitaria: 
            break
        # Remove cláusulas que contêm o literal unitário e simplifica as cláusulas restantes
        clausulas_temp = []
        for c in clausulas:
            if unitaria not in c:
                clausulas_temp.append(c)
        for c in clausulas_temp:  
            if -unitaria in c:
                c.remove(-unitaria)
        clausulas = clausulas_temp
    return clausulas

def DPLL(clausulas):
    # Simplifica a fórmula CNF antes de começar
    clausulas = simplifica(clausulas)
    # Verifica se a fórmula é insatisfatível ou satisfatível
    if [] in clausulas:
        return "insatisfazível"
    if clausulas == []:
        return "satisfazível"

    x = None
    # Encontra um literal não atribuído
    for c in clausulas:
        for l in c:
            if l != 0:
                x = l
                break
        if x is not None:
            break

    if x is None:
        return "insatisfazível"

    clausulas1 = []
    # Faz a atribuição verdadeira do literal x e simplifica a fórmula
    for c in clausulas:
        if x not in c:
            nova_clausula = []
            for l in c:
                if l != -x:
                    nova_clausula.append(l)
            clausulas1.append(nova_clausula)

    # Verifica se a fórmula simplificada é satisfatível
    if DPLL(clausulas1) == "satisfazível":
        return "satisfazível"

    clausulas2 = []
    # Faz a atribuição falsa do literal x e simplifica a fórmula
    for c in clausulas:
        if -x not in c:
            nova_clausula = []
            for l in c:
                if l != x:
                    nova_clausula.append(l)
            clausulas2.append(nova_clausula)

    # Verifica se a fórmula simplificada é satisfatível
    if DPLL(clausulas2) == "satisfazível":
        return "satisfazível"

    return "insatisfazível"

def main():
    # Lê as cláusulas do arquivo CNF e chama o algoritmo DPLL para determinar a satisfatibilidade
    clausulas = ler_cnf('aim-100-2_0-no-1.cnf')
    resultado = DPLL(clausulas)
    print(resultado)

if __name__ == "__main__":
    main()
