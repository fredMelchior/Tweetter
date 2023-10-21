from django.db import models
from django.contrib.auth import get_user_model

# from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    # avatar = models.ImageField(
    #     blank=True, default="default.jpg", upload_to="profile_images", editable=True
    # )
    # background = models.ImageField(
    #     blank=True, default="defaultbg.jpg", upload_to="profile_images", editable=True
    # )
    bio = models.TextField(
        blank=True, default="I'm using Tweeter!", max_length=360, editable=True
    )

    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.avatar.path)
    #     if img.height > 150 or img.width > 150:
    #         output_size = (150, 150)

    #     if img.mode != "RGB":
    #         img = img.convert("RGB")

    #         img.thumbnail(output_size)
    #         img.save(self.avatar.path)

    #     img = Image.open(self.background.path)
    #     if img.height > 320 or img.width > 920:
    #         output_size = (320, 920)

    #     if img.mode != "RGB":
    #         img = img.convert("RGB")

    #         img.thumbnail(output_size)
    #         img.save(self.background.path)
