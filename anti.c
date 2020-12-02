#include <stdio.h>
#include <string.h>

void copy(char *msg)
{
    char buffer[16];
    strcpy(buffer,msg);
    return;
}

int main()
{
    puts("请输入：");
    char buffer[256];
    memset(buffer,0,256);//清空输入内容区域
    read(0,buffer,256);
    copy(buffer);
    return 0;
}
