# An animal shelter holds only dogs and cats, and operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest" (based on
# arrival time) of all animals at the shelter, or they can select whether they
# would prefer a dog or a cat (and will receive the oldest animal of that type).
# They cannot select which specific animal they would like. Create the data
# structures to maintain this system and implement operations such as enqueue,
# dequeueAny, dequeueDog and dequeueCat. You may use built-in LinkedList data
# structure.

# Since the shelter holds only two types of animals, two separate queues will
# be maintained. If the shelter were to hold a few more, then one queue with
# a pointer for the oldest of each animal type would be considered.

import unittest
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

s = Shelter()
s.enqueue(Dog, "Max", 5)
s.enqueue(Cat, "Sushi", 2)
s.enqueue(Dog, "Hiro", 9)
s.enqueue(Cat, "Jester", 3)
s.enqueue(Cat, "Coal", 4)
s.enqueue(Dog, "Hannibal", 7)


class ShelterTest(unittest.TestCase):

  def test_shelter(self):
    resident = s.dequeue_any()
    self.assertEqual(resident.animal.name, "Max")

    resident = s.dequeue_dog()
    self.assertEqual(resident.animal.name, "Hiro")

    resident = s.dequeue_any()
    resident = s.dequeue_any()
    self.assertEqual(resident.animal.name, "Jester")
    self.assertEqual(s.count(), 2)

    resident = s.dequeue_any()
    self.assertEqual(resident.animal.name, "Coal")
    
    resident = s.dequeue_any()
    self.assertEqual(resident.animal.name, "Hannibal")

    
if __name__ == '__main__':
  unittest.main()



