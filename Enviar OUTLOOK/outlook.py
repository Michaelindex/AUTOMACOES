import win32com.client as win32

outlook = win32.Dispatch("Outlook.Application")
message = outlook.CreateItem(0)
message.Display()
message.To = "" #PARA QUEM
message.Cc = ""   #COM COPIA
message.Bcc = ""   #COM COPIA OCULTA
message.Subject = "" #AQUI O ASSUNTO
body = """
<h1>Michael</h1>
<p>Teste Teste</p>
"""

message.HTMLBody = body
#PARA ENVIAR DEVE COLOCAR - message.Send()


#AQUI DISPARANDO PARA VAIOS EMAILS EM lista_email

import win32com.client as win32
outlook = win32.Dispatch("Outlook.Application")

lista_email = ['mcialbr123@', 'mcialbr1234@', 'mcialbr1234@']

for email in lista_email:
    message = outlook.CreateItem(0)
    message.Display()
    message.To = email
    message.Cc = "mcialbr123@"   # COM COPIA
    #message.Bcc = emails COM COPIA OCULTA 
    message.Subject = "AQUI O ASSUNTO"
    body = """
    <h1>Michael</h1>
    <p>Teste Teste</p>
    """

    message.HTMLBody = body
    message.Send()