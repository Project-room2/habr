from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings


def send_verify_mail(user):
    verify_link = reverse('userapp:verify', kwargs={
        'email': user.email,
        'activation_key':    user.activation_key,
    })

    title = f'Подтверждение регистрации {user.email}'

    message = f'Для подтверждения учетной записи {user.username} на портале \
    {settings.DOMAIN_NAME} перейдите по ссылке: \n{settings.DOMAIN_NAME}{verify_link}'

    result = send_mail(title, message, settings.EMAIL_HOST_USER, [user.email, ], fail_silently=False)

    return result
