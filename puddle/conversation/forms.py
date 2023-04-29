from django import forms

from .models import COnversationMessage

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = COnversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }