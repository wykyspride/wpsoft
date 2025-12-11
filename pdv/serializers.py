from rest_framework import routers, serializers, viewsets
from pdv.models import cat_prod, produit, Client, vente, ligne_vente, User
from django.db.models import Count, Sum


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
        model=Client
        fields='__all__'

#API  de vente
class apivente_serializer(serializers.ModelSerializer):
    class Meta:
        model=vente
        fields='__all__'


#API lignes  de vente
class apilignev_serializer(serializers.ModelSerializer):
    class Meta:
        model=ligne_vente
        fields='__all__'

#API ventes par vendeur 
class apiventeparvendeur_serializer(serializers.ModelSerializer):
    class Meta:
        model=vente
        fields='__all__'


#API ventes apikpiterritoire
class apikpiterritoire_serializer(serializers.ModelSerializer):
    class Meta:
        model=vente
        fields='__all__'

#API ventes apikpiterritoire
class apiuser_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'