# Generated migration for changing ImageField to CharField
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casestudy', '0003_alter_casestudy_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casestudy',
            name='casestudyimage',
            field=models.CharField(
                blank=True, 
                help_text="Filename of the image in static/images/ directory (e.g., 'floating-roof.png')", 
                max_length=200, 
                null=True
            ),
        ),
    ]
