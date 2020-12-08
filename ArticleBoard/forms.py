from django import forms

from .models import Article, Review

class ArticleListForm(forms.Form):
    search = forms.CharField(required=False)
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'document')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content', 'status')