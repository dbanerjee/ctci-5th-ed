# Solution to Exercise 3.7 from Cracking the Coding Interview, 5th Edition
# Nitin Punjabi
# nptoronto@yahoo.com
# https://github.com/nitinpunjabi

import time
import queue as q

class Animal:

  def __init__(self, name, age):
    self.name = name
    self.age = age


class Dog(Animal):

  def __init__(self, name, age):
    Animal.__init__(self, name, age)


class Cat(Animal):

  def __init__(self, name, age):
    Animal.__init__(self, name, age)


class Resident:

  def __init__(self, animal_type, name, age):
    self.animal = animal_type(name, age)
    self.entry_time = time.time()


class Shelter:
  
  def __init__(self)  :
    self.dogs = q.Queue()
    self.cats = q.Queue()
    self.animal_count = 0

  def enqueue(self, animal_type, name, age):
    resident = Resident(animal_type, name, age)

    if isinstance(resident.animal, Dog):
      self.dogs.enqueue(resident)
    elif isinstance(resident.animal, Cat):
      self.cats.enqueue(resident)
    else:
      raise Exception("Unknown animal type")

    self.animal_count += 1

  def dequeue_any(self):
    if self.animal_count is 0:
      return None

    self.animal_count -= 1

    oldest_dog = self.dogs.peek()
    if oldest_dog is None:
      return self.cats.dequeue()

    oldest_cat = self.cats.peek()
    if oldest_cat is None:
      return self.dogs.dequeue()

    if oldest_dog.entry_time < oldest_cat.entry_time:
      return self.dogs.dequeue()
    else:
      return self.cats.dequeue()

  def dequeue_dog(self):
    if self.dogs.peek():
      self.animal_count -= 1
      return self.dogs.dequeue()

  def dequeue_cat(self):
    if self.cats.peek():
      self.animal_count -= 1
      return self.cats.dequeue()

  def count(self):
    return self.animal_count



