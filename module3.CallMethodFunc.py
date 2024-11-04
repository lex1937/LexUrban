def send_email(Message_: str, recipient_: str, *, sender_="university.helpg@mail.com"):
    """ Функция отправляет письмо получателю, с проверкой
        корректность  почтового адреса (@,'.com', '.ru', '.net'),
        проверкой на отправку самому себе,
        проверкой на отправителя по умолчанию
    """

    if correct_email(recipient_, sender_) is True:
        if recipient_ == sender_:
            print("Нельзя отправить письмо самому себе!")
        elif sender_ == "university.helpg@mail.com":
            print(f"Письмо успешно отправлено с адреса {sender_} на адрес {recipient_}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! "
                  f"Письмо отправлено с адреса {sender_} на адрес {recipient_}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender_} на адрес {recipient_}")


def correct_email(r, s):
    """ Функция корректности доменного имени и наличие символа '@' """

    t = f = False
    if r.count('@') and s.count("@"):
        r_ = r[r.rfind("."):]
        s_ = s[s.rfind("."):]
        match r_:
            case (".com" | ".ru" | ".net" | ".co"):
                t = True
        match s_:
            case (".com" | ".ru" | ".net" | ".co"):
                f = True
    if t and f is True:
        return True
    return False


send_email('Это сообщение для проверки связи', 'Yra1234@yandex.ru')
send_email('Вы видите это сообщение как лучший студент курса!',
           'Aleksandr98@mail.net', sender_='Yra1234@yandex.ru')
send_email('Пожалуйста, исправьте задание',
           'Yra1234@yandex.cr', sender_='urban.student@mail.ru')
send_email('Напоминаю самому себе о вебинаре',
           'Yra1234@yandex.ru', sender_='Yra1234@yandex.ru')
