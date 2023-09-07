# Extract-UUID

| As the title say, this is a basic script to extract all UUID from a given file.

<br>

**Install the requirements.**
```
pip3 install -r requirements.txt
```

<br>

**Usage**
```
python3 extuuid.py -f <Your File> -o <Output File>
```

<br>

**Specifications**

Your file could contains a letter before the UUID. 

Example: In the following that was extracted from ELF binary you can see "K":
```
K00075fb0-746b-6b74-b05f-0700075XXXXX
rtsp://service:FZ%21sc0Cam@172.19.16.110:554/mode=real&idc=1&ids=3
K7d49925b-4fc7-406b-a0ec-0046b80XXXXX
rtsp://service:FZ%21sc0Cam@172.19.16.210:554/mode=real&idc=1&ids=1
K92bf9572-cff4-44b0-aceb-732d39aXXXXX
rtsp://service:FZ%21sc0Cam@172.19.18.212:554/mode=real&idc=1&ids=1
```

<br>

At the line 11 in the script you can find :
```
line.replace('K', '')
```

> So you have to change this for your need.

<br>

This will give you a list of all UUID extracted - one by line. 

You can sort them and remove duplicate by using `sort` and `uniq` like the following:
```
sort <Output File> | uniq > <New Output File>
```
