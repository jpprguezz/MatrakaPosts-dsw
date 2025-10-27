from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('alias', 'content')
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escribe un comentario...'})
        }