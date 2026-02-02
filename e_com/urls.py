from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Project API",
        default_version="v1",
        description="""
        API documentation for the E-commerce project.

        To test protected endpoints that require authentication:
        1.  Use the `/api/drf/v1/login/` endpoint with your credentials to get an `access` token.
        2.  Click the green **Authorize** button on this page.
        3.  In the dialog that appears, enter `Bearer <your_access_token>` into the value field.
        4.  Click **Authorize** and close the dialog. Your requests will now be authenticated.
    """,
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # admin login
    path("admin/", admin.site.urls),
    # drf urls
    path("api/drf/v1/", include("app.urls")),
    # swagger urls
    path(
        "api/swagger/v1/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # redoc urls
    path(
        "api/redoc/v1/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc-ui",
    ),
]
