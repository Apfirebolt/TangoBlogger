from django import template
from random import randint

register = template.Library()

effect_list = ['fade-up', 'fade-down', 'fade-right', 'fade-left', 'fade-up-right', 'flip-left',
                   'flip-right', 'flip-up', 'flip-down', 'zoom-in-up', 'zoom-in-down']


def filter_effect(list_val):
    random_index = randint(0, 10)
    return list_val[random_index]

register.filter('custom_effect', filter_effect)