#Module Search Ordering
'''
1. 동일 diretory안에 있으면 찾을 수 있음
2. sys.path에서 찾음    
'''

import sys
for path in sys.path:
    print(path)