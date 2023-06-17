import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <h1>Boa Tarde, Michael aqui</h1>
    <h3>REFERENTE A EMPRESA X </h3>
    <p>Segue notas fiscais da empresa X com a numeracao de X</p>
    """

    msg = email.message.Message()
    msg['Subject'] = ""
    msg['From'] = 'mcialbr123@gmail.com'
    msg['To'] = 'mcialbr123@gmail.com'
    password = 'MINHA-SENHA'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


enviar_email()

