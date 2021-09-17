import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

load_url = "http://google.com"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
if(soup.find('exec()', 'system()')):
    print('PerlにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find('`...`', 'qx/.../')):
    print('PerlにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find('open(h, "|{command}")','open(h, "{command}|"))')):
     print('PerlにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find('exec()','passthru()')):
    print('PerlにOSコマンド・インジェクションの脆弱性あり')#ここまでPerl
elif(soup.find('os.system()','os.popen()')):
    print('PythonにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find('proc_open()','shell_exec()','system()')):
    print('PythonにOSコマンド・インジェクションの脆弱性あり')#ここまでPython
elif(soup.find('exec()','system()','`...`')):
    print('RubyにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find('open("|{command}", mode, perm)','open("|-{command}", mode, perm)')):
    print('RubyにOSコマンド・インジェクションの脆弱性あり')#ここまでRuby
elif(soup.find('$','<','>','*')):
    print('特殊文字を検出、OSコマンド・インジェクションの可能性あり')
elif(soup.find('?','{','}')):
    print('特殊文字を検出、OSコマンド・インジェクションの可能性あり')
elif(soup.find('[',']','!')):
    print('特殊文字を検出、OSコマンド・インジェクションの可能性あり')
else:
    print('OSコマンド・インジェクションの脆弱性は見つかりませんでした')
