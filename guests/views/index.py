from django import forms
from django.views.generic.edit import FormView
from django.utils import timezone

from guests import models


class RsvpRequestForm(forms.Form):
    email = forms.EmailField(required=True)

    def send_email(self):
        try:
            group = models.GuestGroup.objects.get(
                email=self.cleaned_data['email']
            )
            active_invitations = group.invitations.filter(
                expires_at__gt=timezone.now()).latest('expires_at')
            models.GuestGroupEmailInvitation.objects.filter(
                group=group
            ).delete()
            group.invitations.create(
                expires_at=timezone.now() + timezone.timedelta(hours=2))
            group.save()
            # TODO: actually send the email!
        except models.GuestGroup.DoesNotExist:
            # just treat it as successful if no group exists
            pass


class RsvpRequestView(FormView):
    template_name = "guests/index.html"
    form_class = RsvpRequestForm
    success_url = "/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
