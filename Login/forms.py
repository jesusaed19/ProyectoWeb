from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

class FormUserLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormUserLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

class FormUserRegister(UserCreationForm, forms.Form):
    email = forms.EmailField(required=False)
    
    def __init__(self, *args, **kwargs):
        super(FormUserRegister, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Verifique su contraseña'
        # self.fields['password2'].widget.attrs['placeholder'] = 'Verifique su contraseña'
        
    
    
      
    
        
        
        