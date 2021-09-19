from django import forms 

from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit

from . import models


class PersonDetailForm(forms.Form):
    """ Simple Test Form to test both is_bound and 
        is_valid() attr of forms 
    """
    name = forms.CharField(max_length = 255)
    age = forms.IntegerField(min_value = 1)

    def __init__(self, *args, **kwargs):
        # get extra keyword args passed from the view class 
        vip = kwargs.pop('vip', False)
        super().__init__(*args, **kwargs)

        #Are you a Vip user 
        if vip:
            self.fields["first_class"]= forms.BooleanField(
                    label="Fly First Class?",
                    required = False,
                    initial = True,
                    help_text = "First-Class only offered to VIPS"
            )

        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('submit', 'Submit'))


class NewsletterForm(forms.Form):
    email = forms.EmailField()
    def __init__(self, *args, **kwargs):
        submit_btn_name = kwargs.pop('submit_btn_name','subscribe_btn')
        submit_btn_value = kwargs.pop('submit_btn_value','Subscribe')
    
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit(name = submit_btn_name,
                                         value = submit_btn_value))
                                              

class SubscribeForm(NewsletterForm):
    def __init__(self, *args, **kwargs):
        kwargs['submit_btn_name'] = 'subscribe_btn'
        kwargs['submit_btn_value'] = 'Subcsribe'
        super().__init__(*args, **kwargs)
    
    
class UnSubscribeForm(NewsletterForm):
    def __init__(self, *args, **kwargs):
        kwargs['submit_btn_name'] = 'unsubscribe_btn'
        kwargs['submit_btn_value'] = 'UnSubcsribe'
        super().__init__(*args, **kwargs)
    


class ImportantDateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save','SaveDate'))
    
    class Meta:
        model = models.ImportantDate
        fields = ['date', 'description' ]
    
    

