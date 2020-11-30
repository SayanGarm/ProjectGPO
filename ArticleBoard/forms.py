from django import forms

from .models import Article

class ArticleListForm(forms.Form):
    search = forms.CharField(required=False)
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'