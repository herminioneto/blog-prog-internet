from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


allowed_emails = [
    "Antonio.mei.nt@gmail.com",
    "patrocinioluisf@gmail.com",
    "hyutfg755@gmail.com",
]


@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if not created and instance.is_active:
        if instance.email in allowed_emails:
            instance.is_active = True
            instance.save()
