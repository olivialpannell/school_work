#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "command.h"

int file_flag = 0;

int main(int argc, char **argv)
{
	/*Check if file mode*/
	if(strcmp(argv[1], "-f") == 0)
	{
		file_flag = 1;
		if(strcmp(argv[2], NULL))
		{
			printf("No filename detected. Please try again.\n");
			return 1;
		}
		else
		{
			/*Variables*/
			char output[] = "output.txt";
			size_t bufsize = 32;
			char *buffer;
			char *tok;
			char *tok2;
			char *semi;

			/*File opens*/
			FILE *f = fopen(argv[1], "r");
			FILE *fout = fopen(output, "w");

			/*Allocate Memory*/
			buffer = (char *)malloc(sizeof(char) * bufsize);

			getline(&buffer, &bufsize, f);
			while(1)
			{
				tok = strtok(buffer, " ");

				while(tok != NULL && (strcmp(tok, "\n") != 0))
				{
					if(strcmp(tok, ";") != 0)
					{
						if(strcmp(tok, "ls") == 0)
						{
							/*Check to make sure theres no extra parameters*/
							semi = strtok(NULL, " ");
							if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
							{
								printf("Error: Unsupported parameters for ls.\n");
								return 1;
							}
							listDir();
						}
						else if(strcmp(tok, "pwd") == 0)
						{
							/*Check to make sure theres no extra parameters*/
							semi = strtok(NULL, " ");
							if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
							{
								printf("Error: Unsupported parameters for pwd.\n");
								return 1;
							}
							showCurrentDir();
						}
						else if(strcmp(tok, "mkdir") == 0)
						{
							tok = strtok(NULL, " ");

							/*Check to make sure theres no extra parameters*/
							semi = strtok(NULL, " ");
							if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
							{
								printf("Error: Unsupported parameters for mkdir.\n");
								return 1;
							}
							makeDir(tok);
						}
						else if(strcmp(tok, "cd") == 0)
						{
							/*Get Directory Name*/
							tok = strtok(NULL, " ");

							/*Check to make sure theres no extra parameters*/
							semi = strtok(NULL, " ");
							if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
							{
								printf("Error: Unsupported parameters for cd.\n");
								return 1;
							}
							changeDir(tok);
						}
						else if(strcmp(tok, "cp") == 0)
						{
							/*Get Parameters*/
							tok = strtok(NULL, " ");
							tok2 = strtok(NULL, " ");

							/*Check to make sure theres no extra parameters*/
							semi = strtok(NULL, " ");
							if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
							{
								printf("Error: Unsupported parameters for cp.\n");
								return 1;
							}

							/*Call Function*/
							copyFile(tok, tok2);
						}
						else if(strcmp(tok, "mv") == 0)
						{
							/*Get Parameters*/
							tok = strtok(NULL, " ");
							tok2 = strtok(NULL, " ");

							/*Check to make sure theres no extra parameters*/
							semi = strtok(NULL, " ");
							if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
							{
								printf("Error: Unsupported parameters for mv.\n");
								return 1;
							}

							moveFile(tok, tok2);
						}
						else if(strcmp(tok, "rm") == 0)
						{
							tok = strtok(NULL, " ");

							/*Check to make sure theres no extra parameters*/
							semi = strtok(NULL, " ");
							if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
							{
								printf("Error: Unsupported parameters for rm.\n");
								return 1;
							}

							deleteFile(tok);
						}
						else if(strcmp(tok, "cat") == 0)
						{
							tok = strtok(NULL, " ");

							/*Check to make sure theres no extra parameters*/
							semi = strtok(NULL, " ");
							if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
							{
								printf("Error: Unsupported parameters for cat.\n");
								return 1;
							}

							displayFile(tok);
						}
						else
						{
							printf("Error! Incorrect syntax. No control code found.\n");
						}

					}
					else
					{
						printf("Error! \n");
					}
					tok = strtok(NULL, " ");

				}
				if(getline(&buffer, &bufsize, f) == -1)
				{
					break;
				}

			}

			/*Closes and Frees*/
			fclose(f);
			fclose(fout);
			free(buffer);


		}

	}
	/*Check if command mode*/
	else if(strcmp(argv[1], "-command") == 0)
	{
		/*Variables*/
		char output[] = "output.txt";
		size_t line;
		size_t bufsize = 32;
		char *buffer;
		char *tok;
		char *tok2;
		char *semi;

		/*Allocate Memory*/
		buffer = (char *)malloc(sizeof(char) * bufsize);

		while(1)
		{
			printf(">>>");
			line = getline(&buffer, &bufsize, stdin);
			tok = strtok(buffer, " ");
			printf("%s\n", tok);
			while(tok != NULL && (strcmp(tok, "\n") != 0))
			{
				if(strcmp(tok, ";") != 0)
				{
					if(strcmp(tok, "exit\n") == 0)
					{
						free(buffer);
						return 0;
					}
					if(strcmp(tok, "ls\n") == 0 || strcmp(tok, "ls") == 0)
					{
						/*Check to make sure theres no extra parameters*/
						semi = strtok(NULL, " ");
						printf("%s\n", semi);
						if( strcmp(semi, ";\n") == 0)
						{
							printf("in here\n");
						}
						if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || semi != NULL)
						{
							printf("Error: Unsupported parameters for ls.\n");
							return 1;
						}
						printf("AFTER\n");
						listDir();
					}
					else if(strcmp(tok, "pwd") == 0)
					{
						/*Check to make sure theres no extra parameters*/
						semi = strtok(NULL, " ");
						if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
						{
							printf("Error: Unsupported parameters for pwd.\n");
							return 1;
						}
						showCurrentDir();
					}
					else if(strcmp(tok, "mkdir") == 0)
					{
						tok = strtok(NULL, " ");

						/*Check to make sure theres no extra parameters*/
						semi = strtok(NULL, " ");
						if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
						{
							printf("Error: Unsupported parameters for mkdir.\n");
							return 1;
						}
						makeDir(tok);
					}
					else if(strcmp(tok, "cd") == 0)
					{
						/*Get Directory Name*/
						tok = strtok(NULL, " ");

						/*Check to make sure theres no extra parameters*/
						semi = strtok(NULL, " ");
						if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
						{
							printf("Error: Unsupported parameters for cd.\n");
							return 1;
						}
						changeDir(tok);
					}
					else if(strcmp(tok, "cp") == 0)
					{
						/*Get Parameters*/
						tok = strtok(NULL, " ");
						tok2 = strtok(NULL, " ");

						/*Check to make sure theres no extra parameters*/
						semi = strtok(NULL, " ");
						if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
						{
							printf("Error: Unsupported parameters for cp.\n");
							return 1;
						}

						/*Call Function*/
						copyFile(tok, tok2);
					}
					else if(strcmp(tok, "mv") == 0)
					{
						/*Get Parameters*/
						tok = strtok(NULL, " ");
						tok2 = strtok(NULL, " ");

						/*Check to make sure theres no extra parameters*/
						semi = strtok(NULL, " ");
						if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
						{
							printf("Error: Unsupported parameters for mv.\n");
							return 1;
						}

						moveFile(tok, tok2);
					}
					else if(strcmp(tok, "rm") == 0)
					{
						tok = strtok(NULL, " ");

						/*Check to make sure theres no extra parameters*/
						semi = strtok(NULL, " ");
						if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
						{
							printf("Error: Unsupported parameters for rm.\n");
							return 1;
						}

						deleteFile(tok);
					}
					else if(strcmp(tok, "cat") == 0)
					{
						tok = strtok(NULL, " ");

						/*Check to make sure theres no extra parameters*/
						semi = strtok(NULL, " ");
						if(strcmp(semi, ";") != 0 || strcmp(semi, "\n") != 0 || strcmp(semi, NULL) != 0)
						{
							printf("Error: Unsupported parameters for cat.\n");
							return 1;
						}

						displayFile(tok);
					}
					else
					{
						printf("Error! Incorrect syntax. No control code found.\n");
					}

				}
				else
				{
					printf("Error! \n");
				}
				tok = strtok(NULL, " ");
				
			}

		}
	}
	else
	{
		printf("Error: Please enter a mode (-f or -command)\n");
		return 1;
	}

	return 0;
}