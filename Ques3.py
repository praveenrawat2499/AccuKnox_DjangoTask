# Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Answer : Yes, by default, Django signals run in the same database transaction as the caller. When a signal like post_save is triggered, it executes within the same database transaction as the operation that triggered it. If the database transaction fails or is rolled back, the changes made in the signal handler will also be rolled back.

# To demonstrate this, let's use a post_save signal and raise an exception in the signal handler to cause the transaction to fail. We can then check if the changes to the database are rolled back.

# myapp/models.py

from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

# Simple model definition
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver to handle post_save
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Inside signal receiver, raising an exception to simulate an error.")
    # Simulate an error by raising an exception
    raise Exception("Simulated error to cause transaction rollback")

# Running this code to test if the transaction is rolled back
if __name__ == "__main__":
    import django
    import os

    # Set up Django environment
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    django.setup()

    # Try to create a new instance of MyModel inside a transaction block
    try:
        with transaction.atomic():
            print("Attempting to create a model instance...")
            MyModel.objects.create(name="Test Instance")
            print("Model instance created.")
    except Exception as e:
        print(f"Exception occurred: {e}")

    # Check if the model instance was actually saved in the database
    instance_exists = MyModel.objects.filter(name="Test Instance").exists()
    print(f"Was the instance saved to the database? {'Yes' if instance_exists else 'No'}")



# The output of the model instance will not saved due to the exception raised in the signal handler, proving that Django signals run in the same database transaction as the caller by default. Isf any exception occurs, the transaction is rolled back.