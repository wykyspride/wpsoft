
from django.contrib import admin
from django.urls import path,include
from pdv.views import home, conex,deconex,venteparcom,venteparpv,venteparmarque,venteparcat, zonecouve,etatvente,stativente, apivente,apilignev, espaceuser,maquette, adtypepoint,typepointvente,pointdevente,marqueprod,catprod, prod, apicatparmarque, commerciaux, apidetailprod, apidetailpoitv, lignevente
from django.conf import settings
from django.conf.urls.static import static
from pdv.api import apicatparmarqueviewset, api_details_pointvente_viewset, api_details_produit_viewset, apivente_viewset, apilignev_viewset
from rest_framework.routers import DefaultRouter 


#Creation d'API avec rest_framework
router=DefaultRouter()
router.register(r'apicatparmarque',apicatparmarqueviewset,basename='apicatparmarque')
router.register(r'apidetailprod',api_details_produit_viewset,basename='apidetailprod')
router.register(r'apidetailpoitv',api_details_pointvente_viewset,basename='apidetailpoitv')
router.register(r'apivente',apivente_viewset,basename='apivente')
router.register(r'apilignev',apilignev_viewset,basename='apilignev')


urlpatterns = [
    path('', conex, name="conex"),
    path('admin/', admin.site.urls),

    path('apidetailprod',apidetailprod, name="apidetailprod"),
    path('apidetailpoitv',apidetailpoitv, name="apidetailpoitv"),
    path('apicatparmarque/',apicatparmarque, name="apicatparmarque"),
    path('apivente/',apivente, name="apivente"),
    path('apilignev/',apilignev, name="apilignev"),

    #path('apicatparmarque', include(router.urls)),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) ,   
    path('maquette', maquette, name="maquette"),
    path('espaceuser/<int:iduser>',espaceuser, name="espaceuser"),
    path('adtypepoint', adtypepoint, name="adtypepoint"),
    path('typepointvente', typepointvente, name="typepointvente"),
    path('pointdevente', pointdevente, name="pointdevente"),
    path('marqueprod', marqueprod,name="marqueprod"),
    path('catprod', catprod,name="catprod"),
    path('prod', prod, name="prod"),
    path('commercial', commerciaux, name="commercial"),
    path('lignevente/<int:idvente>', lignevente, name="lignevente"),
    path('deconex',deconex,name='deconex'),# Deconnexion de l'utilisateur
    path('zonecouve',zonecouve, name="zonecouve"),
    path('etatvente/<int:idvente>', etatvente, name="etatvente"),
    path('stativente',stativente, name="stativente"),
    path('venteparcom',venteparcom, name="venteparcom"),
    path('venteparpv',venteparpv, name="venteparpv"),
    path('venteparmarque',venteparmarque, name="venteparmarque"),
    path('venteparcat',venteparcat, name="venteparcat"),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
