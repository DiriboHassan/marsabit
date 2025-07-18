# Generated by Django 4.2 on 2025-07-14 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marsabitweb', '0019_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('title', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='departments',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='deptheads',
            name='email',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='executives',
            name='email',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projects',
            name='posted_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
