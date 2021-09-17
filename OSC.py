import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

load_url = "http://192.168.0.13/dvwa/vulnerabilities/javascript/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# HTML全体を表示する
if(soup.find_all('label','autocomplete')):
    print('PerlにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find_all('`...`', 'qx/.../')):
    print('PerlにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find_all('open(h, "|{command}")','open(h, "{command}|"))')):
     print('PerlにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find_all('exec()','passthru()')):
    print('PerlにOSコマンド・インジェクションの脆弱性あり')#ここまでPerl
elif(soup.find_all('os.system()','os.popen()')):
    print('PythonにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find_all('proc_open()','shell_exec()','system()')):
    print('PythonにOSコマンド・インジェクションの脆弱性あり')#ここまでPython
elif(soup.find_all('exec()','system()','`...`')):
    print('RubyにOSコマンド・インジェクションの脆弱性あり')
elif(soup.find_all('open("|{command}", mode, perm)','open("|-{command}", mode, perm)')):
    print('RubyにOSコマンド・インジェクションの脆弱性あり')#ここまでRuby
elif(soup.find_all('$','<','>','*')):
    print('特殊文字を検出、OSコマンド・インジェクションの可能性あり')
elif(soup.find_all('?','{','}')):
    print('特殊文字を検出、OSコマンド・インジェクションの可能性あり')
elif(soup.find_all('[',']','!')):
    print('特殊文字を検出、OSコマンド・インジェクションの可能性あり')
else:
    print('OSコマンド・インジェクションの脆弱性は見つかりませんでした')