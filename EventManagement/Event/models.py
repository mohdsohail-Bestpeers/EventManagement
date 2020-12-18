from django.db import models
from django.contrib.auth.models import User


LOCATION = (
    ("indore", "Indore"),
    ("ujjain", "Ujjain"),
    ("pune", "Pune"),
    ("mumbai", "Mumbai"),
    ("banglore", "Banglore"),
    ("other", "Other"),
)

SERVICE = (
    ("wedding", "Wedding"),
    ("birthday", "BirthDay"),
    ("stage_decoration", "Stage_Decoration"),
)

'''Handle the Event user details in database administrations'''
class EventUser(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()

    def __str__(self):
        return self.fname

'''Handle the Event fields details in database administrations'''
class Event(models.Model):
    event_user = models.ForeignKey(EventUser, on_delete=models.CASCADE)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)    #show created publisher from the administrations
    service = models.CharField(choices=SERVICE, default="birthday", max_length=50)
    Max_Guest = models.IntegerField(null=True, blank=True)
    start_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
    )
    end_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.TextField(blank=True)
    payment_status = models.CharField(max_length=20, default='pending')
    

    def __str__(self):
        return self.service

'''Handle the Address details in database administrations'''
class Address(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_address')
    city = models.CharField(choices=LOCATION, default="indore", max_length=50)
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    pincode = models.IntegerField()

'''image function to store the image in separate id folder'''
def image_path(instance, filename):
    instance_id = instance.event.id
    return "images/{}/{}".format(instance_id, filename)

'''Handle the photos with create or update date in database administrations'''
class event_photo(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="event_photos"
    )
    photo = models.ImageField(upload_to=image_path, max_length=255)
    create_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True, null=True)
