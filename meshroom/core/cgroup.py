#!/usr/bin/env python
# coding:utf-8

import os

#Try to retrieve limits of memory for the current process' cgroup
def getCgroupMemorySize():

    #first of all, get pid of process
    pid = os.getpid()

    #Get cgroup associated with pid
    filename = f"/proc/{pid}/cgroup"

    cgroup = None
    try:
        with open(filename, "r") as f :

            #cgroup file is a ':' separated table
            #lookup a line where the second field is "memory"
            lines = f.readlines()
            for line in lines:
                tokens = line.rstrip("\r\n").split(":")
                if len(tokens) < 3:
                    continue
                if tokens[1] == "memory":
                    cgroup = tokens[2]
    except IOError:
        pass

    if cgroup is None:
        return -1

    size = -1
    filename = f"/sys/fs/cgroup/memory/{cgroup}/memory.limit_in_bytes"
    try:
        with open(filename, "r") as f :
            value = f.read().rstrip("\r\n")
            if value.isnumeric():
                size = int(value)
    except IOError:
        pass

    return size

def parseNumericList(str):

    nList = []
    for item in str.split(','):
        if '-' in item:
            start, end = item.split('-')
            start = int(start)
            end = int(end)
            nList.extend(range(start, end + 1))
        else:
            value = int(item)
            nList.append(value)

    return nList

#Try to retrieve limits of cores for the current process' cgroup
def getCgroupCpuCount():

    #first of all, get pid of process
    pid = os.getpid()

    #Get cgroup associated with pid
    filename = f"/proc/{pid}/cgroup"

    cgroup = None
    try:
        with open(filename, "r") as f :

            #cgroup file is a ':' separated table
            #lookup a line where the second field is "memory"
            lines = f.readlines()
            for line in lines:
                tokens = line.rstrip("\r\n").split(":")
                if len(tokens) < 3:
                    continue
                if tokens[1] == "cpuset":
                    cgroup = tokens[2]
    except IOError:
        pass

    if cgroup is None:
        return -1

    size = -1
    filename = f"/sys/fs/cgroup/cpuset/{cgroup}/cpuset.cpus"
    try:
        with open(filename, "r") as f :
            value = f.read().rstrip("\r\n")
            nlist = parseNumericList(value)
            size = len(nlist)

    except IOError:
        pass

    return size

