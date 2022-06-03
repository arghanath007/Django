from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class StreamPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


# This is basically can be anything from movies, tv shows, podcasts, etc.


class WatchList(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    average_rating = models.FloatField(default=0)
    total_rating = models.IntegerField(default=0)

    # This is a Many(Entertainment) to One(Platform) Relationship. As a entertainment(WatchList) Model has many movies which are connected/linked to one platform.
    platform = models.ForeignKey(
        StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# * One platform can have multiple entertainment(WatchList) objects. But one  entertainment(WatchList) object will have only one platform.


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    body = models.CharField(max_length=500, null=True)

    # This is a Many(Reviews) to one(Entertainment) relationship. As the 'Reviews' Model has many reviews for an entertainment(WatchList) object.
    watchlist = models.ForeignKey(
        WatchList, on_delete=models.CASCADE, related_name="reviews")

    # 'True' means it is a valid/genuine review. 'False' means it is a spam/fake review.
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f'{self.rating} | {self.watchlist.title}')
