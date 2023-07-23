from django.db import models
from django.contrib.auth.models import User


TYPE = (
    ('tank', 'танк'),
    ('heal', 'лечитель'),
    ('damage-diler', 'дд'),
    ('gilde-master', 'гилдмастер'),
    ('merchant', 'барыга'),
    ('quest-giver', 'квестгивер'),
    ('smith', 'кузнец'),
    ('tanner', 'кожевенник'),
    ('potion-maker', 'зельевар'),
    ('spell-master', 'маг'),
)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField(default='А еще я ем траву')
    category = models.CharField(max_length=12, choices=TYPE, default='smith')
    upload = models.ImageField(upload_to='images/', height_field=None, width_field=None,
                               max_length=None, null=True, blank=True)
    date_in = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/articles/{self.id}'

    def __str__(self):  # теперь в админке в списке постов текст|автор№2|title
        return f'{self.author} | {self.title} | {self.text} | {self.upload} | {self.date_in}'


class UserResponse(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='Нету отзыва')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False) # можно принять или не принять отклик

    def __str__(self):  # теперь в админке и не только айди,автор,текст
        return f'{self.id} | {self.author} | {self.text}'
