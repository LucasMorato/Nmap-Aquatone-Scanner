import argparse
import os

def run_aquatone(site, flag):
    nmap_command = f"nmap {'-' if flag[0] != '-' else ''}{flag} -oX {site}.xml {site}"
    cat_command = f"cat {site}.xml | aquatone"

    # Executa o comando nmap com a flag -oX e a flag fornecida pelo usuário
    os.system(nmap_command)

    # Executa o comando cat com o pipe para o comando aquatone
    os.system(cat_command)

if __name__ == "__main__":
    # Cria um parser de argumentos
    parser = argparse.ArgumentParser(description="Script para executar comandos relacionados ao site")

    # Adiciona o argumento --site
    parser.add_argument("--site", type=str, help="Nome do site")

    # Adiciona o argumento --flag como obrigatório
    parser.add_argument("--flag", type=str, required=True, help="Flag para o comando nmap")

    # Faz o parse dos argumentos da linha de comando
    args = parser.parse_args()

    # Remove o traço da flag se estiver presente
    flag = args.flag.lstrip("-")

    # Verifica se o argumento --site foi fornecido
    if args.site:
        run_aquatone(args.site, flag)
    else:
        print("É necessário fornecer o nome do site através do argumento --site.")
