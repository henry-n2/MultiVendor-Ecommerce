from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    experience_years = models.PositiveIntegerField()
    award_title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/', null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
