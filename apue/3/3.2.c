#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int my_dup2(int fd, int fd2);

int main(int argc, char *argv[]) {
	if (argc != 3) {
		printf("ERROR: Need at least 2 arguments (`fd` and `fd2`)");
		exit(-1);
	}
	int r = my_dup2(atoi(argv[1]), atoi(argv[2]));
	printf("Found r: %i\n", r);
}

int my_dup2(int fd, int fd2) {
	if (fd == fd2) {
		return fd2;
	}

	close(fd2);
	int r = -1;
	int start = -1;
	while (r < fd2) {
		r = dup(fd);
		if (start == -1) {
			start = r;
		}
	}

	while (start < fd2) {
		close(start);
		start += 1;
	}

	return r;
}
