clockface={':':
"""
  ###  
  ###  
       
  ###  
  ###  
""",'1':
"""
 ##
 ##
 ##
 ##
 ##
""",'2':
"""
 ##### 
ddddd# 
 ##### 
 #     
 ##### 
""",'3':
"""
 ##### 
    ## 
  #### 
    ## 
 ##### 
""",'4':
"""
 #   # 
 #   # 
 ##### 
     # 
     # 
""",'5':
"""
 ##### 
 #     
 ##### 
     # 
 ##### 
""",'6':
"""
 ##### 
 #     
 ##### 
 #   # 
 ##### 
""",'7':
"""
###### 
    ## 
   ##  
  ##   
  ##   
""",'8':
"""
 ##### 
 #   # 
 ##### 
 #   # 
 ##### 
""",'9':
"""
 ##### 
 #   # 
 ##### 
     # 
 ##### 
""",'0':
"""
 ##### 
 #   # 
 #   # 
 #   # 
 ##### 
""",'Z':
"""
#######
#  ### 
  ###  
 ###   
#######
"""}
from datetime import datetime
lines ={}
for char in datetime.now().strftime("%H:%M"):
	for n, line in enumerate(clockface[char].split("\n")):
		if n in lines:
			lines[n] += line.replace("#", "█")
		else:
			lines[n] = line.replace("#", "█")
print("\n".join([text for key, text in lines.items()]))