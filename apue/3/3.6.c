#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

void read_and_print_start(int fd);

int main(int argc, char *argv[]) {
	int fd = open(argv[1], O_RDWR, O_APPEND);

	read_and_print_start(fd);

	lseek(fd, 0, SEEK_SET);
	write(fd, "zyx", 3);

	read_and_print_start(fd);
}

void read_and_print_start(int fd) {
	char buf[4];
	int r;

	lseek(fd, 0, SEEK_SET);
	r = read(fd, buf, 4);

	printf("Read %i bytes: %s\n", r, buf);
}
