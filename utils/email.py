
import smtplib
import email.message

def enviar_email(nome_usuario,destinatario):
    corpo_email = f"""
    <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Confirmação de Registro</title>
</head>
<body>
    <h1>Confirmação de Registro</h1>
    <p>Olá {nome_usuario},</p>
    <p>Obrigado por se registrar em nosso aplicativo. Estamos animados em tê-lo a bordo!</p>
     <img src="https://diariodocomercio.com.br/wp-content/uploads/2020/02/investimento-72.jpg" alt="Descrição da imagem" width="200" height="200">
    <p>Se você não se registrou em nosso aplicativo, ignore este e-mail.</p>
    <p>Atenciosamente,</p>
    <p>Sua Equipe [NOME_DA_EMPRESA]</p>
</body>
</html>

    """

    msg = email.message.Message()
    msg['Subject'] = "Teste"
    msg['From'] = 'lucasfrotabarroso14@gmail.com'
    msg['To'] =  str(destinatario)
    password = 'cojlaheneeafhmmx'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')




