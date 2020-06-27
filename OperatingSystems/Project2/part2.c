/*
*	Author: Olivia Pannell
*	CS 415: Operating Systems
*	Project 1- part 2
*	11/11/19
*/

/*----------------------------------Includes-------------------------------------*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>
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

	printf("Child Process: %d-Recieved Signal: %d\n", getpid(), sig);
	sigwait(&sigset, ptr);
}

void sigchild(pid_t *pid, int sig, int c)
{
	for(int i = 0; i < c; i++)
	{
		if(sig == 19)
			printf("	Child Process has STOPPED - Recieved signal: %d...\n", sig);
		else if(sig == 18)
			printf("	Child Process has CONTINUED - Recieved signal: %d...\n", sig);
		else if(sig == 10)
			printf("	Child Process has recieved USR1 - Recieved signal: %d...\n", sig);
		kill(pid[i], sig);
	}
}
/*------------------------------------------------------------------------------*/

/*----------------------------Processing File Function-----------------------------------*/
void process_file(char * filename) 
{
	/*Variables*/
	char *buf = NULL;
	size_t length = 0;
	pid_t pid [10];
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
	int count = 0;

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
					ex = execvp(tmp, commands);
				}
				else
				{
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
	sigchild(pid, SIGUSR1, count);
	sleep(3);
	sigchild(pid, SIGSTOP, count);
	sleep(3);
	sigchild(pid, SIGCONT, count);

	/*Wait for children to finish*/
	printf("Parent is waiting for child process...\n");
	for(int i = 0; i < count; i++ )
	{
		wait(&pid[i]);
	}

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
