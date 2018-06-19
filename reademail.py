############################# readmail.py ##################################
import imaplib
import pprint
import email

msrvr=imaplib.IMAP4_SSL \
       ('imap.gmail.com',993)

unm = 'finalsoftwareproject@gmail.com'
pwd = 'soft112233'
msrvr.login(unm,pwd)

stat,cnt = msrvr.select('Inbox')

stat,dta = msrvr.fetch \
           (cnt[0],'(RFC822)')

#print( dta[0][1])

raw_email = dta[0][1]
#continue inside the same for loop as above
raw_email_string = raw_email.decode('utf-8')
# converts byte literal to string removing b''
email_message = email.message_from_string(raw_email_string)
# this will loop through all the available multiparts in mail
for part in email_message.walk():
 if part.get_content_type() == "text/plain": # ignore attachments/html
  body = part.get_payload(decode=True)
 else:
  continue

def nothing():
         print(email_message['Date'])

         print 'From   :  '
         print(email_message['From'])
         print ''
         print 'Subject:  '
         print (email_message['Subject'])
         print ''
         print 'Body   :  '
         print (body.decode('utf-8'))


Date=email_message['Date']
From=email_message['From']
Subject= email_message['Subject']
Body=body.decode('utf-8')




msrvr.close()
msrvr.logout()
