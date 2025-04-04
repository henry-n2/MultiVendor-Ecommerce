from django import forms

class SolarForm(forms.Form):
    place_name = forms.CharField(label='Town, City, or Locality Name', max_length=100)
    electricity_bill = forms.FloatField(label='Highest Monthly Electricity Bill (INR)')
    available_area = forms.FloatField(label='Available Area (sq. feet)')
    near_water = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label='Is the site near a water body?')
