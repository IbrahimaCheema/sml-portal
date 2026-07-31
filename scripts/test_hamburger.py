import glob
h = r'C:\Users\ibrah\.gemini\antigravity\scratch\sml-astro-app\dist\shareholders-information.html'
html = open(h, encoding='utf-8').read()
count = html.count('id="hamburger"')
print("Count of hamburger:", count)
