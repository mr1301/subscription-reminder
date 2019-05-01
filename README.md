#Subscription-Reminder
This app will help you remember to cancel your free-trial online subscriptions before payment day by reading your incoming emails, identifying free-trial confirmations and sending you reminders before the free trial ends.

#Configuration

Rerequisites
To use this app you will need to provide an email from which you receive your subscription emails.
You will also need to provide a password

A.Read Email
To read emails from your account you will need to import the following packages and modules: imaplib, emailmessage and emailutils. The imaplib utility helps the command line access your email server, the email utility pulls your emails and their different components, while the config utility reads your sensitive account password from a separate config.py file. As a default the running the code provides the latest email
    Step 1. open the config.py file
    step 2. insert your email account and password under the respective keys
    step 3. Run the code from "define functions" until "pull email components" to see if the app can access and read your email account
    step 4. The results should be the most recent email's body, timestamp, and sender


B.Logic & Condition
From the email pulled in A, this section searches for the terms "free trial" in the body of the email. These terms are the default but can be changed. If the terms are found in the email the code asks the user to confirm that this is a free trial using an input value of "yes" or "no." If confirmed, the logic fruther askes how long the trial is -- this app can only provide reminders for two weeks or a month. user can enter either "one" or "two". If the email read doesn't contain the search term, isn't a subscription or does not meet the term limits, a message is sent notifying the user.
    Step 1. Keep search term on "free trial" or change it.
    step 2. Confirm is matching message is a subscription with a yes or no
    step 3. Confirm the length of the submission

Notes: Having the input query after the app makes the search is optional. However this was made the default to ensure that the app had a high accurary rate, and didn't spam the user with false reminders. If the user is using a work email or an email the user is confident doesn't receive a lot of messages/advertisements for free trials unless they have subscribed, the user should comment out this part or delete the input query altogether and have the app send reminders automatically without prior confirmation.

C.Send Email
To send emails this app uses the Smtp, mimetypes and mime.multipart packages to access the server, write the different components of the email and send them. The app uses the config utility to read the config.py file once again for the account details. An email sent if the user confirms above that the text is in fact a subscription. The date for when to send the reminder was calculated under the "format date" section. It was pulled from the confirmation email, and 29 or 13 days where added to it depending on the trial. The utilties that helped pull and format it where the time and datetime modules. 

To test the code a different sleep time was used for the reminder. When using app comment out the demo sleep time.

  Step 1. use current sleep time demo to check if the app works.
  step 2. comment out the demo sleep time and let the app set reminder
  step 3. check email on day of reminder

#Installation
To install the file:
  1.Download the repository from Github
  2.Follow the configuration instructions from the READme using your on your command line.

#Files
  READme.md
  LICENSE.md
  Requirements.txt - this file contains a description of the app and it's functionality
  Config.py - this file will contain your email and password
  Subscription.py - this file contains the application code
  my_test.py

#Built with
Anaconda
Mac Terminal
Python
Pip
& packages listed under configuration

#Testing & Bugs


#Authors
Mercy Radithupa 

#Copy right & licensing
This project is licensed under the MIT License - see the LICENSE.md file for details





#Acknowledgements & credits
https://stackoverflow.com/questions/52022134/how-do-i-schedule-an-email-to-send-at-a-certain-time-using-cron-and-smtp-in-pyt
https://stackoverflow.com/questions/52326434/mails-send-if-condition-is-true-using-python-code
https://automatetheboringstuff.com/chapter16/
https://stackoverflow.com/questions/1790795/parsing-date-with-timezone-from-an-email
https://www.youtube.com/watch?v=YPiHBtddefI
https://developers.google.com/gmail/api/v1/reference/users/messages/send
https://pymotw.com/3/imaplib/
https://www.youtube.com/watch?v=bbPwv0TP2UQ&t=490s
https://www.afternerd.com/blog/python-string-contains/
https://www.youtube.com/watch?v=bbPwv0TP2UQ&t=490s
https://www.youtube.com/channel/UCBwpMr85NLRe4RmfE6jTRnw
https://stackoverflow.com/questions/41538112/how-to-print-the-subject-of-a-single-email-using-uid
https://stackoverflow.com/questions/12944727/python-imaplib-view-message-to-specific-sender 
https://stackoverflow.com/questions/181530/styling-multi-line-conditions-in-if-statements
https://stackoverflow.com/questions/35423564/how-can-i-store-a-result-of-a-function-in-a-variable-in-python 
https://stackoverflow.com/questions/6871016/adding-5-days-to-a-date-in-python
https://stackoverflow.com/questions/1790795/parsing-date-with-timezone-from-an-email
https://www.youtube.com/watch?v=1RnU4wCiZuI
https://www.youtube.com/watch?v=gu_J5FVO-8k
https://stackoverflow.com/questions/19511440/add-b-prefix-to-python-variable 