import email
import imaplib
from email.message import EmailMessage
import mimetypes
from email import header
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from datetime import timedelta
import email.utils
import time
from email.utils import parsedate_to_datetime
from email.utils import parsedate_tz
import datetime
import config
#==============Define Functions to be Used=============================================================================
#Getting message body
def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else: 
        return msg.get_payload(None,True)
#==============ESTABLISH CONNECTION, LOGIN & RETRIEVE MESSAGES===========================================================
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(config.user,config.password)
mail.list()
mail.select('inbox')
mail.list()
mail.select("inbox") # connect to inbox.
result, data = mail.search(None, "ALL")
ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string
latest_email_id = id_list[-1] # get the latest

result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
raw_email = email.message_from_bytes(data[0][1]) # here's the body
#===============PULL OUT EMAIL OBJECTS NEEDED===============================================================================
body = get_body(raw_email)   # Assign variables to message parts
date = raw_email['Date']
sender = raw_email['From']
#=================FORMAT THE DATE TO ENSURE COMPATABILITY====================================================================
date_str= 'Sun, 28 Apr 2019 22:44:14 -0400'  # manipulate date formats and calculate reminder date
email= parsedate_to_datetime(date_str)
order_date_str =email.strftime("%Y-%m-%d")
order_date_date= datetime.datetime.strptime(order_date_str,"%Y-%m-%d")
OD= order_date_date
one_month_reminder = OD + datetime.timedelta(days= + 29)
two_week_reminder = OD + datetime.timedelta(days= + 13)
#==============CHECK EMAIL CONTENT FOR KEY WORD===============================================================================
def check():                                        #apply search term & continue
    if ( b'free trial' in body):
        return "Continue"
    else:
        print("No free trial")

test = check()
print(test)
#=========================Confirm Subcription & Run Logic=========================================================================
if (test == 'Continue'):
    subscription = input("(yes/no). Is this a subscription order you made?")     # confirm email is your subscription
    sub_response = subscription
    print(sub_response)
    if (sub_response == 'yes'):
        length =input('For how long?, one (month) or two (weeks)?')              # input length of subscription
        length_response = length
        print(length)
        if (length_response == 'one'):                                           
            time.sleep(5)                                                           #for demo in class
            user_email = 'c22oding@gmail.com'
            subject = 'Trial-End Reminder'                                          # construct message with following parts
            sub_provider = sender
            message = "Hello Mercy,\n\n This is a friendly reminder that your month-long free trial from " + sub_provider + " ends today.\n\n Best, \n\n Subscription Management Team"

            msg =MIMEMultipart()                                                     # input details of the messages components
            msg['To'] = user_email
            msg['From'] = user_email
            msg['Subject'] = subject
            msg['Body'] = message

            msg.attach(MIMEText(message,'plain'))
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()                                                       # connect with server and send email
            server.login(config.user,config.password)
            text = msg.as_string()
            server.sendmail(config.user,config.user,text)
            server.quit()
            #send_time = one_month_reminder
            #time.sleep(send_time.timestamp() - time.time())  #to set an actual reminder remember to del the timesleep from demo (line 91)
            print('email sent')

#==========================================================If Trial Is for Two-Weeks==================================================
        else:
            if (length_response == 'two'):                                                        #similar process but time is different
                time.sleep(5) #for demo in class #log into account & send the following message
                user_email = 'c22oding@gmail.com'
                subject = 'Trial-End Reminder'
                sub_provider = sender
                message = "Hello Mercy,\n\n This is a friendly reminder that your two-week-long free trial from " + sub_provider + " ends today.\n\n Best, \n\n Subscription Management Team"

                msg =MIMEMultipart()
                msg['To'] = user_email
                msg['From'] = user_email
                msg['Subject'] = subject
                msg['Body'] = message

                msg.attach(MIMEText(message,'plain'))


                server = smtplib.SMTP('smtp.gmail.com',587)
                server.starttls()
                server.login(config.user,config.password)
                text = msg.as_string()
                server.sendmail(config.user,config.user,text)
                server.quit()
                #send_time = two_week_reminder
                #time.sleep(send_time.timestamp() - time.time())  #to set an actual reminder remember to del the timesleep from demo (line 120)
                print("Email sent")
            else:
                print("Reminders available for one month & two weeks only")                     # for all other inputs

    else:
        print("Message is free-trial but is not Mercy's subsciption")

else:
    print("This message doesn't contain a free trial confirmation")    
       
#WELL DONE!