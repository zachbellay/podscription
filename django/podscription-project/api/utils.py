import random
import string

from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


# def unique_slug_generator(instance, slug_attr, new_slug = None):
#     if new_slug is not None:
#         slug = new_slug
#     else:
#         slug = slugify(getattr(instance, slug_attr))
#     Klass = instance.__class__
#     qs_exists = Klass.objects.filter(slug = slug).exists()
#     if qs_exists:
#         new_slug = "{slug}-{randstr}".format(
#             slug = slug, randstr = random_string_generator(size = 4))

#         return unique_slug_generator(instance, slug_attr, new_slug = new_slug)
#     return slug


def unique_slug_generator(instance, slug_attr, filter_args=None, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(getattr(instance, slug_attr))
    Klass = instance.__class__

    if filter_args is None:
        qs_exists = Klass.objects.filter(slug=slug).exists()
    else:
        qs_exists = Klass.objects.filter(slug=slug, **filter_args).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4)
        )

        return unique_slug_generator(
            instance, slug_attr, filter_args=filter_args, new_slug=new_slug
        )
    return slug
