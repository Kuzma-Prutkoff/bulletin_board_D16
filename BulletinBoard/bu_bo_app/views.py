from .models import Article, UserResponse
from .filters import ArticleFilter
from .forms import ArticleForm, ArticleCommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect


class ArticlesList(ListView):
    model = Article
    ordering = 'title'
    template_name = 'articles.html'
    context_object_name = 'articles' #имя для шаблона
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset  # Добавляем в контекст объект фильтрации(в шаблоне внутри формы)
        return context

    def get_queryset(self):  # Переопределяем функцию получения списка новостей
        queryset = super().get_queryset() # Получаем обычный запрос
        # Используем наш класс фильтрации.self.request.GET содержит объект QueryDict.
        # Сохраняем нашу фильтрацию в объекте класса,чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ArticleFilter(self.request.GET, queryset)
        return self.filterset.qs # Возвращаем из функции отфильтрованный список новостей


class ArticleDetail(DetailView): # в этом КП статья+все комменты этой статьи
    model = Article
    template_name = 'article.html'
    context_object_name = 'article'

# если переопредлить метод гет, то get_context_data вообще не будет работать, так что в return возврат его основн свойств
    def get(self, request, pk, *args, **kwargs):  # переопределяем метод гет, если страница не сущест http://127.0.0.1:8000/articles/99
        try:
            article = Article.objects.get(pk=pk)
        except:          # чтобы не было ошибки 500 (если запрос будет на несуществующ страницу)
            return HttpResponse(content=(f'НЕТУ object {pk} does not exists'), status=404)
        return super().get(self, request, *args, **kwargs) # возвращаем основные методы def get иначе могут быть проблемы

# в UserResponse из поля article __ в Article поле id = экземляр словаря kwargs объекта ArticleDetail, номер статьи по ключу "рк"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_comments_ofthis_atricle'] = UserResponse.objects.filter(article__id=self.kwargs['pk'])
        return context


class ArticleCreate(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'
    raise_exception = True  # если прав на доступ нет, то выброс на шаблон 403

    # автозаполнение поле-автор на залогиненного юзера, чтобы ввариантов не было писать за других
    def form_valid(self, form): # для корректного создания статьи уже с автором, иначе можно писать от кого угодно
        fields = form.save(commit=False) # создаем форму, но не отправляем в БД
        fields.author = self.request.user # присваиваем полю сразу залогиненного автора
        return super().form_valid(form)


class ArticleUpdate(LoginRequiredMixin, UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'article_edit.html'


class ArticleDelete(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles_list')


class PrivateArticleCommentList(LoginRequiredMixin, ListView): # личная страничка
    model = UserResponse
    template_name = 'private_comment_list.html'
    ordering = 'author'
    success_url = reverse_lazy('private_comment_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Фильтруем список статей. (поле author из Article) = (имя юзера, который залогинен)
        context['my_articles'] = Article.objects.filter(author=self.request.user)
        # Фильтруем список комментов. (поле article из UserResponse __ в поле author из Article) = (имя юзера, который залогинен)
        context['my_comments'] = UserResponse.objects.filter(article__author=self.request.user)
        return context


class CommentDetail(LoginRequiredMixin, DetailView):
    model = UserResponse
    template_name = 'comment_detail.html'
    context_object_name = 'comment'


def comment_accept(request, pk):                    # функция меняем статус коммента на ДА
    user_response = UserResponse.objects.get(id=pk) # берем номер коммента
    user_response.status = True                     # меняем статус этого коммента на ОК
    user_response.save()                            # сохраняем
    return render(request, 'accept.html')


def comment_deny(request, pk):                      # функция меняем статус коммента на НЕТ
    user_response = UserResponse.objects.get(id=pk)
    user_response.status = False
    user_response.save()
    return render(request, 'deny.html')


class CommentCreate(LoginRequiredMixin, CreateView):
    form_class = ArticleCommentForm
    model = UserResponse
    template_name = 'comment_create.html'
    success_url = reverse_lazy('private_comment_list') # пока сюда переброс. надо подумать куда перебрасывать
    raise_exception = True  # если прав на доступ нет, то выброс на шаблон 403

    # автозаполнение полей автор-коммента и номера-статьи на которую написан комментарий
    def form_valid(self, form):
        response = form.save(commit=False)
        response.article = Article.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        response.author = self.request.user
        return super().form_valid(form)


class CommentUpdate(LoginRequiredMixin, UpdateView):
    form_class = ArticleCommentForm
    model = UserResponse
    template_name = 'comment_edit.html'
    success_url = reverse_lazy('private_comment_list')


class CommentDelete(LoginRequiredMixin, DeleteView):
    model = UserResponse
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('private_comment_list')
    context_object_name = 'comment'

