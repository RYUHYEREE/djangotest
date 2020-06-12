from django.conf import settings
from django.db import models
from django.utils import timezone

#Post는 모델의 이름입니다. (특수문자와 공백 제외한다면) 다른 이름을 붙일 수도 있습니다. 항상 클래스 이름의 첫 글자는 대문자로 써야 합니다.
#models은 Post가 장고 모델임을 의미합니다. 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됩니다.
class Post(models.Model):
#models.ForeignKey - 다른 모델에 대한 링크를 의미합니다.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#models.CharField - 글자 수가 제한된 텍스트를 정의할 때 사용합니다. 글 제목같이 짧은 문자열 정보를 저장할 때 사용합니다.
    title = models.CharField(max_length=200)
#models.TextField - 글자 수에 제한이 없는 긴 텍스트를 위한 속성입니다. 블로그 콘텐츠를 담기 좋겠죠?
    text = models.TextField()
#models.DateTimeField - 날짜와 시간을 의미합니다.
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#참고/ https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types)
