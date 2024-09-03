import csv

from django.db.models import Prefetch
from django.http import HttpResponse

from .models import PlayerLevel, PlayerPrizeLevel


def set_prize(request):
    """Проверка метода присвоения приза"""
    playerlevel = PlayerLevel.objects.get(player=3)
    playerlevel.set_prize()
    return HttpResponse()


def write_csv(request):
    players_levels = PlayerLevel.objects.all().select_related("level", "player").prefetch_related(
        Prefetch(
            'player__playerprizelevel_set',
            queryset=PlayerPrizeLevel.objects.select_related('prize', 'level'),
            to_attr='prizes_on_levels'
        )
    )

    with open('data.csv', "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=("id", "level_name", "is_completed", "prize"))
        writer.writeheader()
        for players_level in players_levels:
            # В ТЗ указано найти полученный приз за уровень, однако у игрока уже могут имется уровни. Поэтому я решил, что
            # имеется в виду только ПОСЛЕДНИЙ полученный приз
            player_prize_level = players_level.player.prizes_on_levels[-1] if players_level.player.prizes_on_levels else None
            writer.writerow(
                {
                    "id": players_level.player.player_id,
                    "level_name": player_prize_level.level.title,
                    "is_completed": players_level.is_completed,
                    "prize": player_prize_level.prize.title
                }
            )
    return HttpResponse()
