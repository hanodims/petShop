# Generated by Django 3.1.1 on 2020-09-05 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
