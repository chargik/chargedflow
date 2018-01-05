from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from .signals import object_viewed_signal
from pages.models import Tours


User = settings.AUTH_USER_MODEL

class ObjectViewed(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    ip_adress = models.CharField(max_length=220, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Tours, on_delete=models.CASCADE)


    def __str__(self):
        return "%s viewed %s" %(self.content_object, self.timestamp)

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "Object viewed"
        verbose_name_plural = "Objects viewed"


def object_viewed_receiver(sender, instance, request, *args, **kwargs):
    print(sender)
    print(instance)
    print(request)
    print(request.user)

object_viewed_signal.connect(object_viewed_receiver)