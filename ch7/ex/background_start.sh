#!/bin/bash
celery multi start 2 -A tasks -Q sqrt_queue,fibo_queue,webcrawler_queue -l info -c 1
