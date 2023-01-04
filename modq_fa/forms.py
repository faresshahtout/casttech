from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.forms.widgets import PasswordInput, TextInput


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'E-mail', 'class': 'form-control-input','id':'usernmae'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control-input','id':'password'}))
    password1 = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password', 'class': 'form-control-input'}))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Confirm Your Password',  'type': 'password', 'class': 'form-control-input'}))
    hospital=forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder':'Hospital Name', 'class': 'form-control-input'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "hospital")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class castrequestform(forms.Form):
    wristwidht =forms.DecimalField(max_digits=3,decimal_places=2)
    wristhight =forms.DecimalField(max_digits=3,decimal_places=2)
    clearance =forms.DecimalField(max_digits=3,decimal_places=2)
    ABsection =forms.DecimalField(max_digits=3,decimal_places=2)
    Bwidth=forms.DecimalField(max_digits=3,decimal_places=2)
    Bhight =forms.DecimalField(max_digits=3,decimal_places=2)
    castthikness =forms.DecimalField(max_digits=3,decimal_places=2)
    BCsection =forms.DecimalField(max_digits=3,decimal_places=2)
    Chight =forms.DecimalField(max_digits=3,decimal_places=2)
    Cwidth =forms.DecimalField(max_digits=3,decimal_places=2)
    circulediameter =forms.DecimalField(max_digits=3,decimal_places=2)
    hangangle =forms.DecimalField(max_digits=3,decimal_places=2)
    leftpump =forms.DecimalField(max_digits=3,decimal_places=2)
    handtip =forms.DecimalField(max_digits=3,decimal_places=2)
    rightpump =forms.DecimalField(max_digits=3,decimal_places=2)
    midhandthikness =forms.DecimalField(max_digits=3,decimal_places=2)
    palmlength =forms.DecimalField(max_digits=3,decimal_places=2)
    palmwidth =forms.DecimalField(max_digits=3,decimal_places=2)
    thumby =forms.DecimalField(max_digits=3,decimal_places=2)

# from .models import casts
# obj = questions.objects.get(user=request.user)

# wristhight='wristhight'
# clearance='clearance'
# ABsection='ABsection'
# Bwidth='Bwidth'
# Bhight='Bhight'
# castthikness='castthikness'
# BCsection='BCsection'
# Chight='Chight'
# Cwidth='Cwidth'
# circulediameter='circulediameter'
# hangangle='hangangle'
# leftpump='leftpump'
# handtip='handtip'
# rightpump='rightpump'
# midhandthikness='midhandthikness'
# palmlength='palmlength'
# palmwidth='palmwidth'
# thumby='thumby'