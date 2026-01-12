import random

def cadastrar_cliente():
    print("=== Sistema de Cadastro de Clientes ===")
    
    try:
        nome = input("Digite seu nome: ").strip()
        if not nome:
            print("❌ Erro: O nome não pode estar vazio.")
            return

        idade = int(input("Digite sua idade: "))
        
        # Gera um ID aleatório entre 1000 e 9999
        numero_id = random.randint(1000, 9999)
        
        # Define a categoria baseada na idade
        grupo = "Premium" if idade >= 18 else "Básico"

        print("\n✅ Cadastro realizado com sucesso!")
        print(f"👤 Nome: {nome}")
        print(f"🎂 Idade: {idade}")
        print(f"🆔 ID Cliente: {numero_id}")
        print(f"⭐ Categoria: {grupo}")

    except ValueError:
        print("❌ Erro: Por favor, insira um número válido para a idade.")

if __name__ == "__main__":
    cadastrar_cliente()
