# Generated by Django 3.1.4 on 2020-12-20 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RanaFurniture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_image', models.ImageField(upload_to='images')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
