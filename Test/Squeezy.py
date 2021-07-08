import smtplib
from email.mime.text import MIMEText

class Squeezy:

    #Constructor to initiate instance variable definitons 
    def __init__(self):
        
        self.sender = 'EMAIL@gmail.com'
        self.svrnm = 'smtp.gmail.com'
        self.port = '587'
        #self.port = '465' # for secure messages

    def emailBody(self, rc, cont, sub):
        #Defining the email body
        msg = MIMEText(cont)
        msg['From'] = self.sender
        msg['To'] = rc
        msg['Subject'] = str(sub)
        
        return msg
    
    def main(self):
        #Taking input from user
        receiver = input(str("enter email address: "))
        content = input(str("What do you want the email to say: "))
        subject = input(str("What do you want the Subject to be: "))

        #Generating email
        msg = self.emailBody(receiver, content, subject)

        #Initiating server variable based on port number
        if self.port == '465':
            server = smtplib.SMTP_SSL('{}:{}'.format(self.svrnm, self.port))
        else :
            server = smtplib.SMTP('{}:{}'.format(self.svrnm, self.port))
            server.starttls() # this is for secure reason

        #Login to gmail account to send email from
        server.login(self.sender, "PASSWORD_HERE")
        #Send email
        server.send_message(msg)
        #Close server connection
        server.quit()
    
if __name__ == "__main__":
    squeez = Squeezy()
    squeez.main()



