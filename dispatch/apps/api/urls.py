from django.conf.urls import url

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from dispatch.apps.api import views

router = routers.DefaultRouter()

router.register(r'articles', views.ArticleViewSet, base_name='articles')
router.register(r'frontpage', views.FrontpageViewSet, base_name='frontpage')
router.register(r'sections', views.SectionViewSet, base_name='sections')
router.register(r'person', views.PersonViewSet, base_name='person')
router.register(r'tag', views.TagViewSet)
router.register(r'images', views.ImageViewSet, base_name='images')


section_frontpage = views.SectionViewSet.as_view({
    'get': 'frontpage',
})

component = views.ComponentViewSet.as_view({
    'get': 'detail',
    'post': 'update',
})

urlpatterns = format_suffix_patterns([
    # Extra section routes
    url(r'^sections/(?P<pk>[0-9]+)/frontpage/$', section_frontpage, name='section-frontpage'),
    url(r'^sections/(?P<slug>[\w-]+)/frontpage/$', section_frontpage, name='section-frontpage'),
    url(r'^components/(?P<slug>[\w-]+)/$', component, name='component'),
]) + router.urls