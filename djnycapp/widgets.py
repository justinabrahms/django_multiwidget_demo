# widgets
from django.forms import widgets
from django.conf import settings
from django.template.defaulttags import mark_safe
from django.contrib.auth.models import User

class AutoCompleteWidget(widgets.MultiWidget):

    CLIENT_CODE = """
    <script type="text/javascript">
    $('document').ready(function () {
        $('#id_%s_1').autocomplete('/admin/autocomplete/', {
         'hidden_input': $('#id_%s_0')
        });
    });
    </script>
    """

    def __init__(self, attrs=None):
        widget_list = (widgets.HiddenInput(attrs=attrs), widgets.TextInput(attrs=attrs))
        super(AutoCompleteWidget, self).__init__(widget_list, attrs)

    def decompress(self, value):
        """
        Accepts a single value which it then extracts enough values to
        populate the various widgets.
        
        We'll provide the id for the hidden input and a user
        representable string for the shown input field.
        """
        if value:
            obj = User.objects.get(id=value)
            return [obj.id, str(obj)]
        return [None, None]

    def render(self, name, value, attrs=None):
        """
        Converts the widget to an html representation of itself.
        """
        output = super(AutoCompleteWidget, self).render(name, value, attrs)
        return output + mark_safe(self.CLIENT_CODE % (name, name))

    class Media:
        css = {
            'all': (settings.STATIC_URL + 'admin/css/jquery.autocomplete.css',)
        }

        js = (settings.STATIC_URL + 'admin/js/jquery-1.3.2.js',
              settings.STATIC_URL + 'admin/js/jquery.autocomplete.js')
