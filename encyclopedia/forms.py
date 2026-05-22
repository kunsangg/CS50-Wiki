from django import forms


class NewPageForm(forms.Form):
    title = forms.CharField(label="Title")

    content = forms.CharField(
        label="Content",
        widget=forms.Textarea(attrs={
            "rows": 20
        })
    )