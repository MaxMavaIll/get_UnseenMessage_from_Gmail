import imaplib
import email




class Gmail_API:

    def connect(self):
        self.mail = imaplib.IMAP4_SSL(self.imap_url)
        self.mail.login(self.username, self.password)

    def disconnect(self):
        self.mail.logout()

    def form_message(self):
        update_messages = {}

        for index, message_data in enumerate(self.message_with_supra.values()):
            message = f'#### {index + 1} ####\n'
            message += f'<b>From</b>: {message_data['from']}\n'
            message += f'<b>Title</b>: {message_data['title']}\n\n'
            message += f'<b>Text</b>: {message_data['text'][:500]}...\n\n'

            update_messages[index] = message

        return update_messages
        
        

    def get_text_from_email(self):
        email_subject = None
        email_from = None
        email_body = None

        self.mail.list()
        self.mail.select('"[Gmail]/All Mail"')
        status, response = self.mail.search(None, 'UNSEEN')
        unseen_emails = response[0].split()
        print(f'Кількість непрочитаних листів: {len(unseen_emails)}')

        for index, email_id in enumerate(unseen_emails):
            status, email_data = self.mail.fetch(email_id, '(RFC822)')
            
            for response_part in email_data:
                if isinstance(response_part, tuple):
                    # Отримання повідомлення
                    message = email.message_from_bytes(response_part[1])
                    email_subject = message['subject']
                    email_from = message['from']
                    
                    # Перевірка, чи має лист текстовий вміст
                    if message.is_multipart():
                        for part in message.walk():
                            if part.get_content_type() == 'text/plain':
                                email_body = part.get_payload(decode=True).decode('utf-8')
                                break
                    else:
                        email_body = message.get_payload(decode=True).decode('utf-8')

                    print(f'Від: {email_from}, Тема: {email_subject}')
                    print(f'Текст листа: {email_body}') 
                    
        
            self.message_with_supra[index] = {'from': email_from, 'title': email_subject, 'text': email_body}


    def __init__(
            self, 
            username: str = None, 
            password: str = None,
            imap_url: str = 'imap.gmail.com'
        ):
        self.username = username
        self.password = password
        self.imap_url = imap_url
        self.mail = None
        self.message_with_supra = dict()


# Вибір поштової скриньки (наприклад, вхідні)

