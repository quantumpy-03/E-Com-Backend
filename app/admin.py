from django.contrib import admin
from .models import User, CustomerProfile, VendorProfile, UserAddress, ProductCategory, ProductList

admin.site.register([CustomerProfile, VendorProfile, UserAddress])

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'role', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    list_filter = ('role', 'is_staff', 'is_active')
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined', 'email', 'username', 'role', 'password')
    fieldsets = (
        ('Email', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            # Make core fields readonly when editing
            return self.readonly_fields + ('email', 'username', 'role')
        return self.readonly_fields

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description')
    search_fields = ('category_name',)
    ordering = ('category_name',)
    readonly_fields = ('slug',)
    fieldsets = (
        ("Category", {
            "fields": (
                'category_name', 'category_description'
            ),
        }),
    )


@admin.register(ProductList)
class ProductListAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_vendor', 'product_category', 'product_price', 'product_discount','product_specifications', 'product_price_after_discount', 'product_availability', 'product_stock', 'product_created_at', 'product_updated_at', 'slug')
    search_fields = ('product_name', 'product_vendor__username', 'product_category__category_name')
    list_filter = ('product_category', 'product_availability')
    ordering = ('product_name',)
    readonly_fields = ('slug', 'product_price_after_discount', 'product_created_at', 'product_updated_at')
    fieldsets = (
        ('Product Info', {'fields': ('product_vendor', 'product_category', 'product_name', 'product_description', 'product_image', 'product_specifications', 'product_stock')}),
        ('Pricing', {'fields': ('product_price', 'product_discount', 'product_price_after_discount')}),
        ('Availability', {'fields': ('product_availability',)}),
        ('Timestamps', {'fields': ('product_created_at', 'product_updated_at', 'slug')}),
    )

