# Generated by Django 4.1.3 on 2022-11-18 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('typing_meter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taken_date', models.DateTimeField(verbose_name='date published')),
                ('wpm', models.IntegerField(verbose_name='words per minute')),
                ('accuracy', models.IntegerField(verbose_name='accurate words')),
                ('test_text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='typing_meter.testtext')),
            ],
        ),
    ]
