#include <stdio.h>

#include <unistd.h>
int main() {
  int pid;
  pid = fork(); // returns 0 if successful
  if (pid == 0) {
    printf("%d\n", getpid());
    printf("%d\n", getppid());
  }
  return 0;
}
