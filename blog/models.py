from django.db import models
from django.utils import timezone

# Create your models here.

# Postという名のクラスを作る←Djangoのモデル
# class 〜 で、オブジェクトを定義すると宣言
# models.Model←PostはDjangoのモデルで、DBにセーブしろ的なことをDjangoに伝える


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# models.CharField←文字制限のあるテキスト
# models.TextField←制限なし長文用のフィールド
# models.DateTimeField←日付と時間
# models.ForeignKey←他のモデルへのリンク
# 詳細はこちら → https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types

    def publish(self):
        self.published_date = timezone.now()
        self.save()

# def publish(self)は、記事公開用の関数(メソッド)

    def __str__(self):
        return self.title
