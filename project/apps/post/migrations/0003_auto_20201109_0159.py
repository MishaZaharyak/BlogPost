# Generated by Django 3.0.10 on 2020-11-09 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcommentmodel',
            options={'ordering': ['-created_at'], 'verbose_name': 'Post Comment', 'verbose_name_plural': 'Posts Comments'},
        ),
    ]