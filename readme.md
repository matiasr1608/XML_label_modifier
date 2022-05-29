# XML label modifier

While labeling images to train an object recognition model, I encounter a problem. I did not realize that the images had all different sizes and it was needed to be all of the same size, and after re-sizing all the images I did not want to label all of them again, so that why I made this simple script.

## What it does?
It takes a path to a folder containging the old XML files with the labeles for each image, a path to save the edited XML files and the new size of the images. It calcultes the relation of each corner of the labels in the new size taking into account the old size, so it changes the coordinates of the label box.

## How to use it?
You can download the zip and unzip it or clone the repository:

```
$ git clone https://github.com/matiasr1608/XML_label_modifier
```

Then, execute the start.py that should open a pop up to select the required inputs or:
```
$ python3 start.py 
```
