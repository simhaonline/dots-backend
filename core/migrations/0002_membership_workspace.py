# Generated by Django 2.2.12 on 2020-04-22 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workspace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('description', models.TextField(blank=True)),
                ('location', models.TextField(blank=True)),
                ('url', models.URLField(blank=True, max_length=500)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('is_default', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('ADMIN', 'Admin'), ('OWNER', 'Owner'), ('MEMBER', 'Member'), ('GUEST', 'Guest')], default='MEMBER', max_length=6)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to=settings.AUTH_USER_MODEL)),
                ('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership', to='core.Workspace')),
            ],
            options={
                'unique_together': {('user', 'workspace')},
            },
        ),
    ]
