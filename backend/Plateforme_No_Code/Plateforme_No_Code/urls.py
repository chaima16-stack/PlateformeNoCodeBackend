
from django.contrib import admin
from django.urls import path, include
from App.views import *
from rest_framework.schemas import get_schema_view
from User.views import *
from ManageDatabases.views import *
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from Databases.views import *
from Workflow.views import *
schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      contact=openapi.Contact(email="benghorbalchaima@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('apps/', AppListCreateAPIView.as_view(), name='app-list'),
    path('apps/<int:pk>/', AppDetailAPIView.as_view(), name='app-detail'),
    path('screens/', ScreenListCreateAPIView.as_view(), name='screen-list'),
    path('screens/<int:pk>/', ScreenDetailAPIView.as_view(), name='screen-detail'),
    path('appScreens/', ScreensByAppAPIView.as_view(), name='screens_by_app'),
    path('elements/', ElementListCreateAPIView.as_view(), name='element-list'),
    path('elements/<str:pk>/', ElementDetailAPIView.as_view(), name='element-detail'),
    path('elementByScreens/',ElmentByScreenAPIView.as_view(), name='element_by_screen'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('appbyUser/', AppByUserAPIView.as_view(), name='app_by_user'),
    path('relations/', RelationListCreate.as_view(), name='relation-list'),
    path('relations/<int:pk>/', RelationDetailAPIView.as_view(), name='relation-detail'),
    path('databases/', DatabaseListCreate.as_view(), name='database-list'),
    path('databases/<int:pk>/', DatabaseDetailAPIView.as_view(), name='database-detail'),
    path('attributes/', AttributeListCreate.as_view(), name='attribute-list'),
    path('attributes/<int:pk>/', AttributeDetailAPIView.as_view(), name='attribute-detail'),
    path('attributesByEntity/',AttributeByEntityAPIView.as_view(), name='attribute_by_entity'),
    path('entities/', EntityListCreate.as_view(), name='entities-list'),
    path('entities/<int:pk>/', EntityDetailAPIView.as_view(), name='entities-detail'),
    path('entitiesByDatabase/', EntitiesByDatabaseAPIView.as_view(), name='entities_by_db'),
   
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
   
    path('DatabasesApp/', CreateDatabaseAPIView.as_view(), name='db'),
    path('Collection/', CollectionAPIView.as_view(), name='collection'),
    path('Document/', DocumentsAPIView.as_view(), name='get_documents'),
    path('DocumentsById/', DocumentFilterAPIView.as_view(), name="get_document_by_id"),
    path('Attribute/', AttributesAPIView.as_view(), name='attributes'),


    path('events/', EventListCreate.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailAPIView.as_view(), name='event-detail'),
    path('actions/', ActionListCreate.as_view(), name='action-list'),
    path('actions/<int:pk>/', ActionDetailAPIView.as_view(), name='action-detail'),
    path('elementsactions/', ElementActionListCreate.as_view(), name='elementaction-list'),
    path('elementsactions/<int:pk>/', ElementActionDetailAPIView.as_view(), name='elementaction-detail'),
    path('EventByElement/', EventByElementAPIView.as_view(), name='event_by_element'),
    path('ActionByEvent/', ActionByEventAPIView.as_view(), name='action_by_event'),
    path('Actionelement/' , ActionElementAPIView.as_view(), name='action_by_element'),

    path('login/', GoogleOAuthLogin.as_view(), name='google_oauth_login'),
    path('DecodeToken/', DecodeTokenView.as_view(), name='Decode_token'),
     path('Token/', GetToken.as_view(), name='get_token'),
]
