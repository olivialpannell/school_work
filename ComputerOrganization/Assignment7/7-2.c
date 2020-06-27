// Olivia Pannell
// Assignment 7 Question 2

#include <stdio.h>

// returns the byte offset of the address
// within its cache block.
unsigned int getOffset(unsigned int address)
{
	//create mask for hex and des
	unsigned int mk, des;
	//get only the offset of the bits
	mk = 0x0000000F;
	// AND the two to get only whats needed in address and return 
	des = address & mk;
	return des;

}
// returns the cache set for the address.
unsigned int getSet(unsigned int address) 
{
	// create another mask this time only grabbing the part of the address for set
	// then and them together and shift to get it rightmost
	unsigned int mk, des;
	mk = 0x000000F0;
	des = address & mk;
	des = des >> 4;
	return des;
}
// returns the cache tag for the address
unsigned int getTag(unsigned int address) 
{
	// creates a mask for the tag
	// ands that with the address 
	// then shift the unnecessary bits out
	unsigned int mk, des;
	mk = 0xFFFFFF00;
	des = address & mk;
	des = des >> 8;
	return des;
}

int main()
{
	unsigned int test1 = 0x12345678;
	unsigned int test2 = 0x87654321;
	

	//first test
	printf("0x12345678: offset: %x ", getOffset(test1));
	printf(" - tag: %x ", getTag(test1));
	printf("- set: %x \n", getSet(test1));

	//second test
	printf("0x87654321: offset: %x ", getOffset(test2));
	printf(" - tag: %x ", getTag(test2));
	printf("- set: %x \n", getSet(test2));

	return 0;
}