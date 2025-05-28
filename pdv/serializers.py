from rest_framework import routers, serializers, viewsets
from pdv.models import cat_prod, produit, pointv, vente


#API les categorie par marque
class apicatparmarqueserializer(serializers.ModelSerializer):
    class Meta:
        model=cat_prod
        fields='__all__'


#API DETAIL PORDUIT
class api_detaail_produit_serializer(serializers.ModelSerializer):
    class Meta:
        model=produit
        fields='__all__'

#API detail des points de vente
class api_detaail_pointvente_serializer(serializers.ModelSerializer):
    class Meta:
        model=pointv
        fields='__all__'

#API  de vente
class apivente_serializer(serializers.ModelSerializer):
    class Meta:
        model=pointv
        fields='__all__'
