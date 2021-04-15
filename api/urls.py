from django.urls import path

from .views import company_list, company_detail, vacancy_detail, vacancy_list, vacancy_topten, company_vacancy
from . import views
urlpatterns = [
    path('', views.index, name='_index_'),
    path('companies/', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies', company_vacancy),
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', vacancy_topten)
]