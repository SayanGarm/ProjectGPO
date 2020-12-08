from django import forms

from .models import Article, Review, STATUS


class ArticleListForm(forms.Form):
    
    STATUS =(   (None, '--------------'),
                ('A', 'Проверена'),
                ('B', 'Требует исправлений'),
                ('C', 'Ожидает проверки') ) 

    author = forms.CharField(required=False, label='Логин')
    status = forms.ChoiceField(choices=STATUS, required=False, label='Статус')

        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'document')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'status')