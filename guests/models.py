from django.db import models
from django.utils.translation import gettext_lazy as _
from shortuuid.django_fields import ShortUUIDField
from django.contrib import admin


class GuestGroup(models.Model):
    class GuestGroupStatusOptions(models.TextChoices):
        RESPONDED = "RE", _("Responded")
        NO_RESPONSE = "NR", _("No Response")

    name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=2,
        choices=GuestGroupStatusOptions,
        default=GuestGroupStatusOptions.NO_RESPONSE
    )
    email = models.EmailField(unique=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


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
    dietary_restrictions = models.TextField(blank=True, null=True)
    group = models.ForeignKey(
        GuestGroup,
        related_name="guests",
        on_delete=models.CASCADE
    )

    @admin.display(
        boolean=True,
        description="Has a Dietary Restriction?",
    )
    def has_dietary_restriction(self):
        return (
            self.dietary_restrictions is not None
            and len(self.dietary_restrictions) > 0
        )

    def __str__(self):
        return self.name


class GuestGroupEmailInvitation(models.Model):
    slug = ShortUUIDField(
        length=10,
        max_length=10,
        alphabet='abcdefghjkmnprstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789',
        primary_key=False,
        unique=True
    )
    group = models.ForeignKey(
        GuestGroup,
        related_name='invitations',
        on_delete=models.DO_NOTHING
    )
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def __str__(self):
        return self.group.name + " - " + self.slug
