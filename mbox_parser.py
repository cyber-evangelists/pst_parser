import mailbox
import email.utils
import os
from db_manager import create_db, store_data
create_db()

def parse_mbox_file(mbox_file):
    data = []
    mbox = mailbox.mbox(mbox_file)
    for message in mbox:
        # Extract email details
        subject = message['subject']
        sender_info = message['from']
        date = message['date']
        receiver_info = message['to']
        sender_name, sender_email = email.utils.parseaddr(sender_info)
        receiver_name, receiver_email = email.utils.parseaddr(receiver_info)
        
        for part in message.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
                
            attachment_name = part.get_filename()
            content_type = part.get_content_type()
            attachment_data = part.get_payload(decode=True)

            if attachment_data:
                save_dir = 'attachments'
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                attachment_path = os.path.join(save_dir, attachment_name)

                with open(attachment_path, 'wb') as file:
                    file.write(attachment_data)
            email_data = {
                'subject': subject,
                'sender_name': sender_name,
                'sender_email': sender_email,
                'receiver_name': receiver_name,
                'receiver_email': receiver_email,
                'attachment_name': attachment_name,
                'content_type': content_type,
                'datetime': date,
            }
            data.append(email_data)
            store_data(email_data)
    return data
            
           
# print(parse_mbox_file('D:\Languages\Python\Email Attachments\cindyloh3333_gmail.com.mbox')) 

        
        
