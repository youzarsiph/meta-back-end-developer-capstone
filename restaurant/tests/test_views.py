""" Test for the views """


from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


# Create your tests here.
class MenuViewTest(TestCase):
    """ MenuView Test """

    def setUp(self):
        """ Create a few MenuItem instances """

        items = [
            {'title': 'IceCream', 'price': 80, 'inventory': 100},
            {'title': 'Pizza', 'price': 200, 'inventory': 10},
            {'title': 'Pata', 'price': 100, 'inventory': 50},
        ]

        for i in items:
            item = MenuItem.objects.create(**i)
            item.save()

    def test_get_all(self):
        """ Test get all method """

        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(data=items)
        self.assertEqual(serializer.data, [
            {'title': 'IceCream', 'price': 80, 'inventory': 100},
            {'title': 'Pizza', 'price': 200, 'inventory': 10},
            {'title': 'Pata', 'price': 100, 'inventory': 50},
        ])
