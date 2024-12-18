import threading
import time
import queue
import random


class Table():
	def __init__(self, number):
		self.number = number
		self.guest = None


class Guest(threading.Thread):
	def __init__(self, name):
		super().__init__()
		self.name = name

	def run(self):
		time.sleep(random.randint(3, 10))


class Cafe():
	def __init__(self, *tables):
		self.queue = queue.Queue()
		self.tables = tables

	def guest_arrival(self, *guests):
		self.guests = guests
		for g in self.guests:
			empty_sit = False
			for i in self.tables:
				if i.guest == None:
					i.guest = g
					g.start()
					print(f'{g.name} сел(-а) за стол номер {i.number}')
					empty_sit = True
					break
			if empty_sit == False:
				self.queue.put(g)
				print(f'{g.name} в очереди')

	def discuss_guests(self):
		while self.queue.empty() == False and not all(t.guest is None for t in self.tables):
			for table in self.tables:
				if table.guest is not None and not table.guest.is_alive():
					print(f'{table.guest.name} покушал(-а) и ушёл(ушла).')
					print(f'Стол номер {table.number} свободен')
					table.guest = None
				if table.guest == None and not self.queue.empty():
					table.guest = self.queue.get()
					print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
					table.guest.start()


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
	'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
	'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
