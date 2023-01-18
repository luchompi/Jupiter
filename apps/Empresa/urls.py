from django.urls import path as p
from . import views as v
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  p('sedes/',v.SedeListAPI.as_view()),
  p('sedes/search/<kword>',v.SedeQueryAPI.as_view()),
  p('sedes/details/<pk>',v.SedeDetailAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)