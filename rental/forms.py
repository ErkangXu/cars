from django import forms

class StatForm(forms.Form):
	month=forms.CharField(label="月份", max_length=6)

class CustomerForm(forms.Form):
	id_string=forms.CharField(label="身份证号", max_length=30)

class SearchCarForm(forms.Form):
	start=forms.CharField(label="起始日期", max_length=8)
	end=forms.CharField(label="终止日期", max_length=8)