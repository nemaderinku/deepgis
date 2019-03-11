# Generated by Django 2.1.7 on 2019-03-05 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '0007_auto_20180514_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zoom_level', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TileSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_location', models.CharField(max_length=600)),
            ],
        ),
        migrations.AddField(
            model_name='tile',
            name='tile_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webclient.TileSet'),
        ),
    ]
