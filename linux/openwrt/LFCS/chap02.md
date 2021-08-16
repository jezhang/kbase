
### find

- Very powerful command to search for files or directories
- Can search by name, file type, timestamp and many other file attributes
- Supports expressions and blobbing for advanced searchs
- Searches in realtime, so it can be slow on machines with lots of files

```sh
find / -name "nginx.conf"

find / -iname "nginx.conf"

find / -type f -name "*.log"

find /etc -type -f -user root

```

### locate

- Fast search than find
- Limited search options: can't search by attributes or metadata
- 

### which

### whereis

### type

### diff

 - Compares two files or directories line by line
 - Several options for ignoring, filtering the comparison
 - Output can be displayed in ed format, context mode, or unified format
 
### comm

 - Compare two _sorted_ files line by line
 - Output is displayed in 3 columns, uniquie to file1, unique to file2, and the same in both files.

### cmp
 - Compares two files, byte by byte, and returns the position of the first difference



