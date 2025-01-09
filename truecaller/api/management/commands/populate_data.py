from django.core.management.base import BaseCommand
from api.models import User, Contact
from faker import Faker

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                phone_number=fake.phone_number(),
                password='password123'
            )
            for _ in range(5):
                Contact.objects.create(
                    user=user,
                    name=fake.name(),
                    phone_number=fake.phone_number(),
                    is_spam=fake.boolean()
                )
        self.stdout.write(self.style.SUCCESS('Successfully populated the database'))