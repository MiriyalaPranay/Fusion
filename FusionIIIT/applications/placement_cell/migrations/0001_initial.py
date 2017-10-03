# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-03 07:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.CharField(default='', max_length=100)),
                ('achievement_type', models.CharField(choices=[('EDUCATIONAL', 'Educational'), ('OTHER', 'Other')], default='OTHER', max_length=20)),
                ('description', models.CharField(default='', max_length=250)),
                ('issuer', models.CharField(default='', max_length=200)),
                ('date_earned', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChairmanVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=100)),
                ('loaction', models.CharField(default='', max_length=100)),
                ('visiting_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('description', models.CharField(default='', max_length=1000)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coauthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coauthor_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Coinventor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coinventor_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ContactCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='', max_length=100)),
                ('hr_mail', models.CharField(default='', max_length=100)),
                ('reference', models.CharField(default='', max_length=1000)),
                ('description', models.CharField(default='', max_length=500)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=250)),
                ('license_no', models.IntegerField(default='')),
                ('sdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('edate', models.DateField(blank=True, null=True)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(default='', max_length=40)),
                ('institute', models.CharField(default='', max_length=250)),
                ('stream', models.CharField(default='', max_length=150)),
                ('sdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('edate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('status', models.CharField(choices=[('ONGOING', 'Ongoing'), ('COMPLETED', 'Completed')], default='COMPLETED', max_length=20)),
                ('description', models.CharField(default='', max_length=500)),
                ('company', models.CharField(default='', max_length=200)),
                ('location', models.CharField(default='', max_length=200)),
                ('sdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('edate', models.DateField(blank=True, null=True)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Has',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(default='', max_length=100)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Know',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MessageOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(default='', max_length=100)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NotifyStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement_type', models.CharField(choices=[('PLACEMENT', 'Placement'), ('PBI', 'PBI'), ('HIGHER STUDIES', 'Higher Studies'), ('OTHER', 'Other')], default='PLACEMENT', max_length=20)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('ctc', models.DecimalField(decimal_places='2', default='0.0', max_digits='5')),
                ('description', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_name', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=250)),
                ('patent_office', models.CharField(default='', max_length=250)),
                ('patent_date', models.DateField()),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlacementRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placement_type', models.CharField(choices=[('PLACEMENT', 'Placement'), ('PBI', 'PBI'), ('HIGHER STUDIES', 'Higher Studies'), ('OTHER', 'Other')], default='PLACEMENT', max_length=20)),
                ('name', models.CharField(default='', max_length=100)),
                ('ctc', models.DecimalField(decimal_places='2', default='0.0', max_digits='5')),
                ('year', models.IntegerField(default='0')),
                ('test_score', models.IntegerField(default='0')),
                ('test_type', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PlacementSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('placement_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('location', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=500)),
                ('time', models.TimeField()),
                ('notify_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.NotifyStudent')),
            ],
        ),
        migrations.CreateModel(
            name='PlacementStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation', models.CharField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending')], default='PENDING', max_length=20)),
                ('placed', models.CharField(choices=[('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('PENDING', 'Pending')], default='PENDING', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('notify_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.NotifyStudent')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=40)),
                ('project_status', models.CharField(choices=[('ONGOING', 'Ongoing'), ('COMPLETED', 'Completed')], default='COMPLETED', max_length=20)),
                ('summary', models.CharField(default='', max_length=500)),
                ('project_link', models.CharField(default='', max_length=200)),
                ('sdate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('edate', models.DateField(blank=True, null=True)),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_title', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=250)),
                ('publisher', models.CharField(default='', max_length=250)),
                ('publication_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPlacement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debar', models.CharField(choices=[('DEBAR', 'Debar'), ('NOT DEBAR', 'Not Debar')], default='NOT DEBAR', max_length=20)),
                ('future_aspect', models.CharField(choices=[('PLACEMENT', 'Placement'), ('PBI', 'PBI'), ('HIGHER STUDIES', 'Higher Studies'), ('OTHER', 'Other')], default='PLACEMENT', max_length=20)),
                ('placed_type', models.CharField(choices=[('ON CAMPUS', 'On Campus'), ('PPO', 'PPO'), ('OFF CAMPUS', 'Off Campus')], default='PLACEMENT', max_length=20)),
                ('placement_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('package', models.DecimalField(decimal_places='2', default='0.0', max_digits='5')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.PlacementRecord')),
                ('unique_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='know',
            name='language_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.Language'),
        ),
        migrations.AddField(
            model_name='know',
            name='unique_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='has',
            name='skill_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.Skill'),
        ),
        migrations.AddField(
            model_name='has',
            name='unique_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coinventor',
            name='publication_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.Publication'),
        ),
        migrations.AddField(
            model_name='coauthor',
            name='publication_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='placement_cell.Publication'),
        ),
        migrations.AlterUniqueTogether(
            name='studentrecord',
            unique_together=set([('record_id', 'unique_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='placementstatus',
            unique_together=set([('notify_id', 'unique_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='know',
            unique_together=set([('language_id', 'unique_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='has',
            unique_together=set([('skill_id', 'unique_id')]),
        ),
    ]
