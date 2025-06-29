from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    description = models.TextField()
    category = models.CharField()
    tags = models.CharField(max_length=250, blank=True)
    is_free = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.name
    


class Tutorial(models.Model):
    tool = models.ForeignKey('Tool', on_delete=models.CASCADE, related_name='tutorials')
    title = models.CharField(max_length=200)
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title