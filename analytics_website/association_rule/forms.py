from django import forms

class AssociationRuleForm(forms.Form):
	Department = forms.IntegerField(widget=forms.NumberInput( attrs={'class':'form-control'}), min_value = 1, max_value=50)
	Class = forms.DecimalField(widget=forms.NumberInput( attrs={'class':'form-control'}),min_value = 1, max_value=98)
	#SubClass = forms.DecimalField(widget=forms.NumberInput( attrs={'class':'form-control'}),min_value = 1, max_value=98)
	Start_Date = forms.DateTimeField(widget=forms.DateTimeInput( attrs={'class':'form-control'}))
	End_Date = forms.DateTimeField(widget=forms.DateTimeInput( attrs={'class':'form-control'}))