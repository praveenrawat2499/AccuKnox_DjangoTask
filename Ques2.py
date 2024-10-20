# Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

# Answer : Yes, Django signals run in the same thread as the caller by default. This means that the signal handler will execute in the same thread in which the signal was sent. We can demonstrate this behavior by checking the thread identity when a signal is triggered.

# Here is the code. We'll set up a signal receiver and print the thread information from both the caller and the signal receiver to see if they match.

import threading
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Example model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    print("Inside signal receiver.")
    print(f"Signal thread: {threading.current_thread().name}")

# Code to create an instance of MyModel
if __name__ == "__main__":
    print(f"Main thread: {threading.current_thread().name}")
    my_instance = MyModel.objects.create(name="Test Instance")



# The output will show that the thread name is the same in both the main program and the signal receiver, confirming that Django signals run in the same thread by default.
