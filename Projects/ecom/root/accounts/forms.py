from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


# from django.conf import settings
# User=settings.AUTH_USER_MODEL

User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name', 'mobile')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin', 'full_name', 'mobile')
    
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class RegisterForms(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'mobile') 

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForms, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        #user.active = False # send confirmation email
        if commit:
            user.save()
        return user

        
class login_form(forms.Form):
    fullname=forms.CharField(
        label='EMAIL ID',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name'
            }
        )
    )
    password=forms.CharField(
        # label='PASSWORD',
        widget=forms.PasswordInput(
            attrs={
                'label':'',
                'class':'form-control',
                'placeholder':'Enter Password'
            }
        )
    )
    


class homepage(forms.Form):
    pass
class about_page(forms.Form):
    pass

class contactpage(forms.Form):
    cno=forms.IntegerField(
        label='Contact Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Contact Number'
            }
        )
    )



class register(forms.Form):
    username=forms.CharField(
        label='Enter Username',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Username'
            }
        )
    )
    email=forms.EmailField(
        label='EAMIL',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Email Address'
            }
        )
    )
    password=forms.Field(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Password'
            }
        )
    )
    cpassword=forms.Field(
        label='Enter Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Confirm Password'
            }
        )
    )


    def clean_email(self):
        email=self.cleaned_data.get('email')
        qs=User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already exist')
        return email
    
    def clean_username(self):
        un=self.cleaned_data.get('username')
        qs=User.objects.filter(username=un)
        if qs.exists():
            raise forms.ValidationError('Username already exist')
        return un
    
    def clean(self):
        data=self.cleaned_data
        p1=self.cleaned_data.get('password')
        cp1=self.cleaned_data.get('cpassword')
        if p1!=cp1:
            raise forms.ValidationError('Password and Confirmed password not match')
        return data


    

   