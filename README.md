# 📄 Leitor de Notas

Este projeto é um leitor de notas fiscais que extrai informações de um PDF, permite a edição dos valores dos produtos e calcula o valor a ser pago por cada responsável.

## ✨ Funcionalidades

- 📷 Leitura de código de barras usando a câmera.
- 📥 Download automático de PDFs de notas fiscais.
- 📄 Extração de itens e valores do PDF.
- ✏️ Edição dos valores dos produtos.
- 👥 Atribuição de responsáveis pelo pagamento dos produtos.
- 💰 Cálculo do valor total a ser pago por cada responsável.

## 📂 Estrutura do Projeto

- `generateKey.py`: Captura o código de barras usando a câmera.
- `dowloadPDF.py`: Faz o download do PDF da nota fiscal usando a chave capturada.
- `extractItems.py`: Extrai os itens e valores do PDF.
- `payment_calculator.py`: Processa os dados extraídos, permite a edição dos valores e calcula o valor a ser pago por cada responsável.
- `main.py`: Script principal que orquestra a execução das funcionalidades.

## 🚀 Como Usar

1. Execute o script `main.py`.
2. Aponte a câmera para o código de barras da nota fiscal.
3. O script fará o download do PDF da nota fiscal.
4. Os itens e valores serão extraídos do PDF.
5. Você poderá editar os valores dos produtos, se necessário.
6. Atribua os responsáveis pelo pagamento de cada produto.
7. O valor total a ser pago por cada responsável será calculado e exibido.

## 🛠️ Requisitos

- Python 3.x
- Bibliotecas: 
    - `fitz (PyMuPDF)` 
    - `re` 
    - `pandas` 
    - `cv2 (OpenCV)` 
    - `pyzbar` 
    - `selenium`
    - `webdriver_manager`

## 📦 Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/israelsilvap/leitordenotas.git
    cd leitordenotas
    ```
2. Instale as dependências usando o Poetry:
    ```sh
    poetry install
    ```
3. (Opcional) Ative o ambiente virtual do Poetry:
    ```sh
    poetry shell
    ```
4. Execute o projeto:
    ```sh
    poetry run python main.py
    ```

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
