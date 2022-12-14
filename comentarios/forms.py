from django.forms import ModelForm
from .models import Comentario
import requests


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6Lc9Lp0hAAAAAKBwh1hHfHc6MKqkKBQQBeEk30f2',
                'response': recaptcha_response
            }
        )

        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success'):
            self.add_error(
                'comentario',
                'Desculpe, ocorreu um erro.'
            )

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario',)
