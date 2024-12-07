from django.db import models
from django.utils.translation import gettext_lazy as _
from shortuuid.django_fields import ShortUUIDField


class GuestGroup(models.Model):
    class GuestGroupStatusOptions(models.TextChoices):
        RESPONDED = "RE", _("Responded")
        NO_RESPONSE = "NR", _("No Response")

    status = models.CharField(
        max_length=2,
        choices=GuestGroupStatusOptions,
        default=GuestGroupStatusOptions.NO_RESPONSE
    )
    slug = ShortUUIDField(
        length=10,
        max_length=10,
        alphabet='abcdefghjkmnprstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789',
        primary_key=False,
        unique=True
    )
    email = models.EmailField(unique=True)


class Guest(models.Model):
    class GuestStatusOptions(models.TextChoices):
        GOING = "GO", _("Going")
        NOT_GOING = "NG", _("Not Going")
        NO_RESPONSE = "NR", _("No Response")

    name = models.CharField(blank=False, null=False, max_length=300)
    status = models.CharField(
        max_length=2,
        choices=GuestStatusOptions,
        default=GuestStatusOptions.NO_RESPONSE
    )
    dietary_restrictions = models.TextField()
    group = models.ForeignKey(
        GuestGroup,
        related_name="guests",
        on_delete=models.CASCADE
    )
