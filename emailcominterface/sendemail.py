import tkinter as tk
import win32com.client as win32

def enviar_email():
    outlook = win32.Dispatch("Outlook.Application")
    
    lista_email = entry_emails.get().split(',')
    assunto = entry_assunto.get()
    corpo = entry_corpo.get("1.0", "end-1c")

    for email in lista_email:
        message = outlook.CreateItem(0)
        message.To = email
        message.Subject = assunto
        message.Body = corpo
        message.Send()

    label_status["text"] = "E-mails enviados com sucesso!"

# Cria a janela principal
window = tk.Tk()
window.title("Enviar E-mails")
window.geometry("400x300")

# Cria os widgets
label_emails = tk.Label(window, text="E-mails:")
label_emails.pack()
entry_emails = tk.Entry(window, width=40)
entry_emails.pack()

label_assunto = tk.Label(window, text="Assunto:")
label_assunto.pack()
entry_assunto = tk.Entry(window, width=40)
entry_assunto.pack()

label_corpo = tk.Label(window, text="Corpo:")
label_corpo.pack()
entry_corpo = tk.Text(window, width=40, height=6)
entry_corpo.pack()

button_enviar = tk.Button(window, text="Enviar", command=enviar_email)
button_enviar.pack()

label_status = tk.Label(window, text="")
label_status.pack()

# Inicia o loop principal da janela
window.mainloop()
