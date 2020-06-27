#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include <ctype.h>


// Number of response our robot can make
#define NUM_RESPONSE 5

// Input the robot can recognize
char *INPUT_STR[] = {"Good", 
                     "Leaving", 
                     "Age", 
                     "Weather", 
                     "Sports"};

// Corresponding response the robot should make
char *RESPONSE_STR[] = {"Good day to you as well.", 
                        "Good bye.", 
                        "I am a robot and I am 4 hours old.", 
                        "It's raining.", 
                        "Go Ducks!",
                        "I don't understand what you are saying."};


void arg_test(int argc, char **argv);
void arg_print(int argc, char **argv);
void str_comparison(int argc, char **argv);
void str_case(int argc, char **argv);
void print_input();
void print_response();
void respond(int argc, char **argv);

int main(int argc, char **argv)
{
    // Sample code 
    arg_test(argc, argv);
    arg_print(argc, argv);
    str_comparison(argc, argv);
    str_case(argc, argv);
    print_input(); 
    print_response(); 

    // Homework 1, Part 1
    respond(argc, argv);

    return 0;
}



void arg_test(int argc, char **argv)
{
    if(argc < 2) {
        fprintf(stderr, "Error: no input entered\n");
        fprintf(stderr, "usage: %s <some input string>\n", argv[0]);
        fprintf(stderr, "\n");
    } else {
        // Do nothing
    }

}

void arg_print(int argc, char **argv)
{
    printf("# input (excluding the command): %d\n", argc - 1);
    // i starts from 1 as to skip the command
    for(int i = 1; i < argc; i++) {
        printf("Token %2d: ", i);
        // we are using value since length of a string will always >= 0
        // strlen returns the length of the string
        uint32_t length = strlen(argv[i]);
        // print each character from the string one at a time
        for(int j = 0; j < length; j++) {
            printf("%c", argv[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void str_comparison(int argc, char **argv)
{
    // Here we test out string comparison
    // refer to the man page for more detail
    printf("---- String Comparison ----\n");

    int comp = strcmp("spor", "Sports");
    printf("Return value of comparing 'a' and 'd': %d\n", comp);

    comp = strcmp("d", "a");
    printf("Return value of comparing 'd' and 'a': %d\n", comp);

    comp = strcmp("a", "a");
    printf("Return value of comparing 'a' and 'a': %d\n", comp);

    comp = strcmp("Hello", "hello");
    printf("Return value of comparing 'Hello' and 'hello': %d\n", comp);

    comp = strcmp("hello", "Hello");
    printf("Return value of comparing 'hello' and 'Hello': %d\n", comp);

    comp = strcmp("hello", "good bye");
    printf("Return value of comparing 'hello' and 'good bye': %d\n", comp);

    comp = strcmp("good bye!", "good bye");
    printf("Return value of comparing 'good bye!' and 'good bye': %d\n", comp);

    comp = strcmp("good bye", "good bye");
    printf("Return value of comparing 'good bye' and 'good bye': %d\n", comp);

    printf("--------\n\n");
}

void str_case(int argc, char **argv)
{
    char *test_str = "HelLO";
    printf("---- String Case Change ----\n");
    printf("%s to all lower case letters: ", test_str);
    for(int i = 0; i < strlen(test_str); i++)  {
        printf("%c", tolower(test_str[i]));    
    }
    printf("\n");

    printf("%s to all upper case letters: ", test_str);
    for(int i = 0; i < strlen(test_str); i++)  {
        printf("%c", toupper(test_str[i]));    
    }
    printf("\n");

    printf("--------\n\n");
}

void print_input()
{
    printf("---- Recognized Input ----\n");
    for(int i = 0; i < NUM_RESPONSE; i++) {
        printf("%d ::: %s\n", i, INPUT_STR[i]);
    }
    printf("--------\n\n");
}

void print_response()
{
    printf("---- Response ----\n");
    // Note that we are printing NUM_RESPONSE + 1 because of the
    // last undefined input response "I don't understand what you are saying."
    for(int i = 0; i < NUM_RESPONSE + 1; i++) {
        printf("%d ::: %s\n", i, RESPONSE_STR[i]);
    }
    printf("--------\n\n");
}

// This function should take in the input from the user
// and respond appropriately depending on whether the
// input contains a recognizable word (i.e., INPUT_STR_1~5);
// The apppropriate response to INPUT_STR[1] is RESPONSE_STR[1]
// and so on.
// If the input does not contain any of the recognizable words,
// respond with "I don't understand what you are saying."
// NOTE 1:
// The input can be in lower case, upper case, or any combination
// thereof. Be sure to account for that!
// NOTE 2:
// If a sentence contains multiple recognizable words, you should
// make multiple appropriate responses.
void respond(int argc, char **argv)
{
    printf("---- Answer ----\n");

    //found will change to 1 if the variable has found its recognized input
    //so that it will not continue to check against the other inputs
    int found = 0;
    int res = 0;

    //for each argument
    for(int i = 1; i <= argc - 1; i++)
    {	
    	//turn the first character into upper
    	argv[i][0] = toupper(argv[i][0]);
    	//change the rest to be all lower case
    	for(int j = 1; j < strlen(argv[i]); j++) 
    	{
    		argv[i][j] = tolower(argv[i][j]);   
   		}
    	//checks if the input is equal to one of the appropiate inputs
    	for(int k = 0; k < NUM_RESPONSE; k++)
    	{
    		//if the string is exact
    		if(strcmp(argv[i], INPUT_STR[k]) == 0)
    		{
    			printf("%s\n", RESPONSE_STR[k]);
    			found = 1;
    			res = 1;
    		}
       		//if the string has a punctuation
    		else if(strcmp(argv[i], INPUT_STR[k]) == 33 
    				|| strcmp(argv[i], INPUT_STR[k]) == 46 
    				|| strcmp(argv[i], INPUT_STR[k]) == 44
    				|| strcmp(argv[i], INPUT_STR[k]) == 63) 
    		{
    			printf("%s\n", RESPONSE_STR[k]);
    			found = 1;
    			res = 1;
    		}
    		//this argument has already found its match
    		if(found == 1)
    			break;
    	}
    	//reset found
    	found = 0;
    }
    //zero matches were found for any of the inputs
    if(res == 0)
    {
    	printf("%s\n", RESPONSE_STR[5]);
    }

    printf("----------------\n\n");
}

