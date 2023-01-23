""" Model serialization """


from django.contrib.auth.models import User
from rest_framework.serializers import HyperlinkedModelSerializer
from restaurant.models import Booking, MenuItem


class UserSerializer(HyperlinkedModelSerializer):
    """ Hyperlinked User Serializer """

    class Meta:
        """ Meta data """

        model = User
        fields = [
            'id', 'url', 'username', 'first_name',
            'last_name', 'email', 'groups'
        ]


class BookingSerializer(HyperlinkedModelSerializer):
    """ Hyperlinked Booking Serializer """

    class Meta:
        """ Meta data """

        model = Booking
        fields = ['id', 'url', 'name', 'guest_number', 'date']


class MenuItemSerializer(HyperlinkedModelSerializer):

    """ Hyperlinked MenuItem Serializer """

    class Meta:
        """ Meta data """

        model = MenuItem
        fields = ['id', 'url', 'title', 'price', 'inventory']
