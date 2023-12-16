# Lab 4

[Lab 4 Assignment]()

## 4. Filesystem and Memory

For the fourth exercise you have to use python3 as programming language

### 4.1. File Handle

Implement the following pseudocode-functions.

```
procedure write_to_file(filename):
    for i=0 to 25
        print_to_standard_out("Write Line: " + i + actual_timestamp())
        write_to_file(filename, “Write Line: ” + i + actual_timestamp())
        wait 1 second
procedure append_to_file(filename):
    for i=0 to 25
        print_to_standard_out("Append Line: " + i + actual_timestamp()))
        append_to_file(filename, “Append Line: ” + i + actual_timestamp())
        wait 1 second
procedure read_from_file(filename):
    for i=0 to number_of_rows(filename)
        print_to_standard_out(filename_row_number[i]))
        wait 1 second
procedure main()
    write_to_file(file1.txt):
    append_to_file(file2.txt):
    read_from_file (file1.txt):
    read_from_file (file2.txt):
```

Solution:

```python3 
#!/usr/bin/python3

import time
from datetime import datetime


def write_to_file(filename):
    """
    Writes lines to a file, each line containing a sequence number and a timestamp.

    Args:
    filename (str): The name of the file to write to.

    This function opens a file in write mode, which means it will overwrite the existing file
    if it already exists. It writes 26 lines to the file, each with a unique number and the
    current timestamp. There is a 1-second pause between each write.
    """
    with open(filename, 'w') as file:
        for i in range(26):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # looks like 2023-12-15 17:55:33
            line = f"Write Line: {i} {timestamp}\n"
            print(line.strip())
            file.write(line)
            time.sleep(1)  # Pause for 1 second between writes for demonstration purposes.


def append_to_file(filename):
    """
    Appends lines to a file, each line containing a sequence number and a timestamp.

    Args:
    filename (str): The name of the file to append to.

    This function opens a file in append mode. If the file does not exist, it gets created.
    It appends 26 lines to the file, each with a unique number and the current timestamp.
    There is a 1-second pause between each append.
    """
    with open(filename, 'a') as file:
        for i in range(26):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            line = f"Append Line: {i} {timestamp}\n"
            print(line.strip())
            file.write(line)
            time.sleep(1)


def read_from_file(filename):
    """
    Reads lines from a file and prints them to the console.

    Args:
    filename (str): The name of the file to read from.

    This function opens a file in read mode and reads all its lines into a list. It then
    iterates over the list, printing each line with its line number. There is a 1-second
    pause between printing each line.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            print(f"{i}: {line.strip()}")
            time.sleep(1)


def main():
    """
    Main function to demonstrate file operations.

    This function demonstrates writing to, appending to, and reading from files.
    It uses two files, 'file1.txt' and 'file2.txt', to showcase these operations.
    """
    write_to_file("file1.txt")
    append_to_file("file2.txt")
    read_from_file("file1.txt")
    read_from_file("file2.txt")
    exit(1)


if __name__ == "__main__":
    main()

```

Source: https://www.digitalocean.com/community/tutorials/how-to-handle-plain-text-files-in-python-3

#### What is the output of your implementation?

````bash
c2310475021@os-server:~/lab_4$ ./file_handle.py
Write Line: 0 2023-12-15 17:54:41
Write Line: 1 2023-12-15 17:54:42
Write Line: 2 2023-12-15 17:54:43
Write Line: 3 2023-12-15 17:54:44
Write Line: 4 2023-12-15 17:54:45
Write Line: 5 2023-12-15 17:54:46
Write Line: 6 2023-12-15 17:54:47
Write Line: 7 2023-12-15 17:54:48
Write Line: 8 2023-12-15 17:54:49
Write Line: 9 2023-12-15 17:54:50
Write Line: 10 2023-12-15 17:54:51
Write Line: 11 2023-12-15 17:54:52
Write Line: 12 2023-12-15 17:54:53
Write Line: 13 2023-12-15 17:54:54
Write Line: 14 2023-12-15 17:54:55
Write Line: 15 2023-12-15 17:54:56
Write Line: 16 2023-12-15 17:54:57
Write Line: 17 2023-12-15 17:54:58
Write Line: 18 2023-12-15 17:54:59
Write Line: 19 2023-12-15 17:55:00
Write Line: 20 2023-12-15 17:55:01
Write Line: 21 2023-12-15 17:55:02
Write Line: 22 2023-12-15 17:55:03
Write Line: 23 2023-12-15 17:55:04
Write Line: 24 2023-12-15 17:55:05
Write Line: 25 2023-12-15 17:55:06
Append Line: 0 2023-12-15 17:55:07
Append Line: 1 2023-12-15 17:55:08
Append Line: 2 2023-12-15 17:55:09
Append Line: 3 2023-12-15 17:55:10
Append Line: 4 2023-12-15 17:55:11
Append Line: 5 2023-12-15 17:55:12
Append Line: 6 2023-12-15 17:55:13
Append Line: 7 2023-12-15 17:55:14
Append Line: 8 2023-12-15 17:55:16
Append Line: 9 2023-12-15 17:55:17
Append Line: 10 2023-12-15 17:55:18
Append Line: 11 2023-12-15 17:55:19
Append Line: 12 2023-12-15 17:55:20
Append Line: 13 2023-12-15 17:55:21
Append Line: 14 2023-12-15 17:55:22
Append Line: 15 2023-12-15 17:55:23
Append Line: 16 2023-12-15 17:55:24
Append Line: 17 2023-12-15 17:55:25
Append Line: 18 2023-12-15 17:55:26
Append Line: 19 2023-12-15 17:55:27
Append Line: 20 2023-12-15 17:55:28
Append Line: 21 2023-12-15 17:55:29
Append Line: 22 2023-12-15 17:55:30
Append Line: 23 2023-12-15 17:55:31
Append Line: 24 2023-12-15 17:55:32
Append Line: 25 2023-12-15 17:55:33
0: Write Line: 0 2023-12-15 17:54:41
1: Write Line: 1 2023-12-15 17:54:42
2: Write Line: 2 2023-12-15 17:54:43
3: Write Line: 3 2023-12-15 17:54:44
4: Write Line: 4 2023-12-15 17:54:45
5: Write Line: 5 2023-12-15 17:54:46
6: Write Line: 6 2023-12-15 17:54:47
7: Write Line: 7 2023-12-15 17:54:48
8: Write Line: 8 2023-12-15 17:54:49
9: Write Line: 9 2023-12-15 17:54:50
10: Write Line: 10 2023-12-15 17:54:51
11: Write Line: 11 2023-12-15 17:54:52
12: Write Line: 12 2023-12-15 17:54:53
13: Write Line: 13 2023-12-15 17:54:54
14: Write Line: 14 2023-12-15 17:54:55
15: Write Line: 15 2023-12-15 17:54:56
16: Write Line: 16 2023-12-15 17:54:57
17: Write Line: 17 2023-12-15 17:54:58
18: Write Line: 18 2023-12-15 17:54:59
19: Write Line: 19 2023-12-15 17:55:00
20: Write Line: 20 2023-12-15 17:55:01
21: Write Line: 21 2023-12-15 17:55:02
22: Write Line: 22 2023-12-15 17:55:03
23: Write Line: 23 2023-12-15 17:55:04
24: Write Line: 24 2023-12-15 17:55:05
25: Write Line: 25 2023-12-15 17:55:06
0: Append Line: 0 2023-12-15 17:55:07
1: Append Line: 1 2023-12-15 17:55:08
2: Append Line: 2 2023-12-15 17:55:09
3: Append Line: 3 2023-12-15 17:55:10
4: Append Line: 4 2023-12-15 17:55:11
5: Append Line: 5 2023-12-15 17:55:12
6: Append Line: 6 2023-12-15 17:55:13
7: Append Line: 7 2023-12-15 17:55:14
8: Append Line: 8 2023-12-15 17:55:16
9: Append Line: 9 2023-12-15 17:55:17
10: Append Line: 10 2023-12-15 17:55:18
11: Append Line: 11 2023-12-15 17:55:19
12: Append Line: 12 2023-12-15 17:55:20
13: Append Line: 13 2023-12-15 17:55:21
14: Append Line: 14 2023-12-15 17:55:22
15: Append Line: 15 2023-12-15 17:55:23
16: Append Line: 16 2023-12-15 17:55:24
17: Append Line: 17 2023-12-15 17:55:25
18: Append Line: 18 2023-12-15 17:55:26
19: Append Line: 19 2023-12-15 17:55:27
20: Append Line: 20 2023-12-15 17:55:28
21: Append Line: 21 2023-12-15 17:55:29
22: Append Line: 22 2023-12-15 17:55:30
23: Append Line: 23 2023-12-15 17:55:31
24: Append Line: 24 2023-12-15 17:55:32
25: Append Line: 25 2023-12-15 17:55:33
c2310475021@os-server:~/lab_4$ ls
file1.txt  file2.txt  file_handle.py
````

#### What is a file descriptor

A file descriptor, as described in "Operating System Concepts" (10th Edition) by Abraham Silberschatz, is essentially an
index into a small table of open files for a process. Here are some key points about file descriptors based on this
definition:

* **Index in Open File Table**: A file descriptor is a numerical handle that uniquely identifies an open file within a
  process. It acts as an index in a table maintained by the operating system, where each entry in the table points to an
  open file.
* **Standard Descriptors**: File descriptors start at 0. The first three descriptors (0, 1, and 2) are typically
  reserved
  for standard input, standard output, and standard error, respectively.
* **Limited Range**: In most typical programs, file descriptors seldom exceed a small number, such as 6 or 7. This is
  because there's usually a limit to the number of files a process can open simultaneously.
* **File Offset Management**: Each time a file is read from or written to, the current offset in the file is updated.
  This
  offset is maintained in association with the file-table entry for that file and determines the position in the file
  for the next read or write operation.
* **Position Manipulation**: The lseek() system call allows explicit resetting of the file position, which is crucial
  for
  operations like seeking to a specific location in a file or creating sparse files.
* **Duplication and Control**: System calls like dup() and dup2() can be used to create new file descriptors that are
  copies
  of an existing one. Additionally, the fcntl() system call can be used to examine or set various parameters of an open
  file, including manipulation of its file descriptor.

File descriptors are a fundamental concept in operating systems, especially in Unix-like systems, where they provide a
low-level mechanism for file manipulation and I/O operations.

#### Where can you find information about the file descriptor? (Hint: A process is an instance of a computer program that is being executed)

Information about a process's file descriptors can be found in the Linux filesystem under the **_/proc_** directory.
Specifically, for each running process, there is a corresponding directory in **_/proc_** named after the process ID (
PID).
Within this directory, you can find detailed information about the file descriptors being used by the process.

Here are the specific locations where you can find information about file descriptors:

* **/proc/[PID]/fd**: This directory contains entries for each file descriptor that the process has open. Each entry is
  a symbolic link to the actual file or resource (like a socket or pipe) that the file descriptor references. By
  inspecting these links, you can determine what files, sockets, or other resources the process is currently using.
* **/proc/[PID]/fdinfo**: This directory provides detailed information about each file descriptor. Each file in this
  directory corresponds to a file descriptor and contains data such as the current file offset (pos), file status
  flags (flags), and mount point ID (mnt_id) associated with the file descriptor.

To access this information, you would replace **[PID]** with the actual process ID of the process you're interested in.
You
can find the process ID using commands like **ps**, **top**, or **htop**.

For example, if you want to inspect the file descriptors for a process with PID 1234, you would look at **/proc/1234/fd
**
and **/proc/1234/fdinfo**.

Remember, accessing these directories requires appropriate permissions. You might need superuser (root) privileges,
especially if you're inspecting a process that you don't own.

#### What does pos, flags and mnt_id mean? (Hint: “/proc/<processid>/fdinfo”)

In the context of `/proc/<processid>/fdinfo` on a Linux system, `pos`, `flags`, and `mnt_id` provide detailed
information about each file descriptor used by the process. Here's what each of these terms represents:

1. **pos**: This stands for "position." It indicates the current file offset for the file descriptor. This is
   essentially the position within the file where the next read or write operation will begin. For instance, if `pos` is
   set to 100, it means that the next read/write operation on this file descriptor will start from the 100th byte in the
   file.

2. **flags**: These are the file status flags associated with the file descriptor. They provide information about how
   the file or resource is being accessed. Common flags include whether the file is open for reading, writing, is set to
   append on each write, is non-blocking, and other such operational modes. These flags are often represented in a
   numeric format, and you can decode them to understand the file's access and status mode.

3. **mnt_id**: This stands for "mount identifier." It's a unique identifier for the mount point in the filesystem where
   the file or resource associated with the file descriptor is located. This is useful for tracking the actual physical
   or logical storage location being accessed by the process. For example, files on different mounted drives or network
   locations will have different `mnt_id` values.

Together, these pieces of information provide a comprehensive view of how a particular file or resource is being
accessed by a process at a given moment. This can be very useful for debugging, performance analysis, and understanding
the behavior of running processes on a Linux system.

#### Let’s have a look at the files. What permissions do your files have? (Hint: “ls -lahi proc/<processid>/fd/”)

```bash
c2310475021@os-server:~$ ps -u c2310475021 --forest
    PID TTY          TIME CMD
  38697 ?        00:00:00 sshd
  38698 pts/15   00:00:00  \_ bash
  39153 pts/15   00:00:00      \_ ps
  26741 ?        00:00:00 sshd
  26742 pts/4    00:00:00  \_ bash
  39049 pts/4    00:00:00      \_ file_handle.py
  26661 ?        00:00:00 systemd
  26664 ?        00:00:00  \_ (sd-pam)
c2310475021@os-server:~$ ls -lahi /proc/39049/fd/
total 0
491781 dr-x------ 2 c2310475021 student  0 Dec 15 18:20 .
468911 dr-xr-xr-x 9 c2310475021 student  0 Dec 15 18:19 ..
491784 lrwx------ 1 c2310475021 student 64 Dec 15 18:20 0 -> /dev/pts/4
491785 lrwx------ 1 c2310475021 student 64 Dec 15 18:20 1 -> /dev/pts/4
491786 lrwx------ 1 c2310475021 student 64 Dec 15 18:20 2 -> /dev/pts/4
491787 lr-x------ 1 c2310475021 student 64 Dec 15 18:20 3 -> /home/c2310475021/lab_4/file2.txt
c2310475021@os-server:~/lab_4$ ls -lahi
total 20K
800282 drwxr-xr-x  2 c2310475021 student 4.0K Dec 15 17:55 .
526006 drwxr-xr-x 12 c2310475021 student 4.0K Dec 15 17:54 ..
800308 -rw-r--r--  1 c2310475021 student  900 Dec 15 18:19 file1.txt
800310 -rw-r--r--  1 c2310475021 student 2.8K Dec 15 18:19 file2.txt
800309 -rwxrwxrwx  1 c2310475021 student 2.7K Dec 15 17:54 file_handle.py
```

Let's break down the permissions part of the Linux file listing for your examples:

##### Example 1: `file1.txt`

```
800308 -rw-r--r--  1 c2310475021 student  900 Dec 15 18:19 file1.txt
```

##### Example 2: `file2.txt`

```
800310 -rw-r--r--  1 c2310475021 student 2.8K Dec 15 18:19 file2.txt
```

For both examples, the format is similar, so I'll explain using `file1.txt` as the reference:

1. **800308**: This is the inode number of the file `file1.txt`. It's a unique identifier for the file within the
   filesystem.

2. **-rw-r--r--**: This represents the file permissions. Let's break this down:
    - `-`: The first character indicates the type of file. A dash (`-`) signifies that this is a regular file. Other
      possibilities include `d` for directory, `l` for symbolic link, etc.
    - `rw-`: The next three characters represent the permissions for the user who owns the file (`c2310475021` in this
      case). Here, `rw-` means the user has read (`r`) and write (`w`) permissions, but no execute (`x`) permission.
    - `r--`: The following three characters are the permissions for the group that owns the file (`student` in this
      case). `r--` means the group members can read the file but cannot write (`w`) or execute (`x`) it.
    - `r--`: The last three characters are the permissions for others (everyone else). Similar to the group, others can
      only read the file.

3. **1**: This number shows the count of hard links to this file. It indicates how many different directory entries
   point to this inode.

4. **c2310475021**: The name of the user who owns the file.

5. **student**: The name of the group that owns the file.

6. **900**: The size of the file in bytes. In the case of `file2.txt`, it's `2.8K`, indicating the file is 2.8 kilobytes
   in size.

7. **Dec 15 18:19**: The date and time when the file was last modified.

8. **file1.txt**: The name of the file.

Understanding file permissions is crucial for managing access and ensuring security on a Linux system. The permissions
determine who can read, write, or execute the file, which affects how the file can be used or modified.

**For the next 3 Tasks you must install Ubuntu on your own Machine**

1 CPU Core, 2 GB RAM, 32 GB HDD

[Linux and Windows](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox#1-overview)
[Linux and Windows YT Video](https://www.youtube.com/watch?v=v1JVqd8M3Yc)
[Mac M1](https://freegistutorial.com/install-ubuntu-22-10-on-m1-mac/)
[Mac](https://www.youtube.com/watch?v=EiO_CHfSn2s)

### 4.2 Run the script every 10 minutes

Use the [Cron-Daemon](https://wiki.ubuntuusers.de/Cron/) to run the script from 4.1 every 10 minutes.

#### What is a cronjob?

A cron job is a scheduled task in Unix and Unix-like operating systems, used for running specific tasks at predetermined
times or intervals. It's a fundamental tool for system maintenance and automation. The cron system is driven by a daemon
known as `crond` (cron daemon), which executes scheduled tasks based on definitions in crontab files.

Each user on a system can have their own crontab file, where they specify commands and the exact times for execution.
These commands are then executed by the cron daemon at the specified times. The syntax for scheduling a task in a
crontab file involves specifying the minute, hour, day of the month, month, day of the week, and the command to be
executed.

Cron jobs are widely used for a variety of system administration tasks, including backups, system updates, and regular
maintenance tasks. They're especially useful for automating repetitive tasks that need to run at regular intervals.

For more detailed and specific information on cron jobs and their usage in Ubuntu systems, you can refer to the Ubuntu
Users Cron Wiki page [here](https://wiki.ubuntuusers.de/Cron/).

Solution:

```bash
root@ubuntu-linux-22-04-02-desktop:/home/parallels# crontab -l
*/10 * * * * /usr/bin/python3 /home/parallels/lab4/file_handle.py
```

### 4.3 While 1

Add an infinite loop to your code.

```
procedure main()
    while(1)
        write_to_file(file1):
        append_to_file(file2):
```

Solution:

```python3
def main():
    while True:
        write_to_file("file1.txt")
        append_to_file("file2.txt")
```

#### Find out the pid (<processid>) of the process and look at “/proc/<processid>/maps”. What does the values mean?

```bash
root@ubuntu-linux-22-04-02-desktop:/home/parallels/lab4# ps aux --forest
root        1154  0.0  0.1   4032  2404 ?        Ss   19:49   0:00 /usr/sbin/cron -f -P
root       10137  0.0  0.1   9804  3804 ?        S    20:30   0:00  \_ /usr/sbin/CRON -f -P
root       10139  0.0  0.0   2308   832 ?        Ss   20:30   0:00      \_ /bin/sh -c /usr/bin/python3 /home/parallels/lab4/file_handle.py
root       10140  0.0  0.3  12624  7928 ?        S    20:30   0:00          \_ /usr/bin/python3 /home/parallels/lab4/file_handle.py

root@ubuntu-linux-22-04-02-desktop:/home/parallels/lab4# cat /proc/10140/maps
aaaaadda0000-aaaaae2c3000 r-xp 00000000 08:02 2359360                    /usr/bin/python3.10
aaaaae2d2000-aaaaae2d9000 r--p 00522000 08:02 2359360                    /usr/bin/python3.10
aaaaae2d9000-aaaaae318000 rw-p 00529000 08:02 2359360                    /usr/bin/python3.10
aaaaae318000-aaaaae35d000 rw-p 00000000 00:00 0 
aaaaaf358000-aaaaaf41d000 rw-p 00000000 00:00 0                          [heap]
ffffbdf02000-ffffbe189000 rw-p 00000000 00:00 0 
ffffbe189000-ffffbe1e0000 r--p 00000000 08:02 2361335                    /usr/lib/locale/C.utf8/LC_CTYPE
ffffbe1e0000-ffffbe369000 r-xp 00000000 08:02 2359316                    /usr/lib/aarch64-linux-gnu/libc.so.6
ffffbe369000-ffffbe378000 ---p 00189000 08:02 2359316                    /usr/lib/aarch64-linux-gnu/libc.so.6
ffffbe378000-ffffbe37c000 r--p 00188000 08:02 2359316                    /usr/lib/aarch64-linux-gnu/libc.so.6
ffffbe37c000-ffffbe37e000 rw-p 0018c000 08:02 2359316                    /usr/lib/aarch64-linux-gnu/libc.so.6
ffffbe37e000-ffffbe38a000 rw-p 00000000 00:00 0 
ffffbe390000-ffffbe3a8000 r-xp 00000000 08:02 2360649                    /usr/lib/aarch64-linux-gnu/libz.so.1.2.11
ffffbe3a8000-ffffbe3b8000 ---p 00018000 08:02 2360649                    /usr/lib/aarch64-linux-gnu/libz.so.1.2.11
ffffbe3b8000-ffffbe3b9000 r--p 00018000 08:02 2360649                    /usr/lib/aarch64-linux-gnu/libz.so.1.2.11
ffffbe3b9000-ffffbe3ba000 rw-p 00019000 08:02 2360649                    /usr/lib/aarch64-linux-gnu/libz.so.1.2.11
ffffbe3c0000-ffffbe3e7000 r-xp 00000000 08:02 2360496                    /usr/lib/aarch64-linux-gnu/libexpat.so.1.8.7
ffffbe3e7000-ffffbe3f7000 ---p 00027000 08:02 2360496                    /usr/lib/aarch64-linux-gnu/libexpat.so.1.8.7
ffffbe3f7000-ffffbe3f9000 r--p 00027000 08:02 2360496                    /usr/lib/aarch64-linux-gnu/libexpat.so.1.8.7
ffffbe3f9000-ffffbe3fa000 rw-p 00029000 08:02 2360496                    /usr/lib/aarch64-linux-gnu/libexpat.so.1.8.7
ffffbe400000-ffffbe486000 r-xp 00000000 08:02 2359328                    /usr/lib/aarch64-linux-gnu/libm.so.6
ffffbe486000-ffffbe495000 ---p 00086000 08:02 2359328                    /usr/lib/aarch64-linux-gnu/libm.so.6
ffffbe495000-ffffbe496000 r--p 00085000 08:02 2359328                    /usr/lib/aarch64-linux-gnu/libm.so.6
ffffbe496000-ffffbe497000 rw-p 00086000 08:02 2359328                    /usr/lib/aarch64-linux-gnu/libm.so.6
ffffbe4a8000-ffffbe4d3000 r-xp 00000000 08:02 2359309                    /usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1
ffffbe4d4000-ffffbe4db000 r--s 00000000 08:02 2373375                    /usr/lib/aarch64-linux-gnu/gconv/gconv-modules.cache
ffffbe4db000-ffffbe4df000 rw-p 00000000 00:00 0 
ffffbe4df000-ffffbe4e1000 r--p 00000000 00:00 0                          [vvar]
ffffbe4e1000-ffffbe4e2000 r-xp 00000000 00:00 0                          [vdso]
ffffbe4e2000-ffffbe4e4000 r--p 0002a000 08:02 2359309                    /usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1
ffffbe4e4000-ffffbe4e6000 rw-p 0002c000 08:02 2359309                    /usr/lib/aarch64-linux-gnu/ld-linux-aarch64.so.1
ffffe0503000-ffffe0524000 rw-p 00000000 00:00 0                          [stack]
```

The output of `/proc/<processid>/maps` provides a detailed view of a process's memory mapping. Each line represents a memory region. Let's break down what the values mean:

- **Memory Address Range**: `aaaaadda0000-aaaaae2c3000`. This is the range of virtual memory addresses allocated to this region.

- **Permissions**: `r-xp`. These indicate the memory region's permissions: `r` for read, `w` for write, `x` for execute, `p` for private (copy-on-write).

- **Offset**: `00000000`. The offset into the file/region where the mapping begins.

- **Device**: `08:02`. The major and minor device numbers (in hexadecimal) identifying the device.

- **Inode**: `2359360`. The inode on the device of the file that backs the mapping.

- **Path**: `/usr/bin/python3.10`. The file path associated with the region, if applicable.

This file is useful for understanding the memory layout of a process, including which parts of the process's address space are mapped to which files, and with what permissions. It can help in debugging, performance tuning, and security analysis.

#### Look at “/proc/<processid>/smaps”. What does the values Size, Rss, Pss, Shared_Clean,Shared_Dirty, Private_Clean, Private_Dirty, Referenced, Swap and SwapPss mean?



#### What is the pagesize of your system?

#### How can you print out all major and minor pagefaults?

#### Start htop and enter „swapoff –a“ on the terminal. What happens?

#### Reboot your system and print out all your page faults again.

### 4.4 Fill the RAM

Implement the following python script “ram.py”.

```
import sys, time
some_str = ' ' * 1024 * 1024 * 1024 * int(sys.argv[1])
while 1:
    print("true")
    time.sleep(1)
```

#### Start the python script on your Ubuntu. Start the script with the following arguments: 1, 2, 3, 4 and 5. (e.g.: python ram.py 1) What happens?

#### Start htop and enter „swapoff –a“ on the terminal. Start the script with the following arguments: 1, 2, 3, 4 and 5. What happens now? What has changed?

#### Try to change your operating system, to run the python script with all arguments (1, 2, 3, 4 and 5).

https://askubuntu.com/questions/178712/how-to-increase-swap-space

#### Compare the “/proc/meminfo” or “htop” with a running ram.py and a not running ram.py.
