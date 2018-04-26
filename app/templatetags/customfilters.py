from django import template
import datetime

register = template.Library()

@register.filter
def days(value):
    today = datetime.date.today()
    diff  = today - value
    return '%s days' % diff.days
        
