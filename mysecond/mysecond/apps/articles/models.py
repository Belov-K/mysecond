from django.db import models

class Article(models.Model):
    article_title=models.CharField('Название статьи', max_lenght=200)
    article_text=models.TextField('Текст статьи')
    pub_date=models.DateTimeField('дата публикации')

class Comment(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    authon_name=models.CharField('имя пользователя', max_lenght=50)
    comment_text=models.CharField('Текст комментария', max_lenght=200)
