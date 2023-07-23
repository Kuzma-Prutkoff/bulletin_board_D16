from .models import Article, UserResponse
from datetime import datetime
import datetime
import logging
from celery import shared_task
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)


@shared_task
def task_new_articles_7d(): #задача на отправку статей за неделю всем залогиненным запускается в селери по пн-8:00
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    articles = Article.objects.filter(date_in__gte=last_week) # посты больше или = чем неделя отроду
    login_users = User.objects.all().values_list('email', flat=True)
    html_content = render_to_string('weekly_articles.html', {'link': settings.SITE_URL, 'articles': articles})
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='', # у нас шаблон weekly_articles.html, там все напишем
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=login_users
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
