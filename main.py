"""I need a main method"""
import sys
import os
import time
import random
from PIL import  Image
from enum import Enum


def main():
   with Image.open ("./resources/img.png") as img:
      grayscale = img.convert("L")
      width, height = grayscale.size
      mean = 0
      for x in range(width):
         for y in range(height):
            mean += grayscale.getpixel((x,y))
      mean = mean / (width * height)
      for x in range(width):
         for y in range(height):
            if grayscale.getpixel((x,y)) > mean:
               grayscale.putpixel((x,y), 0)
            else:
               grayscale.putpixel((x,y), 1)
      number_of_characters_width = width // 8
      number_of_characters_height = height // 16
      if number_of_characters_width <= 1 & number_of_characters_height <= 1:
         print ("Image is too small")
      else:
         for y in range(number_of_characters_height):
            line = []
            for x in range(number_of_characters_width):
               values = [] 
               for i in range(8):
                  for j in range(16):
                     grayvalue = grayscale.getpixel((x*8+i,y*16+j))
                     values.append(str(grayvalue))
               line.append(get_character(values))
            treat_line(line)
   treat_missing_keys()

def treat_line(line):
   line_final = ""
   for char in line:
      line_final = line_final + char
   print(line_final)

def get_character(values):
   char_map_key = retrieve_char_map_key(values)
   max_percentage = 0.1
   max_percentage_char = " "
   for char in thisDict.keys():
      percentage = get_percentage(char_map_key, char)
      if(percentage > max_percentage):
         max_percentage = percentage
         max_percentage_char = thisDict[char]
   if max_percentage==0.7:
      if char_map_key not in thisMissingKeys.keys():
         thisMissingKeys[char_map_key] = 1
      else:
         thisMissingKeys[char_map_key] += 1
   return max_percentage_char

def get_percentage(char_map_key, char):
   percentage = 0
   """print(len(char_map_key))
   print(len(char))"""
   for i in range(len(char_map_key)):
      if char_map_key[i] == char[i]:
         percentage += 1
   return percentage / len(char_map_key)

def retrieve_char_map_key(values):
   returned = ""
   for key in values:
      returned = returned + key
   return returned

def treat_missing_keys():
   max_missing = 2
   missing_keys = []
   for key in thisMissingKeys.keys():
      if thisMissingKeys[key] > max_missing:
         max_missing = thisMissingKeys[key]
         missing_keys.append(key)
   print("max missing: " + str(max_missing))
   for key in missing_keys:
      print(key)


thisDict = {
  "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111": "█" ,
  "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000": " " ,
  "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110000001100000000000": "." ,
  "00011000000110000001100000011000000110000001100000011000000110000001100000011000000110000001100000011000000110000001100000011000": "|" ,
  "11000011110000110110011001100110001001000011110000011000000110000001100000011000001111000010010001100110011001101100001111000011": "X" ,
  "00000000000000000000000000000000000000000000000000000000111111111111111100000000000000000000000000000000000000000000000000000000": "-" ,
  "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001111111111111111": "_" ,
  "11111111111111110000001100000011000000110000001100000011000000110000001100000011000000110000001100000011000000111111111111111111": "]" ,
  "11111111111111111100000011000000110000001100000011000000110000001100000011000000110000001100000011000000110000001111111111111111": "[" ,
  "00011000000110000001100000011000000110000001100000011000000110000001100000011000000111111111111111111111111111110000001100000011": "A" ,
  "11111111111111110000001100000011000000110000001111111111111111111111111111111110000001100000011000000110000001111111111111111111": "B",
  "00011111111111110000001100000011000000110000001100000011000000110000001100000011000000110000001100000011000000110000001100000011": "C",
  "11111111111111110000001100000011000000110000001100000011000000110000001100000011000000110000001100000011000000111111111111111111": "D",
  "11111111111111111100000011000000110000001100000011111111111111111100000011000000110000001100000011000000110000001100000011000000": "F",
  "11000000110000001110000001100000011100000011000000111000000110000001100000011100000011000000111000000110000001110000001100000011": "\\",
  "00000011000000110000011100000110000011100000110000011100000110000001100000111000001100000111000001100000111000001100000011000000": "/",
  "00000000011111110000000001111111000000000111111100000000011111110000000001111111000000000111111100000000011111110000000001111111": "▒"
  }
"""
Imagin each character in the ascii table is represented as a 8x16 matrix of 1s and 0s representing the physichal character design (a 1 will count as a coloured area and the 0 a non-coloured area). in that example an empty space will be represented by 128 zeroes, and the dot character should be something like this "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000110000001100000000000", or  "11111111111111111100000011000000110000001100000011111111111111111100000011000000110000001100000011000000110000001100000011000000" represents the F character. Can you generate at least 20 examples for a few characters that are really different inside the dictionarym I especially need the parenthesis and \/ L@"*: characters?
"""

thisMissingKeys = {

}
   
   

main()