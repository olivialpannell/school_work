/*
*	Author: Olivia Pannell
*	CS 415: Operating Systems
*	Project 1- part 4
*	12/08/19
*/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/time.h>
#include <pthread.h>

/*-Global Variables-*/
#define MAXENTRIES 9
#define MAXTOPICS 4
#define MAXNAME 15
#define URLSIZE 200
#define CAPSIZE 200
#define MAXPROXIES 6
// #define MAXSUBS 4

pthread_t tid[MAXPROXIES + MAXPROXIES];
// pthread_mutex_t Q[MAXPROXIES * 2];
pthread_mutex_t biglock;
pthread_cond_t cond;
int flag = 0;
int delta = 3;

/*-------Structs-------*/
typedef struct topicEntry
{
	int entryNum;
	struct timeval timeStamp;
	int pubID;
	char photoURL[URLSIZE];
	char photoCaption[CAPSIZE];
} topicEntry;

typedef struct TEQ
{
	char topic[MAXNAME];
	struct topicEntry * buffer;
	int count;
	int head;
	int tail;
	int exists;
	int const length;
	pthread_mutex_t lock;
} TEQ;

typedef struct pub_arg{
	struct topicEntry a[MAXENTRIES];
	char *topic[MAXNAME];
	int th_id;
	char filename[100];
	int entnum;
}pub_arg;

/*Have a lot of stuff in here that i dont use in final product*/
typedef struct sub_arg{
	struct topicEntry a[MAXENTRIES];
	char *topic[MAXNAME];
	int th_id;
	char filename[100];
	int entnum;
}sub_arg;
struct TEQ registry[MAXTOPICS];
/*-------Initialize function-------*/
void initialize(char *id, int i, int len)
{
	strcpy(registry[i].topic, id);
	registry[i].buffer = (struct topicEntry *)malloc(sizeof(struct topicEntry) * len);
	registry[i].count = 0;
	registry[i].exists = 1;
	registry[i].head = 0;
	registry[i].tail = 0;
	flag = 0;
	int *l = (int *)&registry[i].length;
	*l = len;
	registry[i].buffer[registry[i].length - 1].entryNum = -1;

	// registry[i].lock = PTHREAD_MUTEX_INITIALIZER;
	pthread_mutex_init(&(registry[i].lock), NULL);

}

/*--Functions--*/
int enqueue(char *topic, struct topicEntry *ET)
{
	for(int i = 0; i < MAXTOPICS; i++)
	{
		if(strcmp(registry[i].topic, topic) == 0)
		{
			/*Check if full*/
			if(registry[i].count == MAXENTRIES)
			{
				return 0;
			}
			else
			{
				registry[i].count = registry[i].count + 1;
				gettimeofday(&ET->timeStamp, NULL);
				struct topicEntry *r = (struct topicEntry *)&registry[i].buffer[registry[i].tail];
				*r = *ET;
				printf("Enqueued: %s\n", registry[i].buffer[registry[i].tail].photoCaption);
				registry[i].tail = (registry[i].tail + 1) % (registry[i].length + 1);
				printf("Topic: %s Tail: %d\n", topic, registry[i].tail);
				return 1;
			}
		}
	}
	return 0;
}

int getEntry(char *ETQ_ID, int lastEntry, struct topicEntry *ET)
{
	int reg = -1;
	for(int i = 0; i < MAXTOPICS; i++)
	{
		if(strcmp(ETQ_ID, registry[i].topic) == 0)
		{
			reg = i;
			break;
		}
	}
	/*If no such ETQ_ID*/
	if(reg == -1)
	{
		printf("Failed to find ETQ_ID.\n");
		return 0;
	}
	/*If topic queue is empty*/
	else if(registry[reg].head == registry[reg].tail)
	{
		printf("Topic Queue: %s is empty.\n", ETQ_ID);
		return 0;
	}
	int current = registry[reg].head;
	while(current != registry[reg].tail)
	{
		/*Case 2*/
		if(registry[reg].buffer[current].entryNum == (lastEntry + 1))
		{
			/*Copies into ET*/
			ET->entryNum = lastEntry + 1;
			ET->timeStamp = registry[reg].buffer[current].timeStamp;
			ET->pubID = registry[reg].buffer[current].pubID;
			strcpy(ET->photoURL, registry[reg].buffer[current].photoURL);
			strcpy(ET->photoCaption, registry[reg].buffer[current].photoCaption);
			return 1;
		}
		/*Case 3.2*/
		else if(registry[reg].buffer[current].entryNum > (lastEntry + 1))
		{
			/*Copies into ET*/
			ET->entryNum = registry[reg].buffer[current].entryNum;
			ET->timeStamp = registry[reg].buffer[current].timeStamp;
			ET->pubID = registry[reg].buffer[current].pubID;
			strcpy(ET->photoURL, registry[reg].buffer[current].photoURL);
			strcpy(ET->photoCaption, registry[reg].buffer[current].photoCaption);

			lastEntry = ET->entryNum;
			return lastEntry;
		}
		/*Increase increment*/
		current = (current + 1) % (MAXENTRIES + 1);

		if(current == registry[reg].tail )
		{
			printf("No entry+1. \n");
			return 0;

		}
	}
	return 0;
}

int dequeue()
{
	/*Check each entry in every queue*/
	for(int i = 0; i < MAXTOPICS; i++)
	{
		for(int j = 0; j < MAXENTRIES; j++)
		{
			struct timeval current;
			gettimeofday(&current, NULL);
			/*Check if it has been in there for delta or more*/
			if((registry[i].buffer[j].timeStamp.tv_sec + delta) >= current.tv_sec)
			{
				//NEED TO COME BACK HERE
				/*Cleanup and update end of buffer*/
				registry[i].count--;
				registry[i].buffer[registry[i].head].entryNum = -1;
				registry[i].buffer[(registry[i].head - 1) % (registry[i].length)].entryNum = 0;
				registry[i].head = (registry[i].head + 1) % (registry[i].length);
			}
		}
	}
	return 0;
}
/*------------*/

/*-----Pub/Sub-------*/
void *publisher(void *args) {
	void * useless = NULL;
	struct pub_arg * parg = (struct pub_arg *)args;
	printf("Created Publisher Thread: %d \n", parg->th_id);

	/*variables*/
	char * buf = NULL;
	char * pntr = NULL;
	char * pntr2 = NULL;
	size_t length = 0;
	int success = 0;
	FILE *f = fopen(parg->filename, "r");
	while(getline(&buf, &length, f) > 0)
	{
		int last_index = strlen(buf) - 1;
		if(buf[last_index] == '\n'){
			buf[last_index] = '\0';
		}
		char* arg = strtok_r(buf, " ", &pntr);
		if(arg != NULL)
		{
			if(strcmp(arg, "put") == 0)
			{
				/*Get just id, topic name, and link*/
				char* num = strtok_r(NULL, " ", &pntr);
				char* temp1 = strtok_r(NULL, " ", &pntr);
				char* temp2 = strtok_r(NULL, " ", &pntr);
				char* link = strtok_r(temp1, "\"", &pntr2);
				char* topic =  strtok_r(temp2, "\"", &pntr2);
				/*Cast to ints*/
				int n = atoi(num);
				/*Fill in new topic entry*/
				topicEntry te;
				te.entryNum = registry[n-1].count;
				te.pubID = registry[n-1].count + 1;
				strcpy(te.photoURL, link);
				strcpy(te.photoCaption, topic);
				/*Lock the enqueue*/
				sched_yield();
				pthread_mutex_lock(&registry[n-1].lock);
				if(!flag)
				{
					pthread_mutex_lock(&biglock);
					pthread_cond_wait(&cond, &biglock);
					pthread_mutex_unlock(&biglock);
				}
				success = enqueue(registry[n-1].topic, &te);
				if(success == 0)
				{
					printf("Enqueue Failed.\n");
				}
				/*Unlock*/
				pthread_mutex_unlock(&registry[n-1].lock);
			}
			else if(strcmp(arg, "sleep") == 0)
			{
				/*Change to milliseconds*/
				arg = strtok_r(NULL, " ", &pntr);
				int n = atoi(arg);
				n = n /1000;
				sleep(n);	
			}
			else if(strcmp(arg, "stop") == 0)	
			{
				printf("stopping...\n");
			}	
		}
	}
	return useless;
}
void *subscriber(void *args) {
	void * useless = NULL;
	struct sub_arg *sarg = (struct sub_arg *)args;
	struct topicEntry test;
	printf("Created Subscriber Thread: %d \n", sarg->th_id);

	/*variables*/
	char * buf = NULL;
	char * pntr = NULL;
	size_t length = 0;
	int success = 0;

	FILE *f = fopen(sarg->filename, "r");
	while(getline(&buf, &length, f) > 0)
	{
		int last_index = strlen(buf) - 1;
		if(buf[last_index] == '\n'){
			buf[last_index] = '\0';
		}
		char* arg = strtok_r(buf, " ", &pntr);
		if(arg != NULL)
		{
			if(strcmp(arg, "get") == 0)
			{
				/*Get just id*/
				char* num = strtok_r(NULL, " ", &pntr);
				/*Cast to ints*/
				int n = atoi(num);
				/*Lock the getEntry*/
				sched_yield();
				pthread_mutex_lock(&registry[n-1].lock);
				if(!flag)
				{
					pthread_mutex_lock(&biglock);
					pthread_cond_wait(&cond, &biglock);
					pthread_mutex_unlock(&biglock);
				}
				success = getEntry(registry[n-1].topic, registry[n-1].count, &test);
				if(success == 0)
				{
					printf("GetEntry failed.\n");
				}
				else
				{
					printf("Entry from: %s - Photo URL: %s - Photo Caption: %s \n", registry[n-1].topic, test.photoURL, test.photoCaption);
				}
				/*Unlock*/
				pthread_mutex_unlock(&registry[n-1].lock);
			}
			else if(strcmp(arg, "sleep") == 0)
			{
				/*Change to milliseconds*/
				arg = strtok_r(NULL, " ", &pntr);
				int n = atoi(arg);
				n = n /1000;
				sleep(n);	
			}
			else if(strcmp(arg, "stop") == 0)	
			{
				printf("stopping...\n");
			}	
		}
	}
	return useless;
}

// void *topiccleanup(void * it)
// {
// 	sleep(5);
	
// }



/*------------*/
/*Print topics*/
void printtop()
{
	for(int i = 0; i < MAXTOPICS; i++)
	{
		if(registry[i].exists != 1)
		{
			return;
		}
		printf("Topic: %s - ID: %d - Length: %d\n", registry[i].topic, i+1, registry[i].length);
	}
}
/*Print subscribers*/
void printsub()
{
	// for(int i = 0; i < MAXPROXIES; i++)
	// {
	// 	if(registry[i].exists != 1)
	// 	{
	// 		return;
	// 	}
	// 	printf("Topic: %s - ID: %d - Length: %d\n", registry[i].topic, i+1, registry[i].length);
	// }
}
/*Print publishers*/
void printpub()
{
	// for(int i = 0; i < MAXPROXIES; i++)
	// {
	// 	if(registry[i].exists != 1)
	// 	{
	// 		return;
	// 	}
	// 	printf("Topic: %s - ID: %d - Length: %d\n", registry[i].topic, i+1, registry[i].length);
	// }
}

void startfun()
{
	flag = 1;
	pthread_mutex_lock(&biglock);
	pthread_cond_broadcast(&cond);
	pthread_mutex_unlock(&biglock);
}


/*----Main----*/
int main(int argc, char const *argv[])
{
	if(argc != 2)
	{
		printf("Please enter a file.\n");
		return 0;
	}

	char * buf = NULL;
	char * pntr = NULL;
	char * pntr2 = NULL;
	size_t length = 0;
	int numpub = 0;
	int numsub = 0;

	FILE *f = fopen(argv[1],"r");

	while(getline(&buf, &length, f) > 0)
	{
		/*Get rid of newline*/
		int last_index = strlen (buf) - 1;
		if(buf [last_index] == '\n'){
			buf [last_index] = '\0';
		}
		char* arg = strtok_r(buf, " ", &pntr);
		if(arg != NULL)
		{
			/*Find which category*/
			if(strcmp(arg, "create") == 0)
			{
				/*Once to get rid of topic then second one gets the num*/
				arg = strtok_r(NULL, " ", &pntr);
				char* num = strtok_r(NULL, " ", &pntr);
				arg = strtok_r(NULL, " ", &pntr);
				char* length = strtok_r(NULL, " ", &pntr);
				char* name = strtok_r(arg, "\"", &pntr2);
				/*Cast to ints*/
				int n = atoi(num);
				int len = atoi(length);

				/*Initialize queue*/
				initialize(name, n-1, len);
				printf("Created: %s Queue.\n", name);

			}
			else if(strcmp(arg, "query") == 0)
			{
				/*Print out things*/
				arg = strtok_r(NULL, " ", &pntr);
				if(strcmp(arg, "topics") == 0){
					printtop();
				}
				else if(strcmp(arg, "publishers") == 0){
					printpub();
				}
				else if(strcmp(arg, "subscribers") == 0){
					printsub();
				}
			}
			else if(strcmp(arg, "add") == 0)
			{
				/*Print out things*/
				arg = strtok_r(NULL, " ", &pntr);
				char *temp = strtok_r(NULL, " ", &pntr);
				char* filename = strtok_r(temp, "\"", &pntr2);
				if(strcmp(arg, "publisher") == 0){
					struct pub_arg parg;
					strcpy(parg.filename, filename);
					parg.th_id = numpub + 1;
					pthread_create(&tid[numpub], NULL, publisher, &parg);
					sleep(1);
					numpub++;
				}
				else if(strcmp(arg, "subscriber") == 0){
					struct sub_arg sarg;
					strcpy(sarg.filename, filename);
					sarg.th_id = numsub + 1;
					pthread_create(&tid[numsub], NULL, subscriber, &sarg);
					sleep(1);
					numsub++;
				}
			}
			else if(strcmp(arg, "delta") == 0)
			{
				arg = strtok_r(NULL, " ", &pntr);
				delta = atoi(arg);
			}
			else if(strcmp(arg, "start") == 0)
			{
				printf("starting...\n");
				startfun();
			}
		}

	}

	/*Join Thread-Pools*/
	for(int i = 0; i < (numpub + numsub); i++)
	{
		pthread_join(tid[i], NULL);
	}







	// pub_arg parg;
	// sub_arg sarg; 



	// /*Publisher Thread pool*/
	// for(int i = 0; i < MAXPROXIES; i++)
	// {
	// 	pthread_create(&tid[i], NULL, publisher, &parg);
	// }
	// /*Subscriber Thread pool*/
	// for(int i = 0; i < MAXPROXIES; i++)
	// {
	// 	pthread_create(&tid[i], NULL, subscriber, &sarg);
	// }

	// /*Join Thread-pools*/
	// int total = MAXPROXIES + MAXPROXIES;
	// for(int i = 0; i < total; i++)
	// {
	// 	pthread_join(tid[i], NULL);
	// }

	/*Frees*/
	for(int i = 0; i < MAXTOPICS; i++)
	{
		free(registry[i].buffer);
	}

	return 0;
}
/*END OF PROGRAM*/