from django.db import migrations, models
from django.utils.text import slugify

def generate_unique_slugs(apps, schema_editor):
    Post = apps.get_model('blog', 'Post')
    for post in Post.objects.all():
        original_slug = slugify(post.title)
        slug = original_slug
        counter = 1
        while Post.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{counter}"
            counter += 1
        post.slug = slug
        post.save()

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_created_at'),  # Previous migration
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='temp-slug', max_length=255),
        ),
        migrations.RunPython(generate_unique_slugs),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, max_length=255),
        ),
    ]
