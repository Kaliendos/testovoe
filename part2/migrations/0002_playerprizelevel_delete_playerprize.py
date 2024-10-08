# Generated by Django 5.1 on 2024-09-03 16:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPrizeLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part2.level')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part2.player')),
                ('prize', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='part2.prize')),
            ],
        ),
        migrations.DeleteModel(
            name='PlayerPrize',
        ),
    ]
