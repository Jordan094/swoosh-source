from django import forms  # Importing forms module
from .models import Order  # Importing Order model

class OrderForm(forms.ModelForm):
    # Meta class defining the form's model and fields
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    # Constructor to customize form fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call the parent class constructor
        placeholders = {  # Define placeholders for form fields
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State of Locality',
        }

        # Set autofocus attribute for the full_name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Customize each form field
        for field in self.fields:
            if field != 'country':  # Exclude the country field from customization
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'  # Add asterisk for required fields
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder  # Set placeholder attribute
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'  # Add CSS class
            self.fields[field].label = False  # Remove field labels

