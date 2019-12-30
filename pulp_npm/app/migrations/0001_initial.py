# Generated by Django 2.2.9 on 2019-12-30 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0018_auto_20191127_2350'),
    ]

    operations = [
        migrations.CreateModel(
            name='NpmPublication',
            fields=[
                ('publication_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='npm_npmpublication', serialize=False, to='core.Publication')),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
            },
            bases=('core.publication',),
        ),
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
                ('name', models.CharField(max_length=214)),
                ('version', models.CharField(max_length=16)),
            ],
            options={
                'default_related_name': '%(app_label)s_%(model_name)s',
                'unique_together': {('name', 'version')},
            },
            bases=('core.content',),
        ),
    ]
