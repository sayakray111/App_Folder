from django import forms
from .models import Building_Details
MAX_BUILDING_HEIGHT = 20
class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building_Details
        fields=['Area','Height','Description']

    def cleaned_Height(self):
        Height = self.cleaned_data.get("Height")
        if(Height>MAX_BUILDING_HEIGHT):
            raise forms.ValidationError('This building is too high')
        else:
            return Height
            