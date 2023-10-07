from django.contrib import admin
from myapp5.models import Product, Category


@admin.action(description="Сбросить количество продуктов")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    ordering = ['-category', 'quantity']
    list_filter = ['date_added', 'price']
    search_fields = ['description']  # Чем больше полей и размер базы данных, тем сильнее нагружена БД
    search_fields_text = 'Поиск по описанию продукта "descriptions"'
    actions = [reset_quantity]

    """Отдельный продукт"""
    # fields = ['name', 'description', 'category', 'date_added', 'rating']
    readonly_fields = ['date_added', 'rating']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробности для продукта и его категория',
                'fields': ['description', 'category'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity']
            },
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Рейтинг сформирован автоматически на основе оценок пользователей',
                'fields': ['rating', 'date_added'],
            }
        )
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
