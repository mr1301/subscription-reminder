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
def interval(x,y):
    return x+y
  
