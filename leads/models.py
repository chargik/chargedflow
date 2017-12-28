from django.conf import settings
from django.core.mail import send_mail
from django.db import models

from pages.models import Tours

# Create your models here.
class Join(models.Model):
    lead_name = models.CharField(max_length=128)
    telephone = models.CharField(max_length=15)
    # url_field = HttpRequest.get_full_path(self)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.lead_name

    # def save(self):
    #     print(self.lead_name, self.telephone)
    #     subject = 'Заявка с сайта'
    #     message = '''Заявка со страницы  \n\n
    #     Имя: {0}\n\n
    #     Телефон:{1}\n\n'''.format(self.lead_name, self.telephone)
    #     from_email = settings.EMAIL_HOST_USER
    #     to_email = ['unklerufus@gmail.com']
    #     send_mail(subject, message, from_email, to_email, fail_silently=False)
    #     super(Join, self).save()
