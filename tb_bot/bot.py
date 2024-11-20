import requests
import re

class Bot_API:
    def escape_unintended_html_tags(self, text):
    # Розбираємо текст, використовуючи HTML теги та замінюємо тільки випадки не в тегах
        def replace_invalid(match):
            tag, lt, gt = match.groups()
            if tag:  # Якщо це тег, то повертаємо як є
                return tag
            elif lt:  # Якщо це < не у тегу, замінюємо
                return '&lt;'
            elif gt:  # Якщо це > не у тегу, замінюємо
                return '&gt;'
            
        # Паттерн знаходить теги, а також окремі < і >
        pattern = re.compile(r'(</?b>)|(<)|(>)')
        return re.sub(pattern, replace_invalid, text)

    def send_message_all_user(self, message):
        chat_ids = []

        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        # url = url + f'/sendMessage?chat_id={chat_id}&text={message}'
        if type(self.chat_id) == str:
            data = {'chat_id': self.chat_id, 'text': self.escape_unintended_html_tags(message), 'parse_mode': 'HTML'}
            chat_ids.append(data)
        
        elif type(self.chat_id) == dict:
            chat_ids = [chat_ids.append({'chat_id': chait_id, 'text': self.escape_unintended_html_tags(message), 'parse_mode': 'HTML'}) for chait_id in self.chat_id]
        
        for data in chat_ids:
            response = requests.post(url=url, data=data, timeout=5)

            if response.status_code == 200:
                print(f"Повідомлення було відправиленно успішно код {response.status_code}")
                print(f"Отримано через папит:\n{response.text}")
            
            else:
                print(f"Повідомлення отримало код {response.status_code}")
                print(response.text)
        

    def __init__(self, token: str, chat_id: str | dict):
        
        self.token = token
        self.chat_id = chat_id