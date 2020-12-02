#include <iostream>
using namespace std;

void main(){
	char* strr;
	__asm {
		call qwer
		_emit 'm'
		_emit 'y'
		_emit 's'
		_emit 't'
		_emit 'r'
		_emit 0
		qwer:
		pop eax
		mov strr, eax
	}
	printf("%s", strr);
}