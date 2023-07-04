# Generated by Django 4.2.2 on 2023-07-04 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IELTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('candidate_id', models.IntegerField()),
                ('date', models.DateField()),
                ('last_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(choices=[('ayol', 'ayol'), ('erkak', 'erkak')], max_length=200)),
                ('rigion_address', models.CharField(max_length=200)),
                ('nationally', models.CharField(max_length=200)),
                ('first_language', models.CharField(max_length=200)),
                ('speaking', models.FloatField()),
                ('writeng', models.FloatField()),
                ('reading', models.FloatField()),
                ('listening', models.FloatField()),
                ('admission', models.TextField(blank=True, null=True)),
                ('test_number', models.IntegerField()),
                ('date_number', models.IntegerField()),
            ],
            options={
                'verbose_name': 'IELTS',
                'verbose_name_plural': 'IELTS',
            },
        ),
    ]