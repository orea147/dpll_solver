# Relatório: Solver de Satisfatibilidade CNF (DPLL)
Este relatório visa fornecer uma explicação detalhada do código Python que implementa o algoritmo DPLL (Davis-Putnam-Logemann-Loveland) para resolver problemas de satisfatibilidade em forma normal conjuntiva (CNF).

# Resumo

O código consiste em três funções principais:

**1- ler_cnf(arquivo_cnf):** Lê um arquivo CNF e retorna uma lista de cláusulas.

**2- simplifica(clausulas):** Simplifica uma fórmula CNF removendo cláusulas unitárias e simplificando cláusulas que contêm o literal unitário.

**3- DPLL(clausulas):** Implementa o algoritmo DPLL para determinar a satisfatibilidade de uma fórmula CNF.

Além disso, há uma função **main()** que lê um arquivo CNF especificado e chama o algoritmo DPLL para resolver o problema.

# Detalhes das funções

### ler_cnf(arquivo_cnf):
Esta função recebe o nome de um arquivo CNF como entrada e retorna uma lista de cláusulas. Ela lê o arquivo linha por linha, ignorando linhas de comentário e declaração do problema, e converte as linhas restantes em cláusulas representadas por listas de inteiros.

### simplifica(clausulas):
A função "simplifica" remove cláusulas unitárias e simplifica cláusulas que contêm o literal unitário. Ela itera sobre as cláusulas, identifica cláusulas unitárias e simplifica a fórmula CNF removendo cláusulas que contêm o literal unitário e removendo o literal negado do literal unitário das cláusulas restantes.

### DPLL(clausulas):
Esta função implementa o algoritmo DPLL para determinar a satisfatibilidade de uma fórmula CNF. Ela primeiro simplifica a fórmula CNF, verificando se a fórmula é insatisfatível ou satisfatível. Em seguida, itera sobre os literais não atribuídos, fazendo atribuições verdadeiras e falsas, e recursivamente simplifica a fórmula até que uma solução seja encontrada ou a fórmula seja considerada insatisfatível.

# Funcionamento do programa
O programa começa chamando a função main(), que lê um arquivo CNF especificado e chama o algoritmo DPLL para resolver o problema de satisfatibilidade. O resultado é impresso na saída padrão.

# Uso
Para usar o programa, basta rodar o arquivo dpll_solver.py em um ambiente Python, fornecendo o arquivo CNF como argumento. Por exemplo:

Isso imprimirá se a fórmula CNF é satisfatível ou insatisfatível.

Certifique-se de ter o Python instalado e acessível no seu ambiente para executar o programa.

# Conclusão
O código implementa com sucesso o algoritmo DPLL para resolver problemas de satisfatibilidade CNF. Ele fornece uma solução eficiente e escalável para determinar a satisfatibilidade de fórmulas CNF complexas.

Este relatório fornece uma visão geral do funcionamento do código e deve ajudar na compreensão de como o algoritmo DPLL é implementado em Python.
