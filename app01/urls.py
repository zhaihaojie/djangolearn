from django.urls import path, re_path
from . import views


urlpatterns = [
    path("hello/", views.hello),
    # 精确格式匹配
    # path("year/2022", articla_year),
    # 路由转换器格式匹配
    path(
        "year/<int:year>", views.articla_year
    ),  #  默认为字符串str 可以不写 另外还有int slug uuid path
    # path("<int:year>/<int:month>", articla_month), # int
    path("<int:year>/<int:month>/<slug:flag>", views.articla_flag),  # slug 可以匹配任意字符串
    # 正则表达式匹配
    re_path(r"^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.articla_month),
    path("current", views.get_current_datetime),
]
