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

With help from an alumni at Code Institute, I was able to fix the relevant parts of this code to the following:

```
MEMBERSHIP_CHOICES = (
    ('Gold', 'Gold Level'),
    ('Silver', 'Silver Level'),
    ('Bronze', 'Bronze Level')
)


class Membership(models.Model):
    """ Class for memberships """
    membership_level = models.CharField(
        max_length=6,
        choices=MEMBERSHIP_CHOICES,
        default='Bronze',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.membership_level
```

The choices variable was moved to outside the class, and the __str__ function was edited not to return name, but the membership_level constructed.