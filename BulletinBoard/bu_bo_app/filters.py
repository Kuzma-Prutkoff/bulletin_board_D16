import django_filters
from .models import TYPE


class ArticleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Поиск по названию статьи')
    category = django_filters.ChoiceFilter(choices=TYPE, label='Категория', empty_label='Выбери категорию',)




