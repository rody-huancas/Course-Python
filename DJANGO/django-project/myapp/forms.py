from django import forms

# Formulario para enviar a la vista
class CreateNewTask(forms.Form):
    title = forms.CharField(label='Titulo de la tarea: ', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label='Descripción de la tarea: ', widget=forms.Textarea(attrs={'class': 'input'}))


class createNewProject(forms.Form):
    name = forms.CharField(label='Nombre del proyecto: ', max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))