from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit,Field
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True, label="Correo Electronico")
    class Meta:
        model=User
        fields=["username","email"]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper=FormHelper()
        self.form_method="post"
        self.form_class="needs-validation"
            
        self.helper.layout=Layout(
            Row(
                Column(Field("username", css_class="col-md-6 mb-3",placeholder="John Doe") ),
                Column("email", css_class="col-md-6 mb-3", placeholder="Kroosismo0202@gmail.com")

                ),
            Row(
                Column("password1", css_class="col-md-6 mb-3",placeholder="Tu contraseña"),
                Column("password2", css_class="col-md-6 mb-3")

                ),
            Submit("submit","Registrame", css_class="btn btn-primary")

            )
    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
            return user
            


class LoginForm(AuthenticationForm):
    def __init__(self,request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.helper=FormHelper()
        self.helper.form_method="post"
        self.helper.form_class="needs-validation"

        self.helper.layout=Layout(
            Row(
                Column(Field("username", css_class="mb-3", placeholder="Tu Nombre de Usuario")),
                Column(Field("password", css_class="mb-3", placeholder="Contraseña"))
                
                ),
                Submit("submit", "Iniciar sesión", css_class="btn btn-primary")
            
        )