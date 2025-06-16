from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter # Importa o router
# Uploader
from django.conf import settings
from django.conf.urls.static import static
from uploader.router import router as uploader_router
# Autenticação
from usuario.router import router as usuario_router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Documentação
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
# Views
from emovepro.views import CategoriaViewSet, MarcaViewSet, ProdutoViewSet, CompraViewSet
from usuario.views import UsuarioViewSet
from pagamentos.views import paymentCard, oauth

# Inicialização do router:
router = DefaultRouter()
# Rotas
router.register(r"categorias", CategoriaViewSet)
router.register(r"marcas", MarcaViewSet)
router.register(r"produtos", ProdutoViewSet)
router.register(r"usuarios", UsuarioViewSet)
router.register(r"compra", CompraViewSet)
# Endpoints
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    # Usuario
    path("api/", include([
        path("", include(usuario_router.urls)),
        # Autenticação
        path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
        # Uploader
        path("media/", include(uploader_router.urls)),
        # Documentação
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path("swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
        path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    ])),
    # Pagamento
    path('payment/', include([
        path("card/", paymentCard)
    ])),
    path('oauth/', oauth)
]
urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)