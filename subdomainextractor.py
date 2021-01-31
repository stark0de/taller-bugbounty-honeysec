import re
import sys
 
with open(sys.argv[1]) as file:
        for line in file:
            urls = re.findall('[a-zA-Z0-9.]+\.[a-zA-Z0-9.]+\.[a-zA-Z0-9.]+', line)
            if len(urls) > 0:
               print(urls[0])
                
