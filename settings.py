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
 b  ## 
 ##### 
 ##    
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
 ##  ##
 ##  ##
 ######
     ##
     ##
""",'5':
"""
 ##### 
 ##    
 ##### 
    ## 
 ##### 
""",'6':
"""
 ##### 
 ##    
 ##### 
 ## ## 
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
 ## ## 
 ##### 
 ## ## 
 ##### 
""",'9':
"""
 ##### 
 ## ## 
 ##### 
    ## 
 ##### 
""",'0':
"""
 ##### 
 ## ## 
 ## ## 
 ## ## 
 ##### 
""",'Z':
"""
#######
#  ### 
  ###  
 ###   
#######
"""}
tasks={}
schedule={}
from notify import error
def readsettings(filename, Veridis):
	try:
		tasks = open(filename)
		t=tasks.read().rstrip("}").split("\n")
		tasks.close()
		Aliases={}
		def addAlias(fromToList):
			Aliases[fromToList[0]] = fromToList[1]
		t = [dict([[(Aliases[a] if a in Aliases else a) for a in list(value.split(":"))] for value in task.split(";")]) for task in "".join([val for val in [(addAlias(line.split(" ")[1:3]) if not line.find("Alias") else line) for line in t] if not val == None]).split("}")]
		return t
	except IOError as e:
		error("Could not read %s, aborting." % (filename))
		Veridis.running = False
		return False
