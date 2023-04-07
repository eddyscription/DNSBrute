#!/usr/bin/env python3
import sys
import dns.resolver

# Verifica se os argumentos foram fornecidos corretamente
if len(sys.argv) != 3:
    print("Uso: {} <dominio> <arquivo>".format(sys.argv[0]))
    sys.exit(1)

# Obtém o nome do domínio alvo e o nome do arquivo de lista de palavras a partir dos argumentos de linha de comando
dominio = sys.argv[1]
arquivo = sys.argv[2]

try:
    # Abre o arquivo de lista de palavras e armazena as linhas em uma lista
    with open(arquivo) as f:
        linhas = f.read().splitlines()
except FileNotFoundError:
    print("Arquivo não encontrado: {}".format(arquivo))
    sys.exit(1)

# Itera por cada linha na lista de palavras
for linha in linhas:
    # Gera um subdomínio concatenando a linha com o nome do domínio alvo
    subdominio = linha + '.' + dominio
    try:
        # Realiza uma consulta DNS para o subdomínio gerado
        respostas = dns.resolver.resolve(subdominio, 'A')
        # Imprime o subdomínio e o endereço IP correspondente
        for resultado in respostas:
            print(subdominio, resultado)
    except dns.resolver.NXDOMAIN:
        # Se o nome de domínio não existir, passa para o próximo subdomínio
        pass
    except dns.resolver.NoAnswer:
        # Se não houver resposta DNS para o subdomínio, passa para o próximo subdomínio
        pass

# Pausa o programa para permitir que o usuário visualize a saída antes de sair
input('#')
