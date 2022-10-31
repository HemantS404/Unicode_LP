from django import forms

priority_chocies =(
        ('Urgent', (
            ('Urgent & Important', 'Urgent & Important'),
            ('Urgent & Not Important', 'Urgent & Not Important')
            )),
        ('Not Urgent', (
            ('Not Urgent & Important', 'Not Urgent & Important'),
            ('Not Urgent & Not Important', 'Not Urgent & Not Important')
            ))
)
   
class priorityForm(forms.Form):
    priority = forms.ChoiceField(choices = priority_chocies)