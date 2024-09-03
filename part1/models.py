from django.db import models


class Player(models.Model):
    first_login_online = models.DateTimeField(null=True)
    points = models.IntegerField()  # Баллы за вход


class Boost(models.Model):
    type = models.CharField(max_length=255)


class PlayerBoosts(models.Model):
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    boost_id = models.ForeignKey(Boost, on_delete=models.CASCADE)
