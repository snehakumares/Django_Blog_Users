from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.index, name='index'),
    path('signupdata', views.signupdata, name='signupdata'),
    path('doctor/<int:id>', views.doctor, name='doctor'),
    path('patient/<int:id>', views.patient, name='patient'),
    path('addblog', views.addblog, name='addblog'),
    path('doctor/<int:id>/drafts', views.drafts, name='drafts'),
    path('doctor/<int:id>/blogs', views.blogs, name='blogs'),
    path('doctor/<int:id>/draft/<int:blogid>', views.update, name='update'),
    path('doctor/<int:id>/draft/<int:blogid>/updaterecord', views.updaterecord, name='updaterecord'),
    path('patient/<int:id>/viewblogs/<int:catid>', views.viewblogs, name='viewblogs'),
    path('patient/<int:id>/viewblogs/blog/<int:blogid>', views.viewblog, name='viewblog'),
    path('doctor/<int:id>/blog/<int:blogid>', views.docviewblog, name='viewblog'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)