from sys import path
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import xml.etree.ElementTree as ET

def get_new_value(tag,value,newSize,oldSize):
  if tag[0]=="x":  
    return int(newSize[0]*value/oldSize[0])
  else:
    return int(newSize[1]*value/oldSize[1])

def change_the_value(root_element, tag, new_size,width,height):
    old_size = (int(width),int(height))
    for elem in root_element.iter(tag):
        elem.text = str(get_new_value(tag,int(elem.text),new_size,old_size))

def start(path_xml_old,path_xml_new,new_size):
  new_size_tup = tuple(int(a) for a in new_size.split(","))
  for i in os.listdir(path_xml_old):
      file = path_xml_old + "/" + i
      xmldata=ET.parse(file)
      root_element= xmldata.getroot()
      height = root_element.find("size")[1].text
      width = root_element.find("size")[0].text
      for tag in ["xmin","xmax","ymin","ymax"]:
          change_the_value(root_element,tag,new_size_tup,width,height)
      root_element.find("size")[1].text = str(new_size_tup[1])  #height y
      root_element.find("size")[0].text = str(new_size_tup[0])  #width x
      xmldata.write(path_xml_new + "/"+ i)