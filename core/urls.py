# Django
from django.contrib import admin
from django.urls import path, include

# 3rd party swagger for documentation
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Point Of Sales API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('core.customers.urls')),
    path('joins/', include('core.joins.urls')),
    path('laters/', include('core.laters.urls')),
    path('questions/', include('core.questions.urls')),
    path('docs/', include_docs_urls(title="POS_API Documentation")),
]
