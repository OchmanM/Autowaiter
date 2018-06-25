# Generated by Django 2.0.2 on 2018-05-25 15:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20180525_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('isFree', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='opened_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date_created'),
        ),
        migrations.AddField(
            model_name='order',
            name='tableFK',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.Table'),
        ),
    ]
