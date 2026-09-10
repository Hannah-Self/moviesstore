from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
class CustomErrorList(ErrorList):
    def __str__(self):
        if not self: 
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert"> {e}</div>' for e in self]))
    #import errorList class, store errors
    #import mark_safe, ensures no harmful content
    #customs error look and feel
    #override str method, customs HTML code
class CustomUserCreationForm(UserCreationForm): 
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

#import UserCreationForm
#when custom --> calls on parent, iterates by user, pass1, pass2, removes help text
#field specified, add CSS form-control to import look/feel