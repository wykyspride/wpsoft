from .serializers import apicatparmarqueserializer, api_detaail_produit_serializer, api_detaail_pointvente_serializer, apivente_serializer
from .models import cat_prod, produit, pointv
from rest_framework import viewsets

#API les categorie par marque
class apicatparmarqueviewset(viewsets.ModelViewSet):
    queryset=cat_prod.objects.all()
    serializer_class=apicatparmarqueserializer

#API details produit
class api_details_produit_viewset(viewsets.ModelViewSet):
    serializer_class=api_detaail_produit_serializer


#API details point de vente
class api_details_pointvente_viewset(viewsets.ModelViewSet):
    serializer_class=api_detaail_pointvente_serializer



#API de vente
class apivente_viewset(viewsets.ModelViewSet):
    serializer_class=apivente_serializer