from models import PlayerBoosts


def set_boost_after_pass_level(player_id, boost_id) -> None:
    """Зачисдение бустов игроку"""
    player_points = PlayerBoosts(player_id=player_id, boost_id=boost_id)
    player_points.save()


