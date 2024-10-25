# forecast_app/forms.py
from django import forms

class ForecastForm(forms.Form):
    forecast_horizon = forms.IntegerField(label='Forecast Horizon (days)', min_value=1)
    dataset_choice = forms.ChoiceField(
        choices=[
            ('sales', 'Daily sales data for a retail store'),
            ('temperature', 'Monthly average temperatures'),
            ('stock', 'Historical stock prices for a specific company')
        ],
        widget=forms.RadioSelect,
        label='Select Dataset'
    )