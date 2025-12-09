# Generated manually
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_quote_delete_quoterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(choices=[('front-lit', 'Front-Lit Channel Letters'), ('back-lit', 'Back-Lit / Halo-Lit'), ('front-back-lit', 'Front + Back-Lit'), ('open-face', 'Open-Face / Marquee'), ('non-illuminated', 'Non-Illuminated 3D'), ('rgb-programmable', 'RGB / Programmable'), ('neon', 'Neon Signs'), ('lightbox', 'Light Boxes'), ('logo', 'Logo Signs'), ('other', 'Other')], default='other', max_length=50),
        ),
    ]
