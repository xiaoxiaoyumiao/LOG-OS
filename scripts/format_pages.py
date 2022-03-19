from cgi import test
import os
import re
REPO_ROOT = ".."
SOURCE_PATH = "docs"


test_str = "{% embed url=\"https://docs.microsoft.com/zh-cn/windows/wsl/install-win10\" caption=\"cool stuff\" %}"
test_str = test_str + "\n" + test_str
pat_str = r'{% embed url="(*?)" caption="(*?)" %}'
print(re.escape(pat_str))
pat_str = '\{%\ embed\ url="(.*?)"\ caption="(.*?)"\ %\}'
embed_pat = re.compile(pat_str)
res = re.findall(embed_pat, test_str)
print(res[0][0])

def embed_repl(match):
    if match.group(2) != "":
        return "{1} [{0}]({0})".format(match.group(1), match.group(2))
    return "[{0}]({0})".format(match.group(1))

test_res = re.sub(embed_pat, embed_repl, test_str)
print(test_res)

for root, dirs, files in os.walk(os.path.join(REPO_ROOT, SOURCE_PATH)):
    for filename in files:
        if filename.endswith(".md") or filename.endswith(".markdown"):
            content = open(os.path.join(root, filename), encoding="utf-8").read() 
            match = re.findall(embed_pat, content)
            if len(match) > 0:
                print(match)
            content = re.sub(embed_pat, embed_repl, content)
            fw = open(os.path.join(root, filename), encoding="utf-8", mode="w")
            fw.write(content)
            
        
        