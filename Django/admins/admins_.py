"""
sources:
    https://docs.djangoproject.com/en/4.0/ref/contrib/admin/

----------------------------------------------------------------------------------------------------------
                                файл admin.py

есть два споссоба добавлять классы к админке:

1) через вызов напрямую admin.site.register(SomeModel, SomeModelModelAdmin)

2) через декоратор @admin.register(SomeModel) над классом унаследоавнным от ModelAdmin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated',]
    list_editable = ['price', 'available',]
    prepopulated_fields = {'slug': ('name',),}

list_display - то что мы видим в общем списке

list_filter - те поля, по которым мы можем фильтровать

list_editable - добавляет возможность изменять перечисленные поля со страницы списков

list_editable - добавляет возможность изменять перечисленные поля со страницы списков
                но все поля list_editable должны быть обязательно в list_display

prepopulated_fields - словарь, который автоматически преобразует поле (ключ),
                по выбранному значению. чаще всего используется для добавления слага через админку

TabularInline
Оень интересная логика у TabularInline. Этот класс позволяет присоединиться к классу с которым связан
по ForeignKey, ManyToMany, OneToOneField
Вот как выглядит
    class OrderItemTabularInline(admin.TabularInline):
        model = OrderItem
        raw_id_fields = ['product', ]
    @admin.register(Order)
    class OrderModelAdmin(admin.ModelAdmin):
        list_display = ['pk', 'first_name', 'last_name',
                        'email', 'address', 'postal_code',
                        'city', 'created', 'updated', 'paid', ]
        list_filter = ['paid', 'created', 'updated', ]
        inlines = [OrderItemTabularInline, ]
см. результат
http://127.0.0.1:8000/admin/orders/order/add/

1) Создаешь в admin.py класс, который наследуется от admin.TabularInline
2) Указываешь в этом классе аттрибут model (с какой моделью будет работать этот класс)
3) Присваиваешь этот класс в списке в аттрибуте inlines
в классе, в котором хочешь, чтобы эта модель отображалась

Добавление собственных действий в сайт администрирования, например
вывод информации из бд в формат csv
https://docs.djangoproject.com/en/3.2/howto/outputting-csv/

Когда мы расширяем стандартные страницы сайта администрирования - нужно знать, какие блоки использует django
блоки в базовом шаблоне сайта администрирования django:
https://github.com/django/django/tree/main/django/contrib/admin/templates/admin

Чтобы переопределить шаблоны django - достаточно воспроизвести иерархию папок
сайта администрирования django в каталоге templates нашего приложения
тогда django будет находить файлы первыми и использовать их

А в остальном смотри в приложении orders
обрати внимание, на то, то мы передали функцию в list_display  - order_detail
посмотри на что эта функция ссылается и все такое

Важно!! запомни декоратор @staff_member_required
Он очень важный для работы с админкой
staff_member_required - проверяет у request.user - is_staff==True и admin==True

from django.contrib.admin.views.decorators import staff_member_required
----------------------------------------------------------------------------------------------------------





Работа с admin.py в django очень сложная
у admin.py много возможностей

вот пример, как мы работаем с admin.py,
когда переопределяем кастомную модель User

-----------------------------------------
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from customauth.models import MyUser


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
-----------------------------------------


"""