from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    other_info = models.CharField(max_length=250, blank=True, default='')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):

    # Thanks to ramdog and Quintin Walker on Stack Overflow
    def validate_image(self):
        megabyte_limit = 1.0
        width_limit = 400
        height_limit = 300

        file_size = self.file.size
        (file_width, file_height) = get_image_dimensions(self)

        if file_size > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max image size is %sMB" % str(megabyte_limit))
        elif file_width > width_limit or file_height > height_limit:
            raise ValidationError("Max image dimensions are 400 x 300 pixels. "
                                  "Your image is {0} x {1} pixels.".format(file_width, file_height))

    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150, null=False, blank=False)
    history = models.CharField(max_length=1500, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    is_consignment = models.BooleanField(null=False, default=False)
    commission_percent = models.DecimalField(max_digits=2, decimal_places=2, default=.25)  # allows admin to change
    # normal commission percent of .25
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images', default='images/no_image.png', validators=[validate_image])
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)  # required for consignment item
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.title


class Size(models.Model):
    size = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.size




