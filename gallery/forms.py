from django import forms


class GalleryForm(forms.Form):
    keywords = forms.CharField(label='keywords', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'special', 'autocomplete': 'off'}))
    size = forms.CharField(label='size', max_length=50)
    limit = forms.IntegerField(label='limit')
    specific_site = forms.CharField(label='size', max_length=100, required=False)


