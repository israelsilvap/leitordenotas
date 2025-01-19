import fitz  # PyMuPDF
import re
import pandas as pd

def extract_items(chave):
    # Caminho para o PDF
    pdf_path = f"D:/Israel/Documents/Projetos/leitordenotas/downloads/{chave}.pdf"

    # Abrir o PDF
    doc = fitz.open(pdf_path)

    # Variável para armazenar todo o texto do PDF
    texto_completo = ""

    # Iterar pelas páginas e extrair o texto
    for page_num in range(len(doc)):
        page = doc[page_num]
        texto_completo += page.get_text()

    # Fechar o documento
    doc.close()

    # Salvar o texto extraído em um arquivo de texto
    output_file = f"D:/Israel/Documents/Projetos/leitordenotas/downloads/{chave}_output.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(texto_completo)

    # Remover linhas desnecessárias como "Extrato No."
    texto_filtrado = "\n".join(
        line for line in texto_completo.splitlines() if not re.match(r"^[A-Za-z]", line)
    )

    # Regex para capturar os produtos e valores
    padrao = re.compile(
        r"(?P<codigo>\d{3})\s+(?P<id>\d+)\s+(?P<descricao>.+?)\s+(?P<qtd>\d+\.?\d*\s+\w+)\s+X\s+"
        r"(?P<vl_un>\d+,\d+).+?\n(?P<vl_item>\d+,\d+)"
    )

    # Lista para armazenar os resultados
    produtos = []

    # Buscar todas as correspondências no texto extraído
    for match in padrao.finditer(texto_filtrado):
        produto = {
            "Código": match.group("codigo"),
            "ID": match.group("id"),
            "Descrição": match.group("descricao").strip(),
            "Quantidade": match.group("qtd").strip(),
            "Valor Unitário": match.group("vl_un").strip(),
            "Valor Total": match.group("vl_item").strip(),
        }
        produtos.append(produto)

    # Criar um DataFrame com os produtos
    df_produtos = pd.DataFrame(produtos)

    # Remover as colunas "Código" e "ID"
    df_produtos = df_produtos.drop(columns=["Código", "ID"])

    # Retornar o DataFrame final
    return df_produtos
