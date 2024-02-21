import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    # product_type = django_filters.CharFilter(field_name='product_type', lookup_expr='iexact')
    name = django_filters.CharFilter(lookup_expr='icontains')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    # digital = django_filters.BooleanFilter(lookup_expr='iexact')
    

    class Meta:
        model = Product
        fields = [
            # 'product_type', 
            'name', 
            'price__lt', 
            'price__gt', 
            # 'digital',
            ]