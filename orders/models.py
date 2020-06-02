from django.db import models

# Create your models here.

def listMods(items):
    mods_str = " with "
    for item in items:
        mods_str = mods_str + item.name + ", "
    mods_str = mods_str[:-2]
    return mods_str

class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    street_address = models.CharField(max_length=128)
    zipcode = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PizzaBase(models.Model):
    SIZE_CHOICES = [
        ("SM", "Small"),
        ("LG", "Large"),
    ]
    STYLE_CHOICES = [
        ("SIC", "Sicilian"),
        ("REG", "Regular"),
    ]
    TOPPINGS_CHOICES = [
        (0, "Cheese"),
        (1, "One"),
        (2, "Two"),
        (3, "Three"),
        (4, "Special"),
    ]

    style = models.CharField(max_length=3, choices=STYLE_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    toppings_num = models.IntegerField(choices=TOPPINGS_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        toppings_str = ""
        if self.toppings_num == 0:
            toppings_str = "cheese"
        elif self.toppings_num > 3:
            toppings_str = "specialty"
        else:
            toppings_str = f"{self.toppings_num} topping"
        return f"{self.size} {self.style} {toppings_str} pizza: ${self.price}"

class Toppings(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class PizzaOrder(models.Model):
    base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE, related_name="base")
    toppings = models.ManyToManyField(Toppings, blank=True, related_name="pizza")

    def __str__(self):
        toppings_str = ""
        if self.toppings.count() > 0:
            toppings_str = listMods(self.toppings.all())
        return f"{self.base}{toppings_str}"

class SubModifications(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.name

class NotPizzaBase(models.Model):
    SIZE_CHOICES =[
        ("SM", "Small"),
        ("LG", "Large"),
        ("NA", "Not Applicable"),
    ]
    GROUP_CHOICES = [
        ("SUB","Sub Sandwich"),
        ("PST", "Pasta"),
        ("SLD", "Salad"),
        ("DPL", "Dinner Platter"),
    ]
    name = models.CharField(max_length=32)
    group = models.CharField(max_length=3, choices=GROUP_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.size if self.size != 'NA' else ''} {self.name} {self.group}"

class NotPizzaOrder(models.Model):
    base = models.ForeignKey(NotPizzaBase, on_delete=models.CASCADE, related_name="base")
    sandwich_mod = models.ManyToManyField(SubModifications, blank=True, related_name="sub")

    def __str__(self):
        mods_str = ""
        if self.sandwich_mod.count() > 0:
            mods_str = listMods(self.sandwich_mod.all())
        return f"{self.base}{mods_str}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customer")
    time = models.DateTimeField()
    pizza = models.ManyToManyField(PizzaOrder, blank=True, related_name="order")
    not_pizza = models.ManyToManyField(NotPizzaOrder, blank=True, related_name="order")

    def __str__(self):
        return f"{self.customer} at {self.time}"