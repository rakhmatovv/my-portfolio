from django.db import models
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
from django.utils.text import slugify


class CustomUser(AbstractUser):
    """'Custom user model""" ""

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"


class AboutMe(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    about_me = HTMLField(null=True, help_text="Write someting about yourself")
    image = models.ImageField(upload_to="about_me/image", blank=True, null=True)
    skills = models.ManyToManyField(to="Skill", blank=True, help_text="Add your skills")
    my_name = models.CharField(max_length=100, help_text="Enter your name")
    social_media = models.JSONField(
        null=True, blank=True, help_text="Add your social media links"
    )

    def __str__(self):
        return self.my_name


class Education(models.Model):
    """Education model"""

    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    start_year = models.CharField(max_length=4, help_text="Start year, e.g, 2022")
    end_year = models.CharField(max_length=4, help_text="End year, e.g, 2024")
    degree = models.CharField(
        max_length=100, help_text="Degree, e.g. , Bachelor of Science "
    )
    university = models.CharField(
        max_length=100, help_text="University, e.g. , University of Bukhara"
    )
    description = HTMLField(
        help_text="Description, e.g, Bachelor of Science in Computer Science"
    )

    def __str__(self):
        return (
            f"{self.degree} at {self.university} ({self.start_year}- {self.end_year})"
        )


class Experience(models.Model):
    """Experience model"""

    about_me = models.ForeignKey(AboutMe, on_delete=models.CASCADE)
    start_year = models.CharField(max_length=4, help_text="Start year, e.g, 2022")
    end_year = models.CharField(max_length=4, help_text="End year, e.g, 2024")
    position = models.CharField(
        max_length=100, help_text="Postionion, e.g. , Software engineer"
    )
    company = models.CharField(max_length=100, help_text="Company, e.g. , Monday labs")
    description = HTMLField(
        help_text="Description, e.g, Software Engineer at Monday labs"
    )

    def __str__(self):
        return f"{self.position} at {self.company} ({self.start_year}-{self.end_year})"


class Skill(models.Model):
    """Skill model"""

    name = models.CharField(
        max_length=100, unique=True, help_text="Enter your skill name"
    )
    procent = models.CharField(max_length=4, help_text="write % of skill")

    def __str__(self):
        return self.name


class Project(models.Model):
    """Project model"""

    title = models.CharField(max_length=100, help_text="Enter your project title")
    year = models.CharField(
        max_length=4, help_text="Enter the project year, e.g., 2024"
    )
    client = models.CharField(
        max_length=100, help_text="Enter the client name, e.g., Google"
    )
    service = models.CharField(
        max_length=100, help_text="Enter the service type, e.g., Web Design"
    )
    project_type = models.CharField(
        max_length=50, help_text="Enter the project type, e.g., Mobile App"
    )
    description = HTMLField(
        null=True, blank=True, help_text="Details about the project"
    )
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while Project.objects.filter(slug=slug).exists():
            slug = f'{base_slug}-{counter}'
            counter += 1
        self.slug = slug  # Перенесено сюда
    super().save(*args, **kwargs)


class ProjectImage(models.Model):
    """Project image model"""

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(
        upload_to="project/image", help_text="Upload your project image"
    )

    def __str__(self):
        return f"Image for {self.project.title}"


class YoutubeVideo(models.Model):
    """Youtube video model"""

    title = models.CharField(max_length=100, help_text="Enter your video title")
    link = models.URLField(help_text="Enter your video link")
    thumnail = models.ImageField(
        upload_to="image/youtube_thumbnail", help_text="Youtube video thumbnail"
    )
    create_at = models.DateTimeField(auto_now_add=True)
