# Generated manually for shop app

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('design_file', models.FileField(blank=True, null=True, upload_to='quotes/%Y/%m/%d/')),
                ('design_description', models.TextField()),
                ('services', models.CharField(help_text='Selected services', max_length=255)),
                ('start_time', models.CharField(choices=[('immediate', 'Immediate'), ('1-2weeks', '1-2 Weeks'), ('1month', '1 Month'), ('more_than_1_month', 'More than 1 Month')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
            ],
        ),

    ]
