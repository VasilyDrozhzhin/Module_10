import threading
import  time

def write_words(word_count, file_name):
	with open(file_name, "w", encoding="utf-8") as file:
		for i in range(word_count):
			file.write(f'Какой-то текст №{i}')
			time.sleep(0.1)
	print(f'Завершилась запись в файл {file_name}')

t1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
t2 = time.time()
t3 = t2 - t1
print(f'Время работы функций составило: {t3:.2f} секунд')
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
t4 = time.time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
t5 = time.time()
t6 = t5 - t4
print(f'Время работы потоков составило: {t6:.2f} секунд')

