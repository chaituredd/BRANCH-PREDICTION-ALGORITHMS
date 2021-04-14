#statictaken
import os
# f = open("traces/trace_01", "r")
# count_one=0
# count_zero=0
basepath = 'traces/'
for filename in os.listdir(basepath):
   with open(os.path.join(basepath, filename), 'r') as f: # open in readonly mode
      # do your stuff
    count_one=0
    count_zero=0
    #f = open(entry, "r")
    for x in f:
        a = x.split();
        if (a[1]=='1'):
            count_one+=1
        else:
            count_zero+=1

   # print(filename,count_one,count_zero,count_one+count_zero)   
    
    prediction=(count_one/(count_one+count_zero))*100   
    print(filename,"prediction_accuracy=",prediction)
    3
    
    #static not_taken
    import os
basepath = 'traces/'
for filename in os.listdir(basepath):
   with open(os.path.join(basepath, filename), 'r') as f:
    count_one=0
    count_zero=0
    for x in f:
        a = x.split();
        if (a[1]=='1'):
            count_one+=1
        else:
            count_zero+=1

    
    
    prediction=(count_zero/(count_one+count_zero))*100   
    print(filename,"prediction_accuracy=",prediction)
