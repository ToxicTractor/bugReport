## this file is part of Ren'Py plug-in "bugReport" by ToxicTractor
## the project can be found here on GitHub:
## https://github.com/ToxicTractor/bugReport/tree/main

SENDER = "sender@gmail.com"
PASSWORD = "app-password"
RECEIVER = "receiver@gmail.com"
HOST = "smtp.gmail.com"
PORT = 465

def AttemptSend(mail, onComplete):
    import threading

    ## start a thread that attempts to send the email via smtp
    t = threading.Thread(target=ThreadedSendSMTP, args=(mail, onComplete))
    t.start()

def ThreadedSendSMTP(mail, onComplete):
    import ssl
    from smtplib import SMTPConnectError
    from smtplib import SMTP_SSL

    ## set up needed variables
    success = False
    errorMessage = None
    
    ## set the sender and receiver of the mail
    mail['From'] = RECEIVER
    mail['To'] = SENDER

    ## try to connect to the smpt server
    try:
        context = ssl._create_unverified_context()
        with smtplib.SMTP_SSL(HOST, PORT, context=context) as client:
            client.login(SENDER, PASSWORD)
            client.sendmail(SENDER, RECEIVER, mail.as_string())
    ## if something went wrong we set the error message
    except:
        errorMessage = "An error occured. Bug report was not sent."
    ## if nothing went wrong we set success to true
    else:
        success = True
    ## finally we call the onComplete callback method
    finally:
        onComplete(success, errorMessage)