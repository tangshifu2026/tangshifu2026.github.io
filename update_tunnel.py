"""每次隧道地址变化时运行此脚本，自动更新 index.html 中的隧道地址"""
import re, os

# 读取当前隧道地址
tunnel_file = "D:/AI/video_index/tunnel_url.txt"
if not os.path.exists(tunnel_file):
    print("隧道文件不存在，跳过")
    exit(0)

with open(tunnel_file, "r") as f:
    tunnel = f.read().strip()
    # 去掉 /dashboard 后缀
    tunnel = re.sub(r'/dashboard$', '', tunnel)

html_file = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

# 替换旧的 trycloudflare URL
old_pattern = r"https://[a-z0-9\-]+\.trycloudflare\.com"
new_content = re.sub(old_pattern, tunnel, content)

if new_content != content:
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"已更新隧道地址: {tunnel}")
else:
    print(f"隧道地址未变化: {tunnel}")
