from django import forms

STYLES = [("", "Любой"), ("classic", "Классический"), ("sport", "Спортивный"), ("casual", "Повседневный")]
SIZES = [("", "Любой"), ("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")]


class PreferencesForm(forms.Form):
    style = forms.ChoiceField(label="Любимый стиль", choices=STYLES, required=False)
    size = forms.ChoiceField(label="Размер", choices=SIZES, required=False)
