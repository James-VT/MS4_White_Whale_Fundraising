# Testing

Here I will document the testing processes and bugs I encountered during the production of this project

## Donation form

### Passing information through to the database

Before linking Stripe to the project to take payments, I wanted to test that information was passing through properly to the database and that donation forms were being saved correctly. I had experienced a lot of problems building the form, so this was an important step.

I filled out the form with info:

![Image of form filled with info](assets/testing/donationformtesting/filledform1.png)

Then, upon clicking submit, I checked to see whether this had appeared in the database:

![Image of donation entry in database](assets/testing/donationformtesting/donationindatabase1.png)

Success! It had done so. As an aside, I had used a couple of print statements in the view as part of the bugfixing process and the results can be seen here:

![Image of the console prints](assets/testing/donationformtesting/consoleprintdonation1.png)

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

With help from an alumnus at Code Institute, I was able to fix the relevant parts of this code to the following:

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

The choices variable was moved to outside the class, and the __str__ function was edited not to return name, but the membership_level constructed. This fixed the issue. However, in the end I went with a different option so that admins could create new membership types as needed. This was done in order to future-proof the site against the evolving needs of the charity. Thus the choices field was removed, and replaced with a simple CharField.

---

## Donation form JavaScript bug

While building this project's donation form, I wanted to provide donors with a list of options for amounts they could donate, while also giving them the option to manually enter an amount. The pre-set donation amount options were selected via a radio menu, while the custom amount input was a text field. However, this posed a potential problem. Users needed to have the option to change their minds and donate a specific sum instead of a pre-set amount, but if they had selected a pre-set amount then, due to the nature of radio inputs, they could not uncheck a pre-set amount without selecting another pre-set amount. To get around this, I attempted to write a script that would uncheck any checked radio input when a user clicked inside the custom donation input field. I wrote it in a separate JS document and linked it in the ```{% block extra_js %}``` block near the top of the donation_form.html file. At first, I could not get this to work. The script I wrote looked like this:

```
var amountCustom = document.getElementById('amount-custom');

amountCustom.addEventListener("click", uncheckRadio);

function uncheckRadio() {
    var radio = document.querySelector('input[type=radio]:checked');
    radio.checked = false;
    }
```

It did not work. The error it flagged said that it could not read the property of null, citing the element with ID 'amount-custom' as null on the third line, when trying to add the event listener. To fix this, I first tried getting, and adding the event listener to, the outer div containing the text input, but the same problem occurred again. Then, remembering the different results I had encountered when loading my JavaScript at different positions in the HTML file while working on my Gloucestershire Battlefields project, I added the same script directly inline into the HTML file, at the very bottom. Lo and behold, this worked. The null error disappeared, and clicking inside the text input unchecked any checked radio input. As a result, I removed the inline script and moved my JavaScript file link into a new ```{% block postloadjs %}``` at the bottom of the file.

This worked nicely, apart from one small problem. A console error was logged if a user clicked inside the text input while no radio input was checked. The reason for this was that the first line of the function was trying to asign something to a variable every time the text input was clicked, but that thing - a checked radio input - did not exist if a user hadn't selected one. My solution to this was to wrap the function's inner workings inside an if statement. The result was this:

```
var amountCustom = document.getElementById('amount-custom');

amountCustom.addEventListener("click", uncheckRadio);

function uncheckRadio() {

    if (document.querySelector('input[type=radio]:checked')) {
        var radio = document.querySelector('input[type=radio]:checked');
        radio.checked = false;
    }
}
```

This works with no console errors. Success!

NOTE: All of this was later removed as crispy forms proved unsuitable to the task of pairing radio options' values with labels that were at once user-friendly and database-friendly. There was also an issue with the donation total field not accurately gathering user input from one or the other input field. As tutor support was unable to help with these issues, I was forced to take a different approach and use a drop-down menu for pre-set amounts instead. I leave this section here to demonstrate work done and learning; in the future I would like to revisit this project and have another go at implementing these things.

---

