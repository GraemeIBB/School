#include <pthread.h>
#include <stdatomic.h>
#include <stdio.h>
#include <unistd.h>

atomic_flag lock = LOCK_FLAG_INIT;

void acquire_lock()

    int main() {
  pthread_t t1, t2;
  int id1 = 1, id2 = 2;

  pthread_create(&t1, NULL, worker, &id1);
  pthread_create(&t2, NULL, worker, &id2);
}
