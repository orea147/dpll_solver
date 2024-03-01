def main():
    F = ler_cnf('aim-100-2_0-no-1.cnf') # Insira o nome do arquivo cnf
    result = DPLL(F)
    print(result)

if __name__ == "__main__":
    main()
