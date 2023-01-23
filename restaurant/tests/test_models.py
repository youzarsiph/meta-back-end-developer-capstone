""" Test for the models """


from django.test import TestCase
from restaurant.models import MenuItem


# Create your tests here.
class MenuTest(TestCase):
    """ MenuItem Test """

    def test_menu(self):
        """ Test the menu """

        instance = MenuItem.objects.create(
            title='IceCream',
            price=80,
            inventory=100
        )

        self.assertEqual(instance, 'IceCream: $80')
