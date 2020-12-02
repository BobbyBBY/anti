#include <iostream>
#include<stdio.h>
#include<string.h>
#pragma warning(disable:4996)
using namespace std;
void func(char* src) {
	char buf[4];
	strcpy(buf, src);
}
char gbuf[13] = "11111111111";//12¸ö1

int main() {
	void* p;
	_asm {
		push ebp
		mov p, offset aa;
	}
	*((void**)(gbuf + 8)) = p;
	func(gbuf);
	printf("heelo,never execute\n");
	goto end;
	aa:
		_asm add esp, 4;
		_asm pop ebp;
	printf("new path\n");
	end:
		printf("end\n");

	system("pause");
	return 0;
}
