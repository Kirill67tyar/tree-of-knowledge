# from pprint import pprint as pp
# import re
# import sys
# from re import findall, search
#
# help(re)
# print('-+'*50)
# print(re.__doc__)

"""
Sample Input:

catcat
cat and cat
catac
cat
ccaatt

Sample Output:

catcat
cat and cat
"""


# 3.2.7
# answer = []
# for line in sys.stdin:
#     line = line.rstrip()
#     # if line.find('cat') != -1:
#     #     if line.count('cat') >= 2:
#     #         answer.append(line)
#     # or
#     if len(findall(r'cat', line)) >= 2:
#         answer.append(line)
# print(*answer, sep='\n')
#
#
# 3.2.8
# answer = []
# for line in sys.stdin:
#     line = line.rstrip()
#     # if line.find('cat') != -1:
#     #     if line.count('cat') >= 2:
#     #         answer.append(line)
#     # or
#     if search(r'\bcat\b', line):
#         answer.append(line)
# print(*answer, sep='\n')
#
# 3.2.9
# answer = []
# for line in sys.stdin:
#     line = line.rstrip()
#     # if line.find('cat') != -1:
#     #     if line.count('cat') >= 2:
#     #         answer.append(line)
#     # or
#     if search(r'z.{3}z', line):
#         answer.append(line)
# print(*answer, sep='\n')



# 3.2.10
# import sys
# from re import findall, search
# answer = [line.rstrip() for line in sys.stdin if findall(r'\\', line)]
# print(*answer, sep='\n')


# # 3.2.11
# import sys
# from re import findall, search
# answer = [line.rstrip() for line in sys.stdin if findall(r'\b(\w+)\1\b', line)]
# print(*answer, sep='\n')


# # 3.2.13
# import sys
# from re import IGNORECASE, sub
# answer = [sub(r'\b([aA])+\b', 'argh', line, count=1, flags=IGNORECASE).strip() for line in sys.stdin]
# print(*answer, sep='\n')


# # 3.2.14
# import sys
# from re import IGNORECASE, sub
# # answer = [sub(r'\b(\w)(\w)(\w+)', r'\2\1\3', line, flags=IGNORECASE).strip() for line in sys.stdin]
# answer = [sub(r'\b(\w)(\w)+?', r'\2\1', line, flags=IGNORECASE).strip() for line in sys.stdin]
# print(*answer, sep='\n')


# # 3.2.15
# import sys
# from re import IGNORECASE, sub, findall
# answer = []
# for line in sys.stdin:
#     if findall(r'(\w)\1+', line):
#         answer.append(sub(r'(\w)\1+', r'\1', line.strip()))
#     else:
#         answer.append(line.strip())
# print(*answer, sep='\n')

from pprint import pprint as pp
from re import findall, search
import requests


def find_urls(response) -> list:
    all_urls = []
    # pattern = r'hrefs*=s*("([^"]*")|\'[^\']*\'|([^\'">s]+))' # не проходит 3й
    # pattern = r'href=("([^"]*")|\'[^\']*\'|([^\'">s]+))' # не проходит 3й
    pattern = r'a href=("([^"]*")|\'[^\']*\'|([^\'">s]+))' # не проходит 2й и 3й
    # pattern = r'<as*\w*\W*s*hrefs*=s*("([^"]*")|\'[^\']*\'|([^\'">s]+))'
    # pattern = r'<as*[\w\W*]s*hrefs*=s*("([^"]*")|\'[^\']*\'|([^\'">s]+))'
    # pattern = r'<as*("([^"]*")|\'[^\']*\'|([^\'">s]+))s*hrefs*=s*("([^"]*")|\'[^\']*\'|([^\'">s]+))'
    # pattern = r"href\s*=\s*(?:[""'](?<1>[^""']*)[""']|(?<1>[^>\s]+))"
    # pattern = r'<href=\".+\">[0-9]</a>'
    links = findall(pattern, response.text)
    # links = findall(pattern, response)
    if links:
        for item in links:
            urls = map(lambda s: s.replace('"', ''), map(lambda s: s.replace("'", ''), item))
            urls = set(filter(bool, urls))
            all_urls.extend(urls)
    return all_urls

def parser_for_domain(url):
    url_parts = url.split('/')
    if len(url_parts) == 1:
        if url_parts[-1].find('.') != -1:
            if url_parts[-1].find(':') == -1:
                return url_parts[-1]
            return url_parts[-1].split(':')[0]
        return ''
    else:
        domain = list(filter(lambda x: x.find('.') != -1, url_parts))
        if len(domain) == 1 and len(domain[-1]) > 2:
            if domain[-1].find(':') == -1:
                return domain[-1]
            return domain[-1].split(':')[0]
        else:
            level_up_domains = ['ru', 'org', 'com', 'ua', 'ge',]
            domain = list(filter(lambda x: x.split('.')[-1] in level_up_domains, domain))
            if domain:
                if len(domain) == 1:
                    if domain[-1].find(':') == -1:
                        return domain[-1]
                    return domain[-1].split(':')[0]
                else:
                    if domain[0].find(':') == -1:
                        return domain[0]
                    return domain[0].split(':')[0]
            return ''

url = input()
# url = 'http://pastebin.com/raw/7543p0ns'
# url2 = 'http://pastebin.com/raw/hfMThaGb'
response = requests.get(url=url)
result = []
if response.status_code == 200:
    urls = find_urls(response)
    result = list(set(filter(bool, map(parser_for_domain, urls))))


result.sort()
print(*result, sep='\n')
print(len(result))
# with open('dependecies/my_example.txt', 'w') as file:
#     file.write('\n'.join(result))
#
# # это для теста, не для задания
# with open('dependecies/my_example.txt', 'r') as my_example, open('dependecies/right_example.txt', 'r') as right_example:
#     file1 = my_example.read().splitlines()
#     file2 = right_example.read().splitlines()
#     print(len(file1))
#     print(len(file2))
#     print(set(file1).difference(file2))
#     print(set(file2).difference(file1))

# urls = """
# <a href="http://stepic.org/courses">
# <a href='https://stepic.org'>
# <a href='http://neerc.ifmo.ru:1345'>
# <a href="ftp://mail.ru/distib" >
# <a href="ya.ru">
# <a href="www.ya.ru">
# <a href="../skip_relative_links">
# """
# urls = find_urls(urls)
# output = list(set(filter(bool, map(parser_for_domain, urls))))
# output.sort()
# print(*output, sep='\n')

"""
mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""
