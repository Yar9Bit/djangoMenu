from django.db import models


class Menu(models.Model):
    menu_name = models.CharField(max_length=16)

    def __str__(self):
        return self.menu_name


class MenuItem(models.Model):
    visible = models.BooleanField(default=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    uri = models.SlugField(
        verbose_name='URL',
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return self.uri

    def __str__(self):
        return self.name
