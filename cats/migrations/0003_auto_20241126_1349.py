# Generated by Django 3.2 on 2024-11-26 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_auto_20241126_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='AchievementCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.achievement')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cats.cat')),
            ],
        ),
        migrations.AddField(
            model_name='cat',
            name='achievements',
            field=models.ManyToManyField(through='cats.AchievementCat', to='cats.Achievement'),
        ),
    ]
