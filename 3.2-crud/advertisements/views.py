from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .models import Advertisement


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.filter()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, ]
    filter_class = AdvertisementFilter

    def get_permissions(self):
        return [IsAuthenticatedOrReadOnly(), IsOwner()]
