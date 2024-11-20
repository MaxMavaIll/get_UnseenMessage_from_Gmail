import time
import toml

from Gmail.gmail_supra import Gmail_API
from tb_bot.bot import Bot_API

#kuih vhad bpzt zeft
config_toml = toml.load('config.toml')


def main():
    gmail_obj = Gmail_API(
        username=config_toml['gmail']['username'],
        password=config_toml['gmail']['password']
    )
    tg_bot_obj = Bot_API(
        token=config_toml['tg_bot']['token'],
        chat_id=config_toml['tg_bot']['chat_id']
    )

    gmail_obj.connect()
    gmail_obj.get_text_from_email()
    messages = gmail_obj.form_message()

    for index, message in enumerate(messages.values()):
        if index == 0:
            message = ''.join(['Supra\n\n', message])
        tg_bot_obj.send_message_all_user(message)
        time.sleep(1)


    gmail_obj.disconnect()





if __name__ == '__main__':
    main()