# Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Answer : By default, Django signals are executed synchronously. This means that when a signal is sent, the connected receiver functions are executed immediately, and the program will wait for these functions to finish before continuing.

# To demonstrate this, let me show you a code snippet where we use Django signals to prove this behavior. In this example, I'll set up a simple model and connect a signal to the post_save event to see when the receiver function is executed.

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time

# Example model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Signal received, processing...")
    # Simulate a time-consuming task
    time.sleep(5)
    print("Signal processing complete.")

# Code to create an instance of MyModel
if __name__ == "__main__":
    # Create a new instance of MyModel
    print("Creating model instance...")
    my_instance = MyModel.objects.create(name="Test Instance")
    print("Model instance created.")

# If the signals were executed asynchronously, "Model instance created." would appear before "Signal processing complete." But since they are executed synchronously by default, the order confirms that the receiver runs in a blocking manner.
