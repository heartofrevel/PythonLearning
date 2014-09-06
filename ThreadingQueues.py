#!/usr/bin/env python

import threading
import Queue
import time

class WorkerThread(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		print "In Worker Thread"
		while True:
			counter = self.queue.get()
			print "Ordered for sleep for %d seconds"%counter
			time.sleep(counter)
			print "finished sleeping for %d"%counter
			if(i%2==0):
				self.queue.task_done()

queue  = Queue.Queue()

for i in range(10):
	print "Creating Worker Thread : %d"%i
	worker = WorkerThread(queue)
	worker.setDaemon(True)
	worker.start()
	print "Worker Created %d"%i

for j in range(10):
	queue.put(j)

queue.join()

print "All tasks over"
