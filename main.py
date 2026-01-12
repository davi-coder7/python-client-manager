import random
import csv
import os
from datetime import datetime

def cadastrar_cliente():
    """Sistema de cadastro focado em automação e registro de dados para Freelance."""
    print("=== Bot de Cadastro de Clientes ===")
    
    try:
        nome = input("Nome do Cliente: ").strip()
        if not nome:
            print("❌ Erro: Nome obrigatório.")
            return

        idade = int(input("Idade: "))
        email = input("Email: ").strip() 

        # Gera dados automáticos
        numero_id = random.randint(1000, 9999)
        grupo = "Premium" if idade >= 18 else "Básico"
        data_registro = datetime.now().strftime("%d/%m/%Y %H:%M")

        # A MÁGICA: Salva no "Excel" (Arquivo CSV)
        salvar_em_csv(nome, email, idade, grupo, numero_id, data_registro)
        
        print(f"\n✅ Cliente {nome} salvo com sucesso no arquivo 'banco_de_dados.csv'!")

    except ValueError:
        print("❌ Erro: Digite apenas números na idade.")

def salvar_em_csv(nome, email, idade, grupo, uid, data):
    # Verifica se o arquivo já existe para não criar cabeçalho duplicado
    arquivo_existe = os.path.isfile('banco_de_dados.csv')
    
    with open('banco_de_dados.csv', 'a', newline='', encoding='utf-8') as arquivo:
        campos = ['ID', 'Nome', 'Email', 'Idade', 'Categoria', 'Data']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)

        if not arquivo_existe:
            escritor.writeheader() # Cria o cabeçalho (titulos das colunas)
        
        escritor.writerow({
            'ID': uid,
            'Nome': nome,
            'Email': email,
            'Idade': idade,
            'Categoria': grupo,
            'Data': data
        })

if __name__ == "__main__":
    while True:
        cadastrar_cliente()
        continuar = input("\nCadastrar outro? (s/n): ").lower()
        if continuar != 's':
            break
