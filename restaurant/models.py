""" Data models for the app """


from django.db import models


# Create your models here.
class Booking(models.Model):
    """ Booking Model """

    # Attributes
    name = models.CharField(
        max_length=256,
        db_index=True,
        help_text='Name of the booking'
    )
    guest_number = models.SmallIntegerField(
        default=1,
        help_text='Number of the guests'
    )
    date = models.DateTimeField(
        help_text='Booking date'
    )

    def __str__(self):
        """ Convert the object to string """

        return f'Booking for {self.name} at {self.date}'

    class Meta:
        """ Meta data """

        ordering = ['id']


class MenuItem(models.Model):
    """ MenuItem Model """

    # Attributes
    title = models.CharField(
        max_length=256,
        db_index=True,
        help_text='Title of the menu'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Price of the menu'
    )
    inventory = models.SmallIntegerField(
        default=10,
        help_text='Number of items in the inventory'
    )

    def __str__(self):
        """ Convert the object to string """

        return f'{self.title}: ${self.price}'

    class Meta:
        """ Meta data """

        ordering = ['id']
