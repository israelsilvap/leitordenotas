from generateKey import generate_key
from dowloadPDF import download_pdf
from extractItems import extract_items
from payment_calculator import processar_pdf

def main():
    chave = generate_key()
    if chave:
        download_pdf(chave)
        produtos = extract_items(chave)
        valorIndividual = processar_pdf(produtos)
        print("\nValores a pagar por pessoa:")
        print(valorIndividual)

if __name__ == "__main__":
    main()
