#ifndef UART__H__
#define UART__H__

#include <stdio.h>
#include <sys/attribs.h> // __ISR macro
#include <xc.h>          // processor SFR definitions

char m[100]; // array for UART1

void readUART1(char *string, int maxLength);
void writeUART1(const char *string);
void initUART1();

#endif // UART__H__