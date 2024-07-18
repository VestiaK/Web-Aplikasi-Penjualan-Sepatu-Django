from django.forms import ModelForm
from dashboard.models import Barang
from django import forms
from .models import Barang, Jenis, User

class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields='__all__'
        widgets = {
            'kodebrg': forms.TextInput(attrs={'class': 'form-control'}),
            'imagebrg': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'namabrg': forms.TextInput(attrs={'class': 'form-control'}),
            'stokbrg': forms.NumberInput(attrs={'class': 'form-control'}),
            'hargabrg': forms.NumberInput(attrs={'class': 'form-control'}),
            'jenis_id': forms.Select(attrs={'class': 'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields='__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'jenisUser': forms.Select(attrs={'class': 'form-control'}),
        }

        