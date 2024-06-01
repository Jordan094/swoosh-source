from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, UserProfile


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    # Custom widget for the image field
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        # Call the parent class's __init__ method to initialize the form
        super().__init__(*args, **kwargs)
        
        # Fetch all categories from the database
        categories = Category.objects.all()
        # Create a list of tuples (id, friendly_name) for each category
        category_names = [(c.id, c.friendly_name) for c in categories]

        # Set the choices for the category field
        self.fields['category'].choices = category_names
        # Add a custom CSS class to each field
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
