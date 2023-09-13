#############################################################################################################
# This file is not supposed to be in any releases of a game. It contains the app password for the senders 
# email and should therefore only include the compiled version of this script.
############################################################################################################# 

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
    import smtplib, ssl

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
    ## if we cannot connect we give one error message
    except SMTPConnectError:
        errorMessage = "Unable to connect to the server. Please check your internet connection!"
    ## if something went wrong we give another error message
    except:
        errorMessage = "An error occured. Bug report was not sent."
    ## if nothing went wrong we set success to true
    else:
        success = True
    ## finally we call the onComplete callback method
    finally:
        onComplete(success, errorMessage)