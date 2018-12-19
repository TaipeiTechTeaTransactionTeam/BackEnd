from django.template import Library

register = Library()

@register.filter
def number_of_ranks(number):
    return range(1, number+1)
