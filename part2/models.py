from django.db import models

from .exceptions import PrizeNotFoundError


class Player(models.Model):
    player_id = models.CharField(max_length=100)


class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)


class Prize(models.Model):
    title = models.CharField()


class PlayerPrizeLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)


class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)

    def set_prize(self):
        if self.is_completed:
            level_prize = LevelPrize.objects.get(level=self.level)
            if not level_prize:
                raise PrizeNotFoundError(f"Приз для уровня {self.level} не найден")
            player_prize = PlayerPrizeLevel(player=self.player, prize=level_prize.prize, level=self.level)
            player_prize.save()


class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()
