# Generated by Django 5.1 on 2025-06-03 12:43

import common.mixins
import common.upload_to
import common.validators
import django.core.validators
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ru", "Россия"),
                            ("cn", "Китай"),
                            ("by", "Беларусь"),
                            ("vn", "Въетнам"),
                        ],
                        default="cn",
                        max_length=100,
                        null=True,
                        verbose_name="Страна",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=common.upload_to.dynamic_upload_to,
                        validators=[
                            common.validators.validate_image_extension_and_format
                        ],
                        verbose_name="Изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Бренд",
                "verbose_name_plural": "Бренды",
            },
            bases=(models.Model, common.mixins.WebpImageMixin),
        ),
        migrations.CreateModel(
            name="Cart",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
            ],
            options={
                "verbose_name": "Корзина",
                "verbose_name_plural": "Корзины",
            },
        ),
        migrations.CreateModel(
            name="CartItem",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(default=1, verbose_name="Количество"),
                ),
            ],
            options={
                "verbose_name": "Позиция в корзине",
                "verbose_name_plural": "Позиции в корзине",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        max_length=100,
                        null=True,
                        unique=True,
                        verbose_name="URL",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активна"),
                ),
                ("lft", models.PositiveIntegerField(editable=False)),
                ("rght", models.PositiveIntegerField(editable=False)),
                ("tree_id", models.PositiveIntegerField(db_index=True, editable=False)),
                ("level", models.PositiveIntegerField(editable=False)),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Discount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Скидка в %"
                    ),
                ),
                (
                    "start_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="Начало действия",
                    ),
                ),
                (
                    "end_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Окончание действия"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активна"),
                ),
            ],
            options={
                "verbose_name": "Скидка",
                "verbose_name_plural": "Скидки",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=common.upload_to.dynamic_upload_to,
                        validators=[
                            common.validators.validate_image_extension_and_format
                        ],
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, verbose_name="Цена"
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[("RUB", "RUB"), ("USD", "USD"), ("EUR", "EUR")],
                        default="RUB",
                        max_length=3,
                        verbose_name="Валюта",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="Активен"),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
            bases=(models.Model, common.mixins.WebpImageMixin),
        ),
        migrations.CreateModel(
            name="ProductImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to=common.upload_to.dynamic_upload_to,
                        validators=[
                            common.validators.validate_image_extension_and_format
                        ],
                        verbose_name="Изображение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Изображение товара",
                "verbose_name_plural": "Изображения товара",
            },
            bases=(models.Model, common.mixins.WebpImageMixin),
        ),
        migrations.CreateModel(
            name="ProductLike",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ip_address",
                    models.GenericIPAddressField(
                        blank=True, null=True, verbose_name="IP"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
            ],
            options={
                "verbose_name": "Лайк",
                "verbose_name_plural": "Лайки",
            },
        ),
        migrations.CreateModel(
            name="ProductReview",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                (
                    "rating",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProductVariant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("red", "Красный"),
                            ("green", "Зеленый"),
                            ("blue", "Синий"),
                            ("black", "Черный"),
                            ("white", "Белый"),
                            ("yellow", "Желтый"),
                            ("gray", "Серый"),
                            ("orange", "Оранжевый"),
                            ("pink", "Розовый"),
                            ("violet", "Фиолетовый"),
                            ("brown", "Коричневый"),
                            ("gold", "Золотой"),
                            ("silver", "Серебряный"),
                            ("beige", "Бежевый"),
                            ("multicolor", "Мультиколор"),
                            ("other", "Другой"),
                        ],
                        max_length=50,
                        verbose_name="Цвет",
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("xs", "XS"),
                            ("s", "S"),
                            ("m", "M"),
                            ("l", "L"),
                            ("xl", "XL"),
                            ("xxl", "XXL"),
                        ],
                        max_length=10,
                        verbose_name="Размер",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Количество на складе"
                    ),
                ),
            ],
            options={
                "verbose_name": "Вариант товара",
                "verbose_name_plural": "Варианты товара",
            },
        ),
        migrations.CreateModel(
            name="Favorite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Дата обновления"),
                ),
            ],
        ),
    ]
