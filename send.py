# Importações

import smtplib
import urllib.request
import time
import getpass
import os
import sys

# Limpeza inicial, pode ser que o terminal esteje "sujo"
os.system("clear")

try:
	print("Verificando se você está conectado na internet...")
	time.sleep(1)
	connection = urllib.request.urlopen("https://www.google.com.br")

except urllib.error.URLError as erro:
	print("ERROR: Você não está conectado na internet :( ")

else:
	while True:
		os.system("clear")
		print("""
 ___                   _         __  __          _   _ 
/ __|  ___   _ _    __| |  ___  |  \/  |  __ _  (_) | |
\__ \ / -_) | ' \  / _` | |___| | |\/| | / _` | | | | |
|___/ \___| |_||_| \__,_|       |_|  |_| \__,_| |_| |_|              
			""")

		print("\033[1mImportante!!\033[m")
		print("""
Antes de usar esse programa, cheque algumas coisas:

1 - Confira e veja se a opçao "Acesso a app menos seguro"
está ativada!

2 - Confira se a autentiação de 2 fatores está desabilitada
afinal este script irá abrir o seu gmail/hotmail/yahoo para enviar
um e-mail.

			""")

		print("Se tudo está ok, digite Y para enviar e-mail.")
		print("Ou digite X para sair do programa!")
		tudo_ok = str(input(">>> ")).upper()
		while tudo_ok.strip() not in "Y" and tudo_ok.strip() not in "X":
			print("ERROR: Digite uma opção válida!")
			tudo_ok = str(input(">>> ")).upper()
		if tudo_ok == "Y":
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.starttls()
			froom = input("Digite seu e-mail: ")
			senha = getpass.getpass("Senha: ")
			conf = getpass.getpass("Confirme a senha: ")

			if senha == conf:
					server.login(froom, senha)
					to = input("E-mail para: ")
					msg = input("Assunto: ")
					print("Enviando email...")

					# Envia o E-mail
					server.sendmail(froom, to, msg)
						# Fecha o server
					server.quit()

					print("Email enviado com sucesso!\n")

					back = str(input("Deseja enviar mais algum e-mail? S/N: ")).upper()[0]

					# Válidação
					while back.strip() not in "S" and back.strip() not in "N":
						print("\nERROR: opção imválida!")
						back = str(input("Deseja enviar mais algum e-mail? S/N: ")).upper()[0]
					if back == "S":
						time.sleep(0.8)
					elif back == "N": 
						print("Saindo...")
						time.sleep(0.7)
						sys.exit()
			else:
				print("Senha incorreta, tente novamente!\n")

		elif tudo_ok == "X":
			print("Saindo...")
			time.sleep(1)
			sys.exit()


# Fim do script
