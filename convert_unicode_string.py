#& C:/Python311/python.exe c:/Users/master/Project/python/deletme/convert_unicode_string.py \uc644\ub8cc
import sys

if len(sys.argv) > 1 : 
    arg = sys.argv[1]
else:
    print('변환할 문자열이 없습니다.!')
    arg = ''

arg = arg.replace("\\u",'\\\\u')
result = arg.encode().decode("unicode-escape").encode().decode("unicode-escape")
print(result)