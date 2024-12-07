from django.urls import reverse_lazy
from guests.models import Guest
from django.forms import modelformset_factory
from django import forms
from django.views.generic.edit import FormView
from django.utils import timezone
from django.shortcuts import get_object_or_404

from guests import models


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'status', 'dietary_restrictions']
        widgets = {
            'name': forms.HiddenInput,
            'dietary_restrictions': forms.Textarea(attrs={'rows': 3}),
        }


# Create a formset factory for multiple guests
GuestFormSet = modelformset_factory(
    Guest,
    form=GuestForm,
    extra=0,  # No extra empty forms
)


class GuestListFormView(FormView):
    template_name = 'guests/edit.html'
    form_class = GuestFormSet
    success_url = reverse_lazy('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        invitation = get_object_or_404(
            models.GuestGroupEmailInvitation,
            slug=self.kwargs.get('slug'),
            # only allow invitations that haven't expired. while there is a
            # cron job to delete these, it might not be to the second
            expires_at__gt=timezone.now()
        )

        kwargs['queryset'] = Guest.objects.filter(group=invitation.group)
        return kwargs

    def form_valid(self, form):
        form.save()
        # TODO: delete invitation after success
        return super().form_valid(form)
