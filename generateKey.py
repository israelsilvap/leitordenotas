import cv2
from pyzbar.pyzbar import decode

def generate_key():
    # Inicializar a câmera
    cap = cv2.VideoCapture(0)  # Use 0 para a câmera padrão

    if not cap.isOpened():
        print("Erro ao acessar a câmera.")
        return None

    print("Aguardando leitura do código de barras...")

    barcode_data = None  # Variável para armazenar os dados do código de barras

    while True:
        # Capturar frame da câmera
        ret, frame = cap.read()
        if not ret:
            print("Falha ao capturar a imagem. Verifique a câmera.")
            break

        # Detectar e ler códigos de barras
        decoded_objects = decode(frame)
        for obj in decoded_objects:
            # Armazenar os dados do código de barras
            barcode_data = obj.data.decode("utf-8")
            barcode_type = obj.type

            # Exibir o tipo e os dados no console
            print(f"Tipo: {barcode_type}, Dados: {barcode_data}")

            # Salvar o frame como uma imagem usando o código de barras como nome
            file_name = f"D:\Israel\Documents\Projetos\leitordenotas\img\{barcode_data}.jpg"
            cv2.imwrite(file_name, frame)
            print(f"Frame salvo como: {file_name}")

            # Fechar o loop após encontrar o primeiro código de barras
            break

        # Se o código de barras foi encontrado, encerrar
        if barcode_data:
            break

        # Mostrar o vídeo ao vivo enquanto aguarda o código
        cv2.imshow("Câmera - Leitor de Código de Barras", frame)

        # Sair com 'q' (como backup)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Encerrado pelo usuário.")
            break

    # Liberar recursos
    cap.release()
    cv2.destroyAllWindows()

    # Exibir o resultado final após o fechamento da janela
    if barcode_data:
        print(f"\nLeitura finalizada com sucesso!\nCódigo de Barras Lido: {barcode_data}")
        return barcode_data
    else:
        print("Nenhum código de barras foi detectado.")
        return None
