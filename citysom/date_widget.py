import datetime

from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.encoding import smart_unicode

MONTHS = (
    ('', ''),
    (1, 'Jan'),
    (2, 'Feb'),
    (3, 'Mar'),
    (4, 'Apr'),
    (5, 'May'),
    (6, 'Jun'),
    (7, 'July'),
    (8, 'Aug'),
    (9, 'Sep'),
    (10, 'Oct'),
    (11, 'Nov'),
    (12, 'Dec')
)

DAYS = [('','')] + [(x,x) for x in range (1, 32)]

this_year = datetime.datetime.now().year
YEARS = [('', '')] + [(x,x) for x in range(this_year-100, this_year-16)]

class CustomDateField(forms.MultiValueField):
    
    def __init__(self, required=True, label=None, initial=None):
        fields = (
                  forms.IntegerField(widget=forms.Select(choices=MONTHS)),
                  forms.IntegerField(widget=forms.Select(choices=DAYS)),
                  forms.IntegerField(widget=forms.Select(choices=YEARS))
                  )
        widget = DateMultiWidget()
        super(CustomDateField, self).__init__(fields, required, widget, label, initial)
    
    def compress(self, data_list):
        if data_list:
            try:
                d = datetime.datetime(data_list[2], data_list[0], data_list[1])
            except:
                raise forms.ValidationError, "Make sure you have filled out all fields."
            return d
        return None

class DateMultiWidget(forms.MultiWidget):
    
    def __init__(self, attrs=None):
        widgets = (
            forms.Select(choices=MONTHS),
            forms.Select(choices=DAYS),
            forms.Select(choices=YEARS)
        )
        super(DateMultiWidget, self).__init__(widgets, attrs)
        
    def decompress(self, value):
        if value:
            return value.month, value.day, value.year
        return [None, None, None]

    def render(self, name, value, attrs=None):
        # value is a list of values, each corresponding to a widget
        # in self.widgets.
        if not isinstance(value, list):
            value = self.decompress(value)
        
        output = []
        final_attrs = self.build_attrs(attrs)
        id_ = final_attrs.get('id', None)
        for i, widget in enumerate(self.widgets):
            try:
                widget_value = value[i]
            except IndexError:
                widget_value = None
            if id_:
                final_attrs = dict(final_attrs, id='%s_%s' % (id_, i))
            output.append(widget.render(name + '_%s' % i, widget_value, final_attrs))
        
        d = {
            'month':output[0],
            'day':output[1],
            'year':output[2]
        }
         
        return mark_safe(render_to_string('myprofile/date_widget.html', d))
