from django.shortcuts import render
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from commentapp.decorators import comment_ownership_required
from django.utils.decorators import method_decorator

from commentapp.models import Comment
from commentapp.forms import CommentCreationForm
from django.urls import reverse,reverse_lazy
from articleapp.models import Article


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):

        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'
    
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})