from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateTimeField( default= timezone.now)
    # price = models.IntegerField(null=True)
    score = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
    rating1=models.IntegerField(choices=score, default=3,)
    rating2=models.IntegerField(choices=score, default=3,)
    rating3=models.IntegerField(choices=score, default=3,)
    director = models.CharField(max_length=50, default = "")
    # video = models.FileField(null= True)
    img = models.FileField(null = True)
    price = models.IntegerField(default=0)
    post_hit = models.PositiveIntegerField(default=0)
    post_like = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])

    @property
    def update_counter(self):
        self.post_hit = self.post_hit + 1
        self.save()
    
    @property
    def like_update_counter(self):
        self.post_like = self.post_like + 1
        self.save()
        
class CfPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    director = models.CharField(max_length=50, default = "")
    duration = models.IntegerField(default = 0)
    img = models.FileField(null = True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments') #댓글이 속한 글이 지워지면 댓글들도 다 지우도록 함.
    content = models.TextField()
    
class CfComment(models.Model):
    cfpost = models.ForeignKey(CfPost, on_delete = models.CASCADE, related_name='cfcomments', null=True) #댓글이 속한 글이 지워지면 댓글들도 다 지우도록 함.
    cfcontent = models.TextField()