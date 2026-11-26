import urllib.request

SRC = "https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt"

text = urllib.request.urlopen(SRC, timeout=30).read().decode()
lines = [l.strip() for l in text.splitlines()
         if "://" in l and not l.startswith("#")
         and "127.0.0.1" not in l]  # این شرط اختیاری است

header = "#profile-title: My-Sub\n#profile-update-interval: 3\n"
open("configs.txt", "w", encoding="utf-8").write(header + "\n".join(lines) + "\n")
