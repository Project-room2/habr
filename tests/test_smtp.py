from django.test import TestCase
from django.core import mail


class ViewsTestCase(TestCase):
    def test_send(self):
        mail.send_mail('Test SMTP', 'SMTP server 4t-habr.ru.', 'i@4t-habr.ru', ['i@dr2moscow.ru'])
        assert len(mail.outbox) == 1

    def test_send_again(self):
        mail.send_mail('Test SMTP', 'SMTP server 4t-habr.ru.', 'i@4t-habr.ru', ['i@dr2moscow.ru'])
        assert len(mail.outbox) == 1
