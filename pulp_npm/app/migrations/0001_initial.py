# Generated by Django 2.2.9 on 2019-12-27 19:10

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0018_auto_20191127_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='NpmRemote',
            fields=[
                ('remote_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='npm_npmremote', serialize=False, to='core.Remote')),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.remote',),
        ),
        migrations.CreateModel(
            name='NpmRepository',
            fields=[
                ('repository_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='npm_npmrepository', serialize=False, to='core.Repository')),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.repository',),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('content_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='npm_package', serialize=False, to='core.Content')),
                ('_id', models.CharField(max_length=214)),
                ('_rev', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=214)),
                ('description', models.TextField()),
                ('dist_tags', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('versions', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('maintainers', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('time', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('repository', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('readme', models.TextField()),
                ('readme_filename', models.CharField(max_length=255)),
                ('homepage', models.CharField(max_length=255)),
                ('keywords', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
                ('bugs', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('users', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('license', models.CharField(max_length=16)),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.content',),
        ),
    ]
