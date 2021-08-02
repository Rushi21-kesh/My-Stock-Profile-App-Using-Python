import smtplib
import logging as lg

# create a log
lg.basicConfig(filename='otp_sender_log.log',filemode='a',level=lg.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

def mail_send(reciever, otp):
    """ This function helps to generate OTP. """
    try:
        sender_id = "enter mail id"
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(sender_id, "generate access code from gmail and pass here")
        # sending the mail
        server.sendmail(sender_id, reciever, str(otp))
        print("Check mail ...")
        lg.info("\tOTP send to : " + reciever)
        server.quit()
    except Exception as e:
        lg.error('User '+reciever +' get an error : \n\t\t'+str(e))
