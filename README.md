# AutomateWithPython
Code to automate a few tasks with Python, saving manual effort with python scripts.

Tasks covered:
1. Copy folders recursively, and files from one location to another on your computer.
2. Delete old files from a folder

Scripts:
1. replaceDirs.py : Usage:
When two installations of a software are present, and you need to replace older packages or Release Units (RUs) from the earlier installation of a product with the newer RUs, use this script with two text files (old_RUs and new_RUs) containing the package names to replace in new_RU.txt and older package names to delete in old_RUs.txt.  Industry Use Case : Software products using TPCLs (Third Party Class Libraries) of different versions.


2. dir_labels_restructure.py : Usage:
When a number of files (eg. images of objects) are present with specific naming format, this script can collect files having similar labels by grouping them under specific labelled folders. Example use case : The CIFAR 10 Computer Vision dataset at http://pjreddie.com/media/files/cifar.tgz  .
