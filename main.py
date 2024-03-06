def ler_cnf(cnf):
    with open(cnf, 'r') as file:
        content = file.readlines()
    F = []
    for line in content:
        if line.startswith('c') or line.startswith('p'):
            continue
        clausula = list(map(int, line.split()[:-1]))
        F.append(clausula)
    return F

def simplifica(F):
    while True:
        encontrou_clausula_unitaria = False
        for c in F:
            if len(c) == 1:  
                encontrou_clausula_unitaria = True
                unitaria = c[0]
                break
        if not encontrou_clausula_unitaria: 
            break
        F = [c for c in F if unitaria not in c]  
        for c in F:  
            if -unitaria in c:
                c.remove(-unitaria)
    return F

def DPLL(F):
    F = simplifica(F)
    if [] in F:
        return "insatisfazível"
    if F == []:
        return "satisfazível"
    # Falta resto da lógica

def main():
    F = ler_cnf('aim-100-2_0-no-1.cnf') # Insira o nome do arquivo cnf
    result = DPLL(F)
    print(result)

if __name__ == "__main__":
    main()
