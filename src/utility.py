#!/usr/bin/python

from __future__ import division

def lambda_reverse_range(start=1, stop=0, step=-0.00001):
  if (stop>=start or step>=0):
    raise Exception("Invalid parameters. Requirements: Start>=Stop and Step<0")
   i = start
   while i > stop:
     i += step
     yield i
