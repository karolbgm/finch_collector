from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird
# Add the following import
from django.http import HttpResponse

#FUNCTION BASED VIEWS
# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def birds_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  return render(request, 'birds/detail.html', { 'bird': bird })

#CLASS BASED VIEWS
class BirdCreate(CreateView):
  model = Bird
  fields = '__all__' #give me all the fields
# success_url = '/birds/'

class BirdUpdate(UpdateView):
  model = Bird
  fields = ['species', 'age']

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/'





  # Add the Bird class & list and view function below the imports
# class Bird:
#   def __init__(self, name, species, color, age):
#     self.name = name
#     self.species = species
#     self.color = color
#     self.age = age

# birds = [
#   Bird('Bluejay', 'Cyanocitta cristata', 'blue and white', 2),
#   Bird('Robin', 'Turdus migratorius', 'orange and gray', 1),
#   Bird('Parrot', 'Psittacidae', 'green and red', 5)
# ]


# def birds_index(request):
#   return render(request, 'birds/index.html', {'birds': birds})