3.1. No. The kernel may cache data on an internal buffer. This buffer may be synced either automatically by the kernel after a set time or whenever it needs more buffer space; but also synced programatically by calling the fsync function.

3.3. `F_SETFD` modifies the file descriptor flags, which lives inside the process table, so only fd1 should be modified. `F_SETFL` should modify the file status flags, which live inside the file table, so both `fd1` and `fd2` should be modified.

3.4. For fd = 1:
0 is closed. 0 points to fd 1.
nothing happens
2 is close. 2 points to fd 1.

For fd = 3:
0 is closed. 0 points to fd 3.
1 is closed. 1 points to fd 3.
2 is closed. 2 points to fd 3.
3 is closed.

3.5 The first one will have STDOUT and STDERR redirected to `outputfile`. The second one will have STDERR redirect to console, and STDOUT  redirected to file.

3.6 Yes, you can still read and write, even though the file was opened with append.
