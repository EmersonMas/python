import requests

# URL do webhook do Make
url = "https://hook.us1.make.com/brfudnh1t8pbeaeg55neqiqd95g550tn"

# Dados do formulário
data = {
    "Nome": "Seu Nome",
    "Id": "123456",
    "Email": "seuemail@dominio.com",
    "Agente": "Nome do Agente",
    "Protocolo": "Protocolo123",
    "Tipo de demanda": "Tipo da Demanda",
    "Descrição": "Descrição detalhada da demanda"
}

# Arquivos a serem enviados
files = {
    "file1": ("documento.pdf", open("caminho/para/documento.pdf", "rb"), "application/pdf"),
    "file2": ("imagem.jpeg", open("caminho/para/imagem.jpeg", "rb"), "image/jpeg")
}

# Enviando o formulário com os dados e arquivos
response = requests.post(url, data=data, files=files)

# Verificando a resposta do servidor
if response.status_code == 200:
    print("Dados enviados com sucesso!")
else:
    print(f"Erro ao enviar dados: {response.status_code} - {response.text}")
