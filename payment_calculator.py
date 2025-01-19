import fitz  # PyMuPDF
import re
import pandas as pd

def processar_pdf(df_produtos):
    # Perguntar se há algum produto para editar
    while True:
        # Mostrar os produtos atuais
        print(df_produtos)

        editar = input("\nHá algum produto que você deseja editar o valor? (s/n): ").strip().lower()
        if editar == 's':
            try:
                indice = int(input("Digite o número do produto que deseja editar: "))
                if 0 <= indice < len(df_produtos):
                    novo_valor = input("Digite o novo valor (use vírgula para decimais): ").strip()
                    df_produtos.at[indice, "Valor Total"] = novo_valor
                    print("Valor atualizado com sucesso!")
                else:
                    print("Número do produto inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
        elif editar == 'n':
            break
        else:
            print("Opção inválida. Responda com 's' ou 'n'.")

    # Mostrar os produtos após a possível edição
    print("\nProdutos atualizados:")
    print(df_produtos)

    # Adicionar uma nova coluna "Responsável" com base na entrada do usuário
    responsaveis = []

    # Iterar pelos produtos e perguntar ao usuário quem vai pagar
    for _, row in df_produtos.iterrows():
        print(f"\nProduto: {row['Descrição']}, Quantidade: {row['Quantidade']}, Valor Total: R$ {row['Valor Total']}")
        responsavel = input("Quem será o responsável pelo pagamento desse produto? ")
        responsaveis.append(responsavel)

    # Adicionar a coluna "Responsável" ao DataFrame
    df_produtos["Responsável"] = responsaveis

    # Mostrar o DataFrame final
    print("\nTabela final:")
    print(df_produtos)

    # Converter os valores monetários para float
    df_produtos["Valor Total"] = df_produtos["Valor Total"].str.replace(",", ".").astype(float)

    # Dicionário para acumular os valores que cada pessoa deve pagar
    valores_por_pessoa = {}

    # Iterar pelas linhas do DataFrame para calcular os valores
    for _, row in df_produtos.iterrows():
        # Dividir os responsáveis, normalizar os nomes (remover espaços e usar minúsculas)
        responsaveis = [responsavel.strip().upper() for responsavel in row["Responsável"].split("/")]
        responsaveis = list(filter(None, responsaveis))  # Remove entradas vazias
        valor_por_responsavel = row["Valor Total"] / len(responsaveis)  # Dividir o valor total pelo número de responsáveis

        # Somar o valor para cada responsável
        for responsavel in responsaveis:
            if responsavel in valores_por_pessoa:
                valores_por_pessoa[responsavel] += valor_por_responsavel
            else:
                valores_por_pessoa[responsavel] = valor_por_responsavel

    # Exibir os resultados organizados
    df_valores_por_pessoa = pd.DataFrame(list(valores_por_pessoa.items()), columns=["Responsável", "Valor a Pagar"])
    df_valores_por_pessoa["Valor a Pagar"] = df_valores_por_pessoa["Valor a Pagar"].round(2)

    return df_valores_por_pessoa


