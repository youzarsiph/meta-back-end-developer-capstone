""" App configuration """


from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    """ Restaurant app  configuration """

    name = 'restaurant'
    default_auto_field = 'django.db.models.BigAutoField'
