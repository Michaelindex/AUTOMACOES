#AQUI APENAS UM EMAIL CONVENCIONAL

#import win32com.client as win32
#
#outlook = win32.Dispatch("Outlook.Application")
#message = outlook.CreateItem(0)
#message.Display()
#message.To = "mcialbr123@gmail.com"
#message.Subject = "AQUI O ASSUNTO"
#body = """
#<h1>Michael</h1>
#<p>Teste Teste</p>
#"""
#
#message.HTMLBody = body


#AQUI DISPARANDO PARA VAIOS EMAILS EM lista_email

import win32com.client as win32
outlook = win32.Dispatch("Outlook.Application")

lista_email = ['mcialbr123@gmail.com', 'mcialbr1234@gmail.com', 'mcialbr1234@hotmail.com']

for email in lista_email:
    message = outlook.CreateItem(0)
    message.Display()
    message.To = email
    message.Subject = "AQUI O ASSUNTO"
    body = """
    <h1>Michael</h1>
    <p>Teste Teste</p>
    """

    message.HTMLBody = body
    #PARA ENVIAR DEVE COLOCAR - message.Send()