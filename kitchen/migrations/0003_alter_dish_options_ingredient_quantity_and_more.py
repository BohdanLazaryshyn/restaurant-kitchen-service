# Generated by Django 4.1.7 on 2023-03-28 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0002_alter_cook_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={
                "ordering": ["name"],
                "verbose_name": "dish",
                "verbose_name_plural": "dishes",
            },
        ),
        migrations.AddField(
            model_name="ingredient",
            name="quantity",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name="ingredient",
            name="unit",
            field=models.CharField(default="g", max_length=63),
        ),
        migrations.AlterField(
            model_name="dish",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]