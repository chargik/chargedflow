from django.db import models
from pages.models import Tours

# Create your models here.
class Join(models.Model):
    lead_name = models.CharField(max_length=128)
    telephone = models.CharField(max_length=15)
    # url_field = 
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.lead_name

        # def save(self):
        # for item in Subscrib.objects.all():
        #     to_email = item.email
        #     subject = 'Обновление новостей на сайте'
        #     html_content = '<a href="http://developtolive.com/news/%s/">%s</a>' % (self.id, self.title)
        #     from_email = 'i@developtolive.com'
        #     msg = EmailMessage(subject, html_content, from_email, [to_email])
        #     msg.content_subtype = "html"
        #     msg.send()
        # super(News, self).save()