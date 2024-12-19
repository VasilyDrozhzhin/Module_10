import multiprocessing
import time


def read_info(name):
	all_data = []
	with open(name, "r", encoding="utf-8") as file:
		for line in file:
			all_data.append(line)

file_names = [f'./file {number}.txt' for number in range(1, 5)]
t1 = time.time()
for name in file_names:
	read_info(name)
t2 = time.time()
t3 = t2 - t1
print(f'Время линейного выполнения составило: {t3}')
t4 = time.time()
# with multiprocessing.Pool() as pool:
# 	pool.map(read_info, file_names)
t5 = time.time()
t6 = t5 - t4
print(f'Время многопроцессного выполнения составило: {t6}')
