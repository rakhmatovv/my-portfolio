from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Category name, e.g., Technology")
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="Tag name, e.g., Django")
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('disabled', 'Disabled')
    )
    title = models.CharField(max_length=200, help_text="Title of the blog post")
    content = HTMLField(help_text="Content of the blog post")
    image = models.ImageField(upload_to="blog/image", help_text="Upload your blog post image")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="blog_posts",
        null=True,
        blank=True,
    )
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogs", blank=True)
    tags = models.ManyToManyField(Tag, related_name="blogs", blank=True)
    comments_count = models.PositiveIntegerField(default=0, editable=False, help_text="Number of comments")
    share_count = models.PositiveIntegerField(default=0, editable=False, help_text='Number of shares')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', help_text='Status of the blog post')

    def update_comment_count(self):
        """Обновление количества комментариев"""
        self.comments_count = self.comments.count()
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Модель комментариев"""
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100, help_text='Name of the comment')
    email = models.EmailField(help_text='Email of the comment')
    message = HTMLField(help_text='Message of the comment')
    create_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Обновление счетчика комментариев после сохранения"""
        super().save(*args, **kwargs)
        self.blog.update_comment_count()

    def __str__(self):
        return f'Comment by {self.name} on {self.blog.title}'
