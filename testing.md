# Testing

Here I will document the testing processes and bugs I encountered during the production of this project

# Bugs

## Membership Level Bug

While working on my first model, I encountered a bug whereby the model for selecting the different levels of membership did not properly show itself in the site admin. Instead, this was what was visible:

![Image of bare membership level admin page](assets/bugs/membershiplevelbug.png)

My code for this section looked like this:

```
class MembershipLevel(models.Model):
    """Defines the level of a member's subscription"""
    GOLD = 'GO'
    SILVER = 'SI'
    BRONZE = 'BR'
    MEMBERSHIP_CHOICES = [
        (GOLD, 'Gold Level'),
        (SILVER, 'Silver Level'),
        (BRONZE, 'Bronze Level'),
    ]

    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
```