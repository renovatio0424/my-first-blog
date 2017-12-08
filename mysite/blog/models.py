from django.db import models
from django.utils import timezone
# Create your models here.


"""
class : 객체 정의
Post : 모델의 이름 (주의: 특수문자와, 공백, 첫글자 대문자)
models: Post가 장고 모델임을 의미, 이 코드로 데이터 베이스에 저장


models.CharField: 글자 수가 제한된 텍스트를 정의할 때 사용, 글 제목 같이 짧은 문자열 정보 저장할때 사용
models.TextField: 글자 수에 제한이 없는 긴 텍스트를 위한 속성입니다. 블로그 콘텐츠를 담기 좋겠죵?
models.DateTimeField: 날짜와 시간을 의미합니다.
models.ForeignKey: 다른 모델에 대한 링크를 의미합니다.
"""
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
