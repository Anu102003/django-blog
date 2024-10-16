from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This commands inserts Category data"

    def handle(self, *args: Any, **options: Any):

        Category.objects.all().delete()
        
        categories=[
            'Sports','Technolgy','Media','Medical','Others'
        ]
        for category in categories:
            Category.objects.create(name=category)

        self.stdout.write(self.style.SUCCESS("Completed inserting Category Data!"))