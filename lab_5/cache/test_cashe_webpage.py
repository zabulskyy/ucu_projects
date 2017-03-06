from cashe_webpage import WebPage
import time
wp = WebPage("http://ccphillips.net/")
now = time.time()
content1 = wp.content
print(time.time() - now)
now = time.time()
content2 = wp.content
print(time.time() - now)
print(content2 == content1)
wp.refresh()
now = time.time()
content3 = wp.content
print(time.time() - now)
now = time.time()
content4 = wp.content
print(time.time() - now)

print(content2 == content1 and content3 == content4 and content2 == content4 )