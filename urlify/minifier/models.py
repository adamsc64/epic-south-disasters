from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class MinifiedURL(models.Model):
    submitter = models.ForeignKey('auth.user', null=True)
    url = models.CharField(max_length=1000, db_index=True)
    domain = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


@receiver(post_save)
def email_user_on_url_change(sender, **kwargs):
    if sender == MinifiedURL:
        user = kwargs['instance'].submitter
        if user:
            email(user,
                "Congratulations on changing "
                "the URL, %s!" % user.username
                )

def email(user, body):
    """Fakes sending an email for demo purposes."""
    print "%s: %s" % (user, body)
