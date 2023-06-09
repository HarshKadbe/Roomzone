# Generated by Django 3.2.18 on 2023-04-20 18:47

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=500, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('password1', models.CharField(blank=True, max_length=200, null=True)),
                ('password2', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ListProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('Rent', models.IntegerField(blank=True, null=True)),
                ('security_deposit', models.IntegerField(blank=True, null=True)),
                ('bachelers_allowed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=100)),
                ('independent', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('by', models.CharField(choices=[('owner', 'owner'), ('broker', 'broker')], default='owner', max_length=100)),
                ('property_location', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_detail', models.IntegerField()),
                ('description', models.TextField()),
                ('is_featured', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=200, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.category')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='projects.profile')),
            ],
        ),
    ]
