from django.db import models

# Create your models here.
class TransData(models.Model):
    source_text = models.TextField(blank=True, null=True)
    source_lang = models.CharField(max_length=255)
    target_lang = models.CharField(max_length=255)
    trans_text = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)


