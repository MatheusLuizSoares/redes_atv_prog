import socket,os,sys

HOST = ''
PORT = 50000
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind((HOST, PORT))

print("Servidor está ouvindo...")
# O Serviodr está online
while True:
  data, endereco = udpSocket.recvfrom(1024)
  arquivo = data.decode()
  print(f"Pedido recebido para o arquivo: {arquivo}")
    
  if arquivo == '0':
     print('Saindo do programa...')
     sys.exit()
     #caso o cliente queira sair do programa
  caminho_arquivo = os.path.join('arquivos', arquivo)
  #

  try:
   with open(caminho_arquivo, 'r') as f:
    conteudo = f.read()
    udpSocket.sendto(conteudo.encode(), endereco)
    print(f"Conteúdo do arquivo '{arquivo}' enviando para {endereco}")
  except FileNotFoundError:
    erro = "Arquivo não encontrado."
    udpSocket.sendto(erro.encode(), endereco)
    print(f"Arquivo '{arquivo}' não encontrado! A Mensagem de erro enviada para {endereco}")
            
            


