# import pandas as pd  
import pandas as pd   
      
# List1   
lst = [['Jeet', 25], ['is', 30],  
       ['Rajveer', 26], ['Simran', 22]]  
  
# creating df object with columns specified     
df = pd.DataFrame(lst, columns =['Tag', 'number'])  ;
print(df ) ;