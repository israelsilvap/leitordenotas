import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def download_pdf(chave):
    print("Iniciando nosso robo...\n")

    # Diretório para salvar o PDF
    download_dir = os.path.join(os.getcwd(), "downloads")  # Salvar no diretório atual em uma pasta "downloads"
    os.makedirs(download_dir, exist_ok=True)  # Criar o diretório se não existir

    # Configuração do navegador para download automático
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": download_dir,  # Configurar o diretório de download
        "download.prompt_for_download": False,       # Desativar o prompt de download
        "plugins.always_open_pdf_externally": True   # Abrir PDF diretamente no sistema de arquivos
    }
    options.add_experimental_option("prefs", prefs)

    # Configuração do driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Navegando até o site para baixar o PDF
        driver.get("https://cfe.sefaz.ce.gov.br/mfe/servicos#/cupom-fiscal")
        time.sleep(5)  # Esperar o carregamento inicial da página

        # Localizando o campo de entrada para a chave de 44 caracteres
        expected_file = os.path.join(download_dir, f"{chave}.pdf")

        # Excluir o arquivo existente, se houver
        if os.path.exists(expected_file):
            os.remove(expected_file)
            print(f"Arquivo existente '{expected_file}' foi excluído para evitar duplicação.")

        chave_input = driver.find_element(By.CSS_SELECTOR, "input[ng-model='formData.cfeKey']")
        chave_input.clear()
        chave_input.send_keys(chave)
        print(f"Chave '{chave}' foi inserida com sucesso.")

        # Localizar e alternar para o iframe do reCAPTCHA
        recaptcha_iframe = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src*='recaptcha']"))
        )
        driver.switch_to.frame(recaptcha_iframe)
        print("Mudança para o iframe do reCAPTCHA bem-sucedida.")

        # Monitorar a validação do reCAPTCHA
        WebDriverWait(driver, 300).until(
            lambda d: d.find_element(By.ID, "recaptcha-anchor").get_attribute("aria-checked") == "true"
        )
        print("reCAPTCHA validado com sucesso.")

        # Voltar ao contexto principal
        driver.switch_to.default_content()

        # Localizar o botão "Consultar" e clicar nele
        consultar_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.btn.btn-success[ng-click='showFiscalCouponExtractPopup(formData.cfeKey)']")
            )
        )
        consultar_button.click()
        print("Botão 'Consultar' clicado com sucesso.")

        # Localizar o botão "Download PDF" e clicar nele
        download_pdf_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[ng-click='downloadPDF()']"))
        )
        download_pdf_button.click()
        print("Botão 'Download PDF' clicado com sucesso.")

        # Monitorar o download do arquivo
        while True:
            files_in_dir = os.listdir(download_dir)
            if f"{chave}.pdf" in files_in_dir:
                print(f"Arquivo '{chave}.pdf' baixado com sucesso.")
                break
            elif any(file.endswith(".crdownload") for file in files_in_dir):
                print("Download em andamento...")
            else:
                print("Aguardando início do download...")
            time.sleep(1)  # Verificar a cada segundo

    finally:
        # Fechando o navegador
        print("Fechando o navegador...")
        driver.quit()
