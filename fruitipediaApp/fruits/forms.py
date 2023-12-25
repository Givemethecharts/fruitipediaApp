from django import forms

from fruitipediaApp.fruits.models import Fruit, Category


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryCreateForm(CategoryBaseForm):
    pass


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitCreateForm(FruitBaseForm):
    pass


class FruitEditBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class FruitEditForm(FruitEditBaseForm):
    pass


class FruitDeleteBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = "__all__"

class FruitDeleteForm(FruitDeleteBaseForm):
    pass