from django import forms

priority_chocies =(
        ('Urgent', (
            ( 1,'Urgent & Important'),
            (2, 'Urgent & Not Important')
            )),
        ('Not Urgent', (
            (3, 'Not Urgent & Important'),
            (4,'Not Urgent & Not Important' )
            ))
)
   
class priorityForm(forms.Form):
    priority = forms.ChoiceField(choices = priority_chocies)