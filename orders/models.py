from django.db import models
from members.models import User


class Order(models.Model):
    time_placed = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(User, related_name='user_order', on_delete=models.CASCADE)
    requested_coach = models.ForeignKey(User, related_name='requested_coach', on_delete=models.CASCADE) # Customer inputs what coach they want. If customer does not input anything, set to 'Any'
    order_notes = models.TextField(max_length=240)                                                      # Small notes from customer that they want the coach to read before reaching out to them.


    def __str__(self):
        return f'Customer {self.customer.username} requested {self.requested_coach} as their coach.'