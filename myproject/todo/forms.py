from django import forms

class TodoForm(forms.Form):
    text = forms.CharField(max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter items to be bought e.g. banana', 'aria-label': 'Todo', 'aria-describedby': 'add-btn'}
                           ))