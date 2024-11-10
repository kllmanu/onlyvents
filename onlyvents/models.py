from django.db import models

SETTINGS = {
    "Twitter": {
        "TWITTER_USERNAME": "TWITTER_USERNAME",
        "TWITTER_PASSWORD": "TWITTER_PASSWORD"
    }
}

class Setting(models.Model):
    name = models.CharField(choices=SETTINGS, max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"

class Source(models.Model):
    name = models.CharField(max_length=255, blank=True)
    url = models.URLField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Source"
        verbose_name_plural = "Sources"

class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    sources = models.ManyToManyField(Source)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"

class Filter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    query = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Filter"
        verbose_name_plural = "Filters"