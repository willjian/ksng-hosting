# Generated by Django 2.2 on 2020-04-01 08:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('websiteManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default=None, max_length=255)),
                ('type', models.SmallIntegerField(default=0)),
                ('user', models.CharField(default=None, max_length=255, null=True)),
                ('password', models.CharField(default=None, max_length=255, null=True)),
                ('ip', models.CharField(default=None, max_length=255, null=True)),
                ('serial', models.IntegerField(default=None, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('provision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='websiteManager.Provision')),
            ],
            options={
                'db_table': 'wafs',
            },
        ),
    ]
