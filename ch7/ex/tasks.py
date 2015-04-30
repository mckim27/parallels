# -*- coding: utf-8 -*-

from math import sqrt
from celery import Celery
import logging
import re
import requests

html_link_regex = re.compile(
 '<a\s(?:.*?\s)*?href=[\'"](.*?)[\'"].*?>')

app = Celery('tasks', broker='redis://127.0.0.1:6379/0', backend='redis://127.0.0.1:6379/0')
#app.config.CELERY_RESULT_BACKEND = 'redis://192.168.0.6:6379/0'

@app.task
def sqrt_task(value):
  return sqrt(value)

@app.task
def fibo_task(value):
  a, b = 0,1
  for item in range(value):
    a, b = b, a + b
  message = "The Fibonacci calculated with task id %s was %d" % (fibo_task.request.id, a)
  print message
  return (value, message)

@app.task
def crawl_task(url):
  request_data = requests.get(url)
  links = html_link_regex.findall(request_data.text)
  message = "The task %s found the following links %s.." % (url, links)
  print message
  return message
