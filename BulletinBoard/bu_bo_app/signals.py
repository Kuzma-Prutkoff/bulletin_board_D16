from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import UserResponse


# Сигнал при создании коммента на статью
@receiver(post_save, sender=UserResponse)
def comment_created(sender, instance, created, **kwargs):
    author_article = instance.article.author.username # автор статьи (через модель UserResponse)
    author_comment = instance.author                  # автор коммента поле  модели UserResponse
    send_mail(
        subject='На твою статью  написали коммент',
        message=f'{author_article} тебе коммент от {author_comment}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[instance.article.author.email] # почта автора статьи
    )


# Сигнал при переводе статуса коммента из False в True
@receiver(post_save, sender=UserResponse)
def comment_accept(sender, instance, created, **kwargs):
    if instance.status: # если отклик принят автором объявления (ФОЛС поменялось на ТРУ), то письмо автору отклика
        send_mail(
            subject='Your comment was accepted',
            message=f'{instance.author.username} твой коммент к статье "{instance.article.title}" приняли',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.author.email] # почта автора коммента
    )
