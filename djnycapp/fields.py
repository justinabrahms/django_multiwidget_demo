# fields
from django.forms import fields
from djnycapp.widgets import AutoCompleteWidget
from django.contrib.auth.models import User

class UserAutoCompleteField(fields.MultiValueField):
    widget = AutoCompleteWidget

    def __init__(self, *args, **kwargs):
        """
        Have to pass a list of field types to the constructor, else we
        won't get any data to our compress method.
        """
        all_fields = (
            fields.CharField(),
            fields.CharField(),
            )
        super(UserAutoCompleteField, self).__init__(all_fields, *args, **kwargs)
    
    def compress(self, data_list):
        """
        Takes the values from the MultiWidget and passes them as a
        list to this function. This function needs to compress the
        list into a single object to save.
        """
        if data_list:
            return User.objects.get(id=data_list[0])
        return None
