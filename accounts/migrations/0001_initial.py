# Generated by Django 5.2 on 2025-04-17 23:51

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('role', models.CharField(choices=[('NGO', 'NGO'), ('LAWYER', 'Lawyer'), ('DONOR', 'Donor'), ('ADMIN', 'Admin')], max_length=10)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('verification_code', models.CharField(blank=True, max_length=6, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DonorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(max_length=255)),
                ('allow_anonymous', models.BooleanField(default=False)),
                ('preferred_causes', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='donor_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LawyerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('license_number', models.CharField(max_length=100)),
                ('specialization', models.CharField(max_length=255)),
                ('experience_years', models.PositiveIntegerField()),
                ('education', models.TextField()),
                ('bio', models.TextField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='lawyer_profiles/')),
                ('verification_documents', models.FileField(blank=True, null=True, upload_to='lawyer_verification/')),
                ('is_verified', models.BooleanField(default=False)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lawyer_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NGOProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('address', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='ngo_logos/')),
                ('verification_documents', models.FileField(blank=True, null=True, upload_to='ngo_verification/')),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ngo_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
