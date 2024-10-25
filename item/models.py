# # # from django.db import models

# # # class Item(models.Model):
# # #     name = models.CharField(max_length=100)
# # #     price = models.DecimalField(max_digits=10, decimal_places=2)
# # #     image = models.ImageField(upload_to='images/', blank=True, null=True)  # Example definition

# # #     def __str__(self):
# # #         return self.name
# from django.db import models
# from django.contrib.auth.models import User  # Import the User model

# class Item(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='item_images/', blank=True, null=True)
#    # category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='items')  # Example of a category field
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Add this field if you want to track who created the item
#     description = models.TextField(blank=True, null=True)  # Optional description field
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255, default='Uncategorized')
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
    
#     def __str__(self):
#         return self.name
                        
# # from django.db import models
# # from django.contrib.auth.models import User  # Import the User model

# # class Item(models.Model):
# #     name = models.CharField(max_length=100)
# #     price = models.DecimalField(max_digits=10, decimal_places=2)
# #     image = models.ImageField(upload_to='item_images/', blank=True, null=True)
# #     created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this field
# #     description = models.TextField(blank=True, null=True)  # Optional description field

# #     def __str__(self):
# #         return self.name
