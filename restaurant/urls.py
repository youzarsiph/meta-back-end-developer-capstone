""" URlConf for the app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant.views import IndexView, AboutView, UserViewSet, BookingViewSet, MenuItemViewSet


router = DefaultRouter(trailing_slash=False)

router.register('users', UserViewSet, 'user')
router.register('bookings', BookingViewSet, 'booking')
router.register('menuitems', MenuItemViewSet, 'menuitem')

app_name = 'restaurant'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),

    # APIs
    path('api/', include(router.urls), name='api'),
]
