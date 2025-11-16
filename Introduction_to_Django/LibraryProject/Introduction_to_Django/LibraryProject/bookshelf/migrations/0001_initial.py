from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                migrations.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
                migrations.CharField(max_length=200),
                migrations.CharField(max_length=100),
                migrations.IntegerField(),
            ],
        ),
    ]
