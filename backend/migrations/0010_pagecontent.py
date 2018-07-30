# Generated by Django 2.0.6 on 2018-07-30 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_add_page_name_choices_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(choices=[(('HOME',), 'Home'), ('RESUME', 'Title'), ('PROJECTS', 'Projects')], max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=65535)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_header', to='backend.Image')),
            ],
        ),
        migrations.RemoveField(
            model_name='pagecontent',
            name='page_name',
        ),
        migrations.RemoveField(
            model_name='pagecontent',
            name='type',
        ),
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.ManyToManyField(related_name='page', to='backend.PageContent'),
        ),
        migrations.AddField(
            model_name='page',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page', to='backend.PageHeader'),
        ),
    ]