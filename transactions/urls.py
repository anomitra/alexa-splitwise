from django.conf.urls import url

from transactions import views

urlpatterns = [
    url(
        # r'^transactions/(?P<vehicle_id>[a-f0-9-]+)/history/transfers/$',
        r'^transactions/$',
        views.TransactionViewSet.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='transactions',
    ),
]
