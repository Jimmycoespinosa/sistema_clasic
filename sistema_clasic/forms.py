from django import forms
from .models import mdlMain, setCounty
from .models import setState, loadState

class frmMain(forms.ModelForm):
    class Meta:
        model = mdlMain
        fields = '__all__'

class frmCreateCn(forms.ModelForm):
    class Meta:
        model = setCounty
        fields = '__all__'

class frmCreateSt(forms.ModelForm):
    class Meta:
        model = setState
        fields = '__all__'

class frmLoadSt(forms.ModelForm):
    class Meta:
        model = loadState
        fields = '__all__'
