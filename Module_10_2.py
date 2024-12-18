# https://github.com/VasilyDrozhzhin/Module_10/blob/main/Module_10_2.py
import threading
import time


class Knight(threading.Thread):
	def __init__(self, name, power):
		threading.Thread.__init__(self, name=name)
		self.power = power

	def run(self):
		print(f'{self.name}, на нас напали')
		num_enemis = 100
		count = 0
		while num_enemis > 0:
			num_enemis -= self.power
			time.sleep(1)
			count += 1
			print(f'{self.name} сражается {count} дней(дня), осталось {num_enemis} войнов\n')
		print(f'{self.name} одержал победу спустя {count} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы завершены')
