from django.conf.urls import patterns, url ,include

from main_app.views import IndexView
from rest_framework_nested import routers

from authentication.views import AccountViewSet
# from authentication import views
# from routers.urls import urlpatterns
from authentication.views import LoginView
from authentication.views import LogoutView

from posts.views import AccountPostsViewSet, PostViewSet
from main_app.views import IndexView


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'posts', AccountPostsViewSet)


urlpatterns = patterns(
    '',

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url('^.*$', IndexView.as_view(), name='index'),
)
