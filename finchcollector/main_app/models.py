from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Bird(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('detail', kwargs={'bird_id': self.id})
    

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
      max_length=1,
      choices=MEALS,
      default=MEALS[0][0]
      )
  # Create a bird_id FK
  bird = models.ForeignKey(Bird, on_delete=models.CASCADE)
  #(if the bird is deleted, every feeding will be deleted)
  
  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_meal_display()} on {self.date}"