import django_filters
from .models import Product, type_choices

class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    type = django_filters.ChoiceFilter(field_name='type', choices=type_choices)
    digital = django_filters.BooleanFilter(lookup_expr='iexact')
    

    class Meta:
        model = Product
        fields = [
            'name', 
            'price__lt', 
            'price__gt', 
            'type', 
            'digital',
            ]