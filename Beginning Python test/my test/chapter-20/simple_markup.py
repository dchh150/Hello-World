#代码清单20-3 一个简单的标记程序
#测试命令如下：
#python simple_markup.py <test_input.txt> test_output.html

import sys, re
from util import *

print("<html><head><title>...</title><body>")

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*',r'<em>\1</em>',block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print("</p>")
    
print("</body></html>")
