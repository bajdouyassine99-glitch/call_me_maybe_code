#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <stdio.h>


// pthread_t t1;
// pthread_t t2;

// pthread_mutex_t lock;
// pthread_mutex_t lock2;

// pthread_cond_t cond;



// void *routine1(void *arg)
// {
//     char *ptr = (char *)arg;
    
//     pthread_mutex_lock(&lock2);
//     printf("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n");
//     ptr = malloc(1);
//     ptr[0] = 'a'; 
//     pthread_cond_signal(&cond);
//     printf("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n");
//     pthread_mutex_unlock(&lock2);
//     printf("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n");
//     return NULL;
// }

// void *routine2(void * arg)
// {
//     char *ptr = (char *)arg;
    
//     printf("xxxxxxxxxxxxxxxxxxxxxxxxx\n");
//     pthread_mutex_lock(&lock);
//     // free(*ptr);

//     if (!ptr)
//     {
//         printf("xxxxxxxxxxxxxxxxxxxxxxxxx\n");
//         // if (ptr)
//         // {
//         //     free(ptr);
//         //     break;
//         // }
//         // else
//         pthread_cond_wait(&cond, &lock);
//         printf("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n");
//         // printf("xxxxxxxxxxxxxxxxxxxxxxxxx\n");
//         free(ptr);
//     }    
//     pthread_mutex_unlock(&lock);
    
//     return NULL;
// }


// int main()
// {
//     char *ptr = NULL;
    
//     pthread_mutex_init(&lock, NULL);
//     pthread_mutex_init(&lock2, NULL);

//     pthread_cond_init(&cond, NULL);

//     pthread_create(&t1, NULL, routine1, ptr);
//     pthread_create(&t2, NULL, routine2, ptr);

//     pthread_join(t1, NULL);
//     pthread_join(t2, NULL);
// }



pthread_mutex_t lock;
pthread_cond_t cond;

pthread_t t1;
pthread_t t2;

// pthread_mutex_t lock;
// pthread_mutex_t lock2;

// pthread_cond_t cond;




// char *ptr = NULL;
int ready = 0;

void *routine1(void *arg)
{
    char **ptr = (char **) arg;
    sleep(1);
    pthread_mutex_lock(&lock);

    *ptr = malloc(1);
    *ptr[0] = 'a';

    ready = 1;
    pthread_cond_signal(&cond);

    pthread_mutex_unlock(&lock);
    return NULL;
}

void *routine2(void *arg)
{
    char **ptr = (char **) arg;
    
    pthread_mutex_lock(&lock);

    printf("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n");
    while (!ready)
        pthread_cond_wait(&cond, &lock);
    printf("%c\n", *ptr[0]);
    free(ptr);

    pthread_mutex_unlock(&lock);
    return NULL;
}


int main()
{
    char **ptr = NULL;
    
    pthread_mutex_init(&lock, NULL);

    pthread_cond_init(&cond, NULL);

    pthread_create(&t1, NULL, routine1, ptr);
    pthread_create(&t2, NULL, routine2, ptr);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
}