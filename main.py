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

def main():
    F = ler_cnf('aim-100-2_0-no-1.cnf') # Insira o nome do arquivo cnf
    result = DPLL(F)
    print(result)

if __name__ == "__main__":
    main()
