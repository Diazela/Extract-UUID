# Extract-UUID

## Description

As the title say, this is a basic script to extract all UUID from a given file.

## Install

Install the requirements.
```
pip3 install -r requirements.txt
```

## Usage

Start the tool.
```
python3 extuuid.py -f <Your File> -o <Output File>
```

## Specifications

Some type of file can contains a letter either before the UUID, like in the following that was extracted from ELF binary and where you can see "K":
```
K00075fb0-746b-6b74-b05f-0700075XXXXX
rtsp://service:FZ%21sc0Cam@172.19.16.110:554/mode=real&idc=1&ids=3
K7d49925b-4fc7-406b-a0ec-0046b80XXXXX
rtsp://service:FZ%21sc0Cam@172.19.16.210:554/mode=real&idc=1&ids=1
K92bf9572-cff4-44b0-aceb-732d39aXXXXX
rtsp://service:FZ%21sc0Cam@172.19.18.212:554/mode=real&idc=1&ids=1
```

At the line 11 in the script you can find `line.replace('K', '')` so you have to change this for your need.
