from django.core.mail import send_mail


def send_msg(user):
    subject = "Письмо с токеном"
    email = user.email
    body = f""" Привет, {user.username}!
    Это письмо с кодом подтверждения для дальнейшего получения JWT токена.
    Ниже твои данные:
    Username: {user.username}
    Адрес почты: {user.email}
    Код подтверждения: {user.confirmation_code}
    """
    send_mail(
        subject, body, email, ["vanish@gmail.com"],
    )
