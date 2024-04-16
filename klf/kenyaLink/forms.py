from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Invisible

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=256, label='First Name')
    last_name = forms.CharField(max_length=256, label='Last Name')
    email = forms.EmailField(max_length=256, label='Email')
    subject = forms.CharField(max_length=256, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    agree_to_terms = forms.BooleanField(label='I accept the Terms & Conditions')
    captcha = ReCaptchaField(widget=ReCaptchaV2Invisible)
