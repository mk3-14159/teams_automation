#!/usr/bin/python3 
import pyautogui
import time 
import sys
import os 

# keep getting position
def get_relative_position():
  print("test block")

# clicker on this position Point(x=374, y=576)
def get_display_position():
  current = pyautogui.position()
  print(current)

def countdown(time_sec):
    print("staring countdown ...")
    while time_sec:  
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("starting click")

# Point(x=254, y=463)
# identify button coordinate and define the click time 
def click(times):
    for i in range(times):
      # clicked = pyautogui.click(button='left', x=254, y=463)
      pyautogui.click(button='left', x=254, y=463)
      position = pyautogui.position()
      #print(clicked) # returns none for some reason
      print("%s coordinate clicked on %s times!" %(position, i))

def check_text():
  print("testing the check text")

if __name__ == "__main__":
  #get_display_position()
  countdown(3)
  click(20)
  #get_display_position()