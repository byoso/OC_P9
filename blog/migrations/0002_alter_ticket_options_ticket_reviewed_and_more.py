# Generated by Django 4.0.2 on 2022-02-22 19:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ('-time_created',)},
        ),
        migrations.AddField(
            model_name='ticket',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(blank=True, max_length=8192, verbose_name='Commentaire'),
        ),
        migrations.AlterField(
            model_name='review',
            name='headline',
            field=models.CharField(max_length=128, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Note'),
        ),
        migrations.AlterField(
            model_name='review',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='blog.ticket'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=128, verbose_name='titre'),
        ),
    ]
