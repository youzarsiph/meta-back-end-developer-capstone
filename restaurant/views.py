""" Views for the app """


from django.contrib.auth.models import User
from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from restaurant.models import Booking, MenuItem
from restaurant.serializers import UserSerializer, BookingSerializer, MenuItemSerializer


# Static HTML views
class IndexView(TemplateView):
    """ Index View """

    template_name = 'restaurant/index.html'


class AboutView(TemplateView):
    """ About View """

    template_name = 'restaurant/about.html'


# API ViewSets
class UserViewSet(ModelViewSet):
    """ BookingViewSet """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['username', 'email']
    ordering_fields = ['id', 'username', 'email']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSet(ModelViewSet):
    """ BookingViewSet """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    search_fields = ['name', 'guest_number', 'date']
    ordering_fields = ['id', 'name', 'guest_number', 'date']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticatedOrReadOnly]


class MenuItemViewSet(ModelViewSet):
    """ MenuViewSet """

    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    search_fields = ['title', 'price', 'inventory']
    ordering_fields = ['id', 'title', 'price', 'inventory']
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if self.action in ('list', 'retrieve'):
            permission_classes = [IsAuthenticatedOrReadOnly]

        else:
            permission_classes = [IsAuthenticatedOrReadOnly, IsAdminUser]

        return [permission() for permission in permission_classes]
