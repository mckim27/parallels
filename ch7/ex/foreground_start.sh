#!/bin/bash

celery worker -A tasks -Q sqrt_queue,fibo_queue,webcrawler_queue -l info -c 4
