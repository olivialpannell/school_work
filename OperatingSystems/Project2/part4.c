/*
*	Author: Olivia Pannell
*	CS 415: Operating Systems
*	Description: Run and schedule a workload of programs on a system. This will read a list 
*   of programs (with arguments) to run from a file, start up and run the programs as processes, 
*	andthen schedule the processes to run concurrently in a time-sliced manner. 
*	In addition, the MCPwill monitor the processes, keeping track of how the processes are using 
*	system resources.
*	11/11/19
*/

/*----------------------------------Includes-------------------------------------*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
#include "header.h"
/*------------------------------------------------------------------------------*/

/*------------------------------Global Variables-----------------------------------*/
int ind = 0;
pid_t pid[10];
int count = 0;
/*------------------------------------------------------------------------------*/

/*---------------------Helper functions for finding the commands--------------------*/
/*This function tells get commands how many arguments exist*/
int get_num_commands (char *line, char sep) {
	int counter = 0;
	int isarg = 1;
	for (int i = 0; i < strlen (line); i++) 
	{
		if (line[i] != sep && isarg) 
		{
			counter++;
			isarg = 0;
		}
		else if (line[i] == sep) 
			isarg = 1;
	}
	return counter;
}

/*This function seperates each command and returns an array*/
char ** get_commands (char *line, int *length) 
{
	char buf [BUFSIZ];
	int count = get_num_commands (line, ' '); 
	*length = count;
	char **commands = (char **)malloc (sizeof (char *) * count);
	if (commands != NULL) 
	{
		strcpy (buf, line);
		char *command = strtok (buf, " ");
		int i = 0;
		while (command) 
		{
			commands [i++] = strdup(command);
			command = strtok (NULL, " ");
		}
	}
	return commands;
}
/*------------------------------------------------------------------------------*/

/*---------------------------Signal Helper Functions----------------------------------*/
void sighandler(int sig, siginfo_t *hello, void *test)
{
	sigset_t sigset;
	int stat;
	int *ptr = &stat;
	sigemptyset(&sigset);
	sigaddset(&sigset, SIGUSR1);

	//printf("Child Process: %d-Recieved Signal: %d\n", getpid(), sig);
	sigwait(&sigset, ptr);
}

void sigalarm(int sig)
{
	int stat;
	//printf("	Parent Process: %i - Caught Alarm\n", getpid());
	/*Check if any processes are alive*/
	while(waitpid(0, &stat, WNOHANG) < 0)
	{
		printf("none alive\n");
		return;
	}	
	/*If a process exists*/
	/*Stops process*/
	for(; ind < count; ind++)
	{
		if(kill(pid[ind], 0) == 0)
		{
			// printf("	Stopping Child Process...\n");
			kill(pid[ind], SIGSTOP);
			ind++;	
			if(ind == count){
			ind = 0;
			}	
			break;
		}
		
	}
	/*Continues next process*/
	for(;ind < count; ind++)
	{
		if(kill(pid[ind], 0) == 0)
		{
			//printf("--------------------Switching Commands---------------------\n");
			// printf("	Continuing Child Process...\n");
			kill(pid[ind], SIGCONT);
			break;
		}
	}
}

void sigchild(int sig, int c)
{
	/*Check if sig stop*/
	if(sig == 19){
		for(int i = 1; i < c; i++){
			//printf("	Child Process: %d - Recieved Signal: SIGSTOP\n", i+1);
			kill(pid[i], sig);
		}
	}
	else{
		for(int i = 0; i < c; i++){
			if(sig == 18){
				//printf("	Child Process: %d - Recieved Signal: SIGCONT\n", i+1);
			}
			else if(sig == 10){
				//printf("	Child Process: %d - Recieved Signal: SIGUSR1\n", i+1);
			}
			kill(pid[i], sig);
		}
	}
}
/*------------------------------------------------------------------------------*/

/*-------------------------Proc Information Function-------------------------------*/
/*PID Process output function*/
void procfun(int p)
{
	for(int i = 0; i < count; i++)
	{
		/*Proc variables*/
		char file[100] = "/proc/";
		char pidch[10];
		int co = 0;
		size_t length = 0;
		char * buf = NULL;

		/*Puts path together with pid*/
		if(p == 1)
			sprintf(pidch, "%d", getpid());
		else
			sprintf(pidch, "%d", pid[i]);
		strcat(file, pidch);
		strcat(file, "/stat");

		/*Open files*/
		FILE *fproc = fopen(file, "r");

		/*Get Info*/
		getline(&buf, &length, fproc);
		char *rand = strtok(buf, " ");
		if(p == 1)
			printf("-----------Parent Process: %d Information-----------\n", getpid());
		else
			printf("-------------PID: %d Process Information-------------\n", pid[i]);
		while(rand)
		{
			if(co == 0)
				printf("Process ID: %s\n", rand);
			else if(co == 1)
				printf("Executable: %s\n", rand);
			else if(co == 2)
				printf("State: %s\n", rand);
			else if(co == 3)
				printf("Parent Process: %s\n", rand);
			else if(co == 13)
				printf("Uptime: %s\n", rand);
			else if(co == 19)
				printf("Threads: %s\n", rand);
			else if(co > 20)
				break;
			co++;
			rand = strtok(NULL, " ");
		}
		fclose(fproc);

		/*Break if parent*/
		if(p == 1)
			break;
	}
}

/*Memory output function*/
void memfun()
{
	/* Proc Variables */
	int co = 0;
	size_t length2 = 0;
	char * buf2 = NULL;

	/*Opens meminfo*/
	FILE * fmem = fopen("/proc/meminfo", "r");
	getline(&buf2, &length2, fmem);
	printf("-------------------Memory Information------------------\n");
	for(int i = 0; i < 4; i++)
	{
		char *rand2 = strtok(buf2, "        ");
		rand2 = strtok(NULL, "        ");
		if(co == 0)
			printf("Total Memory: %s kB\n", rand2);
		else if(co == 1)
			printf("Memory Free: %s kB\n", rand2);
		else if(co == 2)
			printf("Memory Available: %s kB\n", rand2);
		else if(co == 3)
			printf("Buffers: %s kB\n", rand2);
		getline(&buf2, &length2, fmem);
		co++;
	}
	fclose(fmem);
}
/*------------------------------------------------------------------------------*/

/*----------------------------Processing File Function-----------------------------------*/
void process_file(char * filename) 
{
	/*Variables*/
	char *buf = NULL;
	size_t length = 0;
	int test = 0;
	char tmp[100];

	/*Signal variables*/
	sigset_t sigset;
	int stat;
	int *ptr = &stat;
	sigemptyset(&sigset);
	sigaddset(&sigset, SIGUSR1);
	struct sigaction s = {0};
	s.sa_sigaction = &sighandler;
	sigaction(SIGUSR1, &s, NULL);

	/*Opening files*/
	FILE * f = fopen(filename, "r");


	/*Gets every line of file*/
	while (getline (&buf, &length, f) > 0) 
	{
		/*Checks for newlines and carriage returns and deletes them*/
		int last_index = strlen (buf) - 1;
		if(buf [last_index] == '\n'){
			buf [last_index] = '\0';
		}
		if (last_index > 1) {
			if (buf [last_index-1] == '\r') {
				buf [last_index-1] = '\0';
			}
		}
	
		/*Gets commands in an array and replaces len with the amount 
		of arguments*/
		int len = 0;
		char ** commands = get_commands(buf, &len);
	
		/*Makes sure commands exist*/
		if (commands != NULL) {
			/*Fork and check if it forked correctly*/
			pid[count] = fork();
			if(pid[count] < 0){printf("Error: with pid.\n");}

			/*Child Process*/
			else if(pid[count] == 0)
			{
				/*Check it the command is running an executable*/
				if(commands[0][0] == '.' && commands[0][1] == '/')
				{
					printf("strlen: %ld \n", strlen(commands[0]));

					/*Keep track of executable in tmp*/
					strcpy(tmp, commands[0]);
					commands[len] = '\0';
					test = 1;
				}

				/*Set the wait*/	
				sleep(1);
				printf("Child Process: %d - Beginning waiting...\n", getpid());
				sigwait(&sigset, ptr);

				/*Execute the commands*/
				int ex;
				if(test == 1){
					printf("Child Process: %i - Executing commands...\n", getpid());
					ex = execvp(tmp, commands);
					
				}
				else
				{
					printf("Child Process: %i - Executing commands...\n", getpid());
					ex = execvp(commands[0], commands);
				}

				if(ex < 0)
				{
					printf("Invalid syntax.\n");
					exit(1);
				}
			}
			/*Free the commands*/
				for (int i = 0; i < len; i++) 
				{
					free (commands [i]);
				}

				free (commands);
		}
		count = count + 1;
	}
	/*Parent doing stuff*/
	/*Parent sends signals to children*/
	sleep(2);				
	sigchild(SIGUSR1, count);
	sigchild(SIGSTOP, count);

	/*Getting info from proc*/
	// system("clear");
	printf("--------------------------------------------------------\n");
	printf("------------------------PART 4--------------------------\n");
	printf("--------------------------------------------------------\n");
	memfun();
	procfun(1);
	procfun(0);
	printf("---------------------------------------------------------\n");
	printf("------------------------END PART 4-----------------------\n");
	printf("---------------------------------------------------------\n");

	/*Setting the alarm*/
	signal(SIGALRM, sigalarm);
	int wflag = 0;
	while(1)
	{
		alarm(3);
		sleep(3);
		/*If all children are done*/
		for(int i = 0; i < count; i++)
		{
			if(kill(pid[i], 0) == 0)
			{
				wflag = 0;
				break;
			}
			wflag = 1;
		}
		if(wflag == 1){
			break;
		}

	}

	/*Wait for children to finish*/
	printf("	Parent is Waiting for Child Process...\n");
	for(int i = 0; i < count; i++ )
	{
		wait(&pid[i]);
	}
	printf("------------------------FINISHED---------------------------\n");

	/*Closes and Frees*/
	fclose(f);
	free (buf);
}
/*------------------------------------------------------------------------------*/

/*-------------------------------------Main-----------------------------------------*/
int main(int argc, char * argv[])
{
	/*Check if user entered a file*/
	if(argc != 2)
	{
		printf("Error. Enter a file.\n");
		return 0;
	}
	process_file(argv[1]);
	return 0;
}
/*--------------------------------------END OF PROGRAM----------------------------------------*/
