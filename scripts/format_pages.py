from cgi import test
import os
import re
REPO_ROOT = ".."
SOURCE_PATH = "docs"


test_str = "{% embed url=\"https://docs.microsoft.com/zh-cn/windows/wsl/install-win10\" caption=\"cool stuff\" %}"
test_str = test_str + "\n" + test_str

pat_str = '\{%\ embed\ url="(.*?)"\ caption="(.*?)"\ %\}'
embed_pat = re.compile(pat_str)

sim_pat_str = '\{%\ embed\ url="(.*?)"\ %\}'
embed_sim_pat = re.compile(sim_pat_str)

end_pat_str = '{%\ endembed\ %}'
embed_end_pat = re.compile(end_pat_str)

def embed_repl(match):
    if match.group(2) != "":
        return "{1} [{0}]({0})".format(match.group(1), match.group(2))
    return "[{0}]({0})".format(match.group(1))

def embed_sim_repl(match):
    return "[{0}]({0})".format(match.group(1))

test_res = re.sub(embed_pat, embed_repl, test_str)
print(test_res)

test_str = "/.gitbook/assets/16.png"
test_str = re.sub("\.gitbook/assets", "attachments/assets", test_str)
test_str = re.sub("attachments/assets", "{{ site.baseurl }}/attachments/assets", test_str)
print(test_str)

for root, dirs, files in os.walk(os.path.join(REPO_ROOT, SOURCE_PATH)):
    for filename in files:
        if filename.endswith(".md") or filename.endswith(".markdown"):
            content = open(os.path.join(root, filename), encoding="utf-8").read() 
            
            match = re.findall(embed_pat, content)
            if len(match) > 0:
                print(match)
            content = re.sub(embed_pat, embed_repl, content)
            
            match = re.findall(embed_sim_pat, content)
            if len(match) > 0:
                print(match)
            content = re.sub(embed_sim_pat, embed_sim_repl, content)
            
            content = re.sub(embed_end_pat, "", content)
            
            content = re.sub("\.gitbook/assets", "attachments/assets", content)
            content = re.sub("attachments/assets", "{{ site.baseurl }}/attachments/assets", content)
            
            fw = open(os.path.join(root, filename), encoding="utf-8", mode="w")
            fw.write(content)
            
        
        