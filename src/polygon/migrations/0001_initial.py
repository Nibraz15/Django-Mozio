# Generated by Django 2.0.7 on 2019-07-29 00:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Polygons',
            fields=[
                ('polygon_id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=120)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Polygon', djgeojson.fields.PolygonField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]