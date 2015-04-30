# -*- coding: utf-8 -*-

import logging
import time
from tasks import *

logging.basicConfig(level=logging.DEBUG)

input_list = [3, 4, 6, 8, 10, 12, 16, 20]
url_list = ['http://www.google.com',
            'http://br.bing.com',
            'http://duckduckgo.com',
            'http://github.com',
            'http://br.search.yahoo.com']

def manage_sqrt_task(value):
  result = app.send_task('tasks.sqrt_task', args=(value,),
                   queue='sqrt_queue', routing_key='sqrt_queue')
  logging.info(result.get())


def manage_fibo_task(value_list):
  async_result_dict = {x: app.send_task('tasks.fibo_task', args=(x,), queue='fibo_queue', 
                            routing_key='fibo_queue') for x in value_list}
  time.sleep(2)
  for key, value in async_result_dict.items():
    if value.ready():
      logging.info("Value [%d] -> %s" % (key,  value.get()[1]))
    else:
      logging.info("Task [%s] is not ready" % value.task_id)


def manage_crawl_task(url_list):
  async_result_dict = {url: app.send_task('tasks.crawl_task', args=(url,), queue='webcrawler_queue',
                              routing_key='webcrawler_queue') for url in url_list}
  time.sleep(4)
  for key, value in async_result_dict.items():
    if value.ready():
      logging.info("%s -> %s" % (key, value.get()))
    else:
      logging.info("The task [%s] is not ready" % value.task_id)


if __name__ == '__main__':
  #manage_sqrt_task(4)
  manage_fibo_task(input_list)
  #manage_crawl_task(url_list)
