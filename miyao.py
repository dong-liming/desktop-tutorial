import secrets

# 生成一个 32 字节的随机密钥
secret_key = secrets.token_hex(32)
print(f"Generated SECRET_KEY: {secret_key}")