#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <fcntl.h> 
#include <sys/stat.h>
#include <unistd.h>
#include "command.h"

extern int file_flag;

/*for the ls command*/
void listDir()
{
	/*Get the current directory*/
	char cwdbuff[BUFSIZ];
	struct dirent * sdir;
	DIR * dir;

	/*open files*/
	int fout = open("output.txt", O_RDWR | O_CREAT | O_APPEND);

	/*Get cwd and make sure it worked*/
	if(getcwd(cwdbuff, sizeof(cwdbuff)) == NULL)
 	{
 		/*Find where to write error*/
 		if(file_flag){
 			write(fout, "Error while finding cwd.\n", strlen("Error while finding cwd.\n"));
 		}
 		else{
 			write(1, "Error while finding cwd.\n", strlen("Error while finding cwd.\n"));
 		}
 		exit(EXIT_FAILURE);
 		close(fout);
 	}
 	dir = opendir(cwdbuff);

	if (dir == NULL) 
	{
		if(file_flag){
 			write(fout, "Error opening directory\n", strlen("Error opening directory\n"));
 		}
 		else{
 			write(1, "Error while finding cwd.\n", strlen("Error while finding cwd.\n"));
 		}
	    closedir(dir);
	    close(fout);
	    exit(EXIT_FAILURE);
	}
	while((sdir = readdir(dir)) != NULL)
	{
		if(file_flag){
 			write(fout, sdir->d_name, strlen(sdir->d_name));
 			write(fout, "  ", strlen("  "));
 		}
 		else{
 			write(1, sdir->d_name, strlen(sdir->d_name));
 			write(1, "  ", strlen("  "));
 		}
	}
	/*Write a new line character*/
	if(file_flag){write(fout, "\n", strlen("\n"));}
	else{write(1, "\n", strlen("\n"));}
	
	close(fout);
	closedir(dir);

}

 /*for the pwd command*/
void showCurrentDir()
{
	/*Open files*/
	int fout = open("output.txt", O_RDWR | O_CREAT | O_APPEND);

	/*Find current working directory and print it*/
	char cwdbuff[BUFSIZ];
	if(getcwd(cwdbuff, sizeof(cwdbuff)) == NULL)
	{
 		if(file_flag){
 			write(fout, "Error while finding cwd.\n", strlen("Error while finding cwd.\n"));
 		}
 		else{
 			write(1, "Error while finding cwd.\n", strlen("Error while finding cwd.\n"));
 		}
 		close(fout);
 		exit(EXIT_FAILURE);
 	}
 	if(file_flag){
		write(fout, cwdbuff, strlen(cwdbuff));
 	}
 	else{
 		write(1, cwdbuff, strlen(cwdbuff));
 	}

 	/*Write a new line character*/
	write(1, "\n", strlen("\n"));

	/*Close file*/
	close(fout);
 	
}

/*for the mkdir command*/
void makeDir(char *dirName)
{
	/*Open files*/
	int fout = open("output.txt", O_RDWR | O_CREAT | O_APPEND);

	/*Connect dirName to current directory*/
	char cwdbuff[BUFSIZ];
	if(getcwd(cwdbuff, sizeof(cwdbuff)) == NULL)
	{
		if(file_flag){
 			write(fout, "Error with current directory in mkdir.\n", strlen("Error with current directory in mkdir.\n"));
 		}
 		else{
 			write(1, "Error with current directory in mkdir.\n", strlen("Error with current directory in mkdir.\n"));
 		}
 		close(fout);
 		exit(EXIT_FAILURE);
 		
 	}       
 	strcat(cwdbuff, "/");
 	strcat(cwdbuff, dirName);

 	/*Get rid of any trailing newline characters*/
 	char * p;
 	if((p = strchr(cwdbuff, '\n')) != NULL)
		*p = '\0';

	if(mkdir(cwdbuff, 0777) != 0)
	{
		write(1, "Error making new directory\n", strlen("Error making new directory\n"));
	}

	close(fout);
}

/*for the cd command*/
void changeDir(char *dirName)/*for the cd command*/
{
	/*Connect dirName to current directory*/
	char cwdbuff[BUFSIZ];
	if(getcwd(cwdbuff, sizeof(cwdbuff)) == NULL)
 	{
 		write(1, "Error with current directory in mkdir.\n", strlen("Error with current directory in mkdir.\n"));
 	} 

 	/*Return to root directory*/
 	if(dirName == NULL)
 	{
 		memmove(cwdbuff, cwdbuff+1, strlen(cwdbuff));
 		char * ps;
 		/*Check to make sure the directory isn't already the root*/
	 	if((ps = strchr(cwdbuff, '/')) == NULL)
	 	{
	 		char temp[256];
	 		return;
	 	}
	 	else
	 	{
			*ps = '\0';
			
	 	}
	 	

		char temp[256];
		strcpy(temp, "/");
		strcat(temp, cwdbuff);
		strcpy(cwdbuff, temp);

		ps = NULL;
 	}
 	/* Return to last directory*/
 	else if(strcmp(dirName, "..") == 0 || strcmp(dirName, "..\n") == 0)
 	{
 		char *pos = &cwdbuff[ strlen(cwdbuff) ];
	    while (pos > cwdbuff && *pos != '/')
	    {
	        pos--;
	    }
	    if (*pos== '/')
	    {
	        *pos= '\0';
	    }
	    // pos = NULL;
 	}
 	else
 	{
 		strcat(cwdbuff, "/");
 		strcat(cwdbuff, dirName);
 	}


 	/*Get rid of any trailing newline characters*/
 	char * p;
 	if((p = strchr(cwdbuff, '\n')) != NULL)
		*p = '\0';
	// p = NULL;

	printf("CWD: (%s)\n", cwdbuff);

	if(chdir(cwdbuff) != 0)
	{
		// if(file_flag)
 	// 	{
 	// 		int fout = open("output.txt", O_RDWR | O_CREAT);
 	// 		write(fout, "Error while changing directory.\n", strlen("Error while changing directory.\n"));
 	// 		close(fout);
 	// 	}
 	// 	else
 	// 	{
 			write(1, "Error while changing directory.\n", strlen("Error while changing directory.\n"));
 		// }
		exit(EXIT_FAILURE);
	}
}

/*for the cp command*/
void copyFile(char *sourcePath, char *destinationPath)
{
	// int f = open(sourcePath, O_RDONLY);
	// int fout = open(destinationPath, O_RDONLY | O_CREAT);

	// size_t bufsize = 32;
	// char *buffer = (char*)malloc(bufsize * sizeof(char));
	// getline(&buffer, &bufsize, f);
	// while(1)
	// {
		
	// 	if(file_flag)
	// 	{
	// 		write(destinationPath, buffer, strlen(buffer));
	// 	}
	// 	else
	// 		write(1, buffer, strlen(buffer));

	// 	if(getline(&buffer, &bufsize, f) == -1)
	// 	{
	// 		break;
	// 	}
	// }
	// close(f);
	// close(fout);
	// free(buffer);

}

/*for the mv command*/
void moveFile(char *sourcePath, char *destinationPath)
{
	/*Get rid of any trailing newline characters*/
 	char * p;
 	if((p = strchr(destinationPath, '\n')) != NULL)
		*p = '\0';

	if(rename(sourcePath, destinationPath) != 0)
	{
		write(1, "Error with moving file.\n", strlen("Error with moving file.\n"));
	}
}

/*for the rm command*/
void deleteFile(char *filename)
{
	/*Connect dirName to current directory*/
	char cwdbuff[BUFSIZ];
	if(getcwd(cwdbuff, sizeof(cwdbuff)) == NULL)
 	{
 		write(1, "Error with current directory in mkdir.\n", strlen("Error with current directory in mkdir.\n"));
 	}       
 	strcat(cwdbuff, "/");
 	strcat(cwdbuff, filename);
 	printf("%s\n", cwdbuff);

 	/*Get rid of any trailing newline characters*/
 	char * p;
 	if((p = strchr(cwdbuff, '\n')) != NULL)
		*p = '\0';


	if(unlink(cwdbuff) != 0)
	{
		// if(file_flag)
 	// 	{
 	// 		int fout = open("output.txt", O_RDWR | O_CREAT);
 	// 		write(fout, "Error deleting the file.\n", strlen("Error deleting the file.\n"));
 	// 		close(fout);
 	// 	}
 	// 	else
 	// 	{
 			write(1, "Error deleting the file.\n", strlen("Error deleting the file.\n"));
 		// }
 		exit(EXIT_FAILURE);
	}

}

/*for the cat command*/
void displayFile(char *filename)
{
	/*Connect dirName to current directory*/
	char cwdbuff[BUFSIZ];
	if(getcwd(cwdbuff, sizeof(cwdbuff)) == NULL)
 	{
 		write(1, "Error with current directory in mkdir.\n", strlen("Error with current directory in mkdir.\n"));
 	}       
 	strcat(cwdbuff, "/");
 	strcat(cwdbuff, filename);
 	printf("%s\n", cwdbuff);

	/*Get rid of any trailing newline characters*/
 	char * p;
 	if((p = strchr(cwdbuff, '\n')) != NULL)
		*p = '\0';

	int f = open(cwdbuff, O_RDONLY);
	if(f < 0)
	{
		write(1, "Error reading file.\n", strlen("Error reading file.\n"));
	}
	size_t bufsize = BUFSIZ;
	char *buffer = (char*)malloc(bufsize * sizeof(char));
	read(f, buffer, bufsize);
	printf("Buffer: %s\n", buffer);
	write(1, buffer, strlen(buffer));
	write(1, "\n", strlen("\n"));


	// getline(&buffer, &bufsize, f);
	// while(1)
	// {
	// 	// if(file_flag)
	// 	// {
	// 	// 	int fout = open("output.txt", O_RDWR | O_CREAT);
 // 	// 		write(fout, buffer, strlen(buffer));
 // 	// 		close(fout);

	// 	// }
	// 	// else
	// 		write(1, buffer, strlen(buffer));
	// 	if(getline(&buffer, &bufsize, f) == -1)
	// 	{
	// 		break;
	// 	}
	// }
	close(f);
	free(buffer);

}