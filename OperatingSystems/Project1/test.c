#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "command.c"

int file_flag = 0;

int get_num_commands (char *line) 
{
	int counter = 1;
	int i = 0;
	for (; i < strlen (line); i++) 
	{
		if (line [i] == ';')
			counter++;
	}
	return counter;
}

int get_argc (char * line)
{
	int counter = 0;
	int isarg = 1;
	for (int i = 0; i < strlen (line); i++) 
	{
		if (line[i] != ' ' && isarg) 
		{
			counter++;
			isarg = 0;
		}
		else if (line[i] == ' ') 
			isarg = 1;
	}
	return counter;
}

char ** get_argv (char *command, int *argc) 
{
	char buf [BUFSIZ];

	int count = get_argc (command); 
	*argc = count;
	char **args = (char **)malloc (sizeof (char *) * count);
	if (args != NULL) 
	{
		int j = 0;
		for (; j < strlen (command); j++) 
		{
			buf [j] = command [j];
		}
		buf [j] = '\0';
		char *arg = strtok (buf, " ");
		int i = 0;
		while (arg) 
		{
			args [i++] = strdup(arg);
			arg = strtok (NULL, " ");
		}
	}
	return args;

}

char ** get_commands (char *line, int *length) 
{
	char buf [BUFSIZ];

	int count = get_num_commands (line); 
	*length = count;
	char **commands = (char **)malloc (sizeof (char *) * count);
	if (commands != NULL) 
	{
		strcpy (buf, line);
		char *command = strtok (buf, ";");
		int i = 0;
		while (command) 
		{
			commands [i++] = strdup(command);
			command = strtok (NULL, ";");
		}
	}
	return commands;
}

void process_stdin() 
{
	char *buf = NULL;
	size_t length = 0;
	printf (">>> ");
	while (getline (&buf, &length, stdin) > 0) 
	{
		int len = 0;
		char ** commands = get_commands (buf, &len);
		if (commands != NULL) {
			for (int i = 0; i < len; i++) {
			
				if (strstr(commands[i], "exit") != NULL) {
					for (int j = i; j < len; j++)
						free (commands [j]);
					free (commands);
					free (buf);
					return;
				}
				int argc;
				char **args = get_argv (commands[i], &argc);
				if (args != NULL) {
					if(strstr(args[0], "ls") != NULL)
					{
						if(argc != 1)
						{
							printf("Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							listDir();
						}

					}
					else if(strstr(args[0], "pwd") != NULL)
					{
						if(argc != 1)
						{
							printf("Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							showCurrentDir();
						}
					}
					else if(strstr(args[0], "mkdir") != NULL)
					{
						if(argc != 2)
						{
							printf("Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							if(argc == 2) makeDir(args[1]);
							else makeDir(NULL);
						}

					}
					else if(strstr(args[0], "cd") != NULL)
					{
						if(argc > 2)
						{
							printf("Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							changeDir(args[1]);
						}

					}
					else if(strstr(args[0], "cp") != NULL)
					{
						if(argc != 3)
						{
							printf("Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							copyFile(args[1], args[2]);
						}

					}
					else if(strstr(args[0], "mv") != NULL)
					{
						if(argc != 3)
						{
							printf("Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							moveFile(args[1], args[2]);
						}

					}
					else if(strstr(args[0], "rm") != NULL)
					{
						if(argc != 2)
						{
							printf("Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							deleteFile(args[1]);
						}

					}
					else if(strstr(args[0], "cat") != NULL)
					{
						if(argc != 2)
						{
							printf("Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							displayFile(args[1]);
						}

					}
					for (int j = 0; j < argc; j++) {
						free (args[j]);
					}
					free (args);
				}
				free (commands [i]);
			}
			free (commands);
		}
		printf (">>> ");
	}
	free (buf);
}

void process_file(char * filename) 
{
	char *buf = NULL;
	size_t length = 0;

	FILE * f = fopen(filename, "r");
	FILE * fout = fopen("output.txt", "w");

	while (getline (&buf, &length, f) > 0) 
	{
		printf("BUFF: %s\n", buf);
		int len = 0;
		char ** commands = get_commands (buf, &len);
		if (commands != NULL) {
			for (int i = 0; i < len; i++) {
			
				if (strstr(commands[i], "exit") != NULL) {
					for (int j = i; j < len; j++)
						free (commands [j]);
					free(commands);
					free(buf);
					return;
				}
				int argc;
				char **args = get_argv (commands[i], &argc);
				if (args != NULL) {
					if(strstr(args[0], "ls") != NULL)
					{
						if(argc != 1)
						{
							fprintf(fout, "Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							listDir();
						}

					}
					else if(strstr(args[0], "pwd") != NULL)
					{
						if(argc != 1)
						{
							fprintf(fout, "Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							showCurrentDir();
						}
					}
					else if(strstr(args[0], "mkdir") != NULL)
					{
						if(argc != 2)
						{
							fprintf(fout, "Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							if(argc == 2) makeDir(args[1]);
							else makeDir(NULL);
						}

					}
					else if(strstr(args[0], "cd") != NULL)
					{
						if(argc > 2)
						{
							fprintf(fout, "Error! Incorrect syntax. No control code found.\n");
						}
						else
						{

							changeDir(args[1]);
						}

					}
					else if(strstr(args[0], "cp") != NULL)
					{
						if(argc != 3)
						{
							fprintf(fout, "Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							copyFile(args[1], args[2]);
						}

					}
					else if(strstr(args[0], "mv") != NULL)
					{
						if(argc != 3)
						{
							fprintf(fout, "Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							moveFile(args[1], args[2]);
						}

					}
					else if(strstr(args[0], "rm") != NULL)
					{
						if(argc != 2)
						{
							fprintf(fout, "Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							deleteFile(args[1]);
						}

					}
					else if(strstr(args[0], "cat") != NULL)
					{
						if(argc != 2)
						{
							fprintf(fout, "Error! Incorrect syntax. No control code found.\n");
						}
						else
						{
							displayFile(args[1]);
						}

					}
					for (int j = 0; j < argc; j++) {
						free (args[j]);
					}
					free (args);
				}
				free (commands [i]);
			}
			free (commands);
		}
		printf (">>> ");
	}
	fclose(f);
	fclose(fout);
	free (buf);
}


int main (int argc, char *argv []) 
{
	/* Make sure user entered a mode*/
	if(argc == 1)
	{
		printf("Error: Please enter a mode (-f or -command)\n");
		return 0;
	}


	/* Check for mode */
	if(strcmp(argv[1], "-f") == 0)
	{
		/*Check to make sure correct amount of arguments given*/
		if(argc > 3)
		{
			printf("Too many parameters. Please enter just -f (filename)\n");
			return 0;
		}
		else if(argc < 3)
		{
			printf("Error! Incorrect format. Please enter a filename after -f.\n");
			return 0;
		}
		else
		{
			file_flag = 1;
			process_file(argv[2]);
		}

	}
	else if(strcmp(argv[1], "-command") == 0)
	{
		/*Check to make sure correct amount of arguments given for command */
		if(argc != 2)
		{
			printf("Error! Too many parameters.\n");
			return 0;
		}
		else
		{
			process_stdin();
		}
	}

	return 0;
}
