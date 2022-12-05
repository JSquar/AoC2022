#!/usr/bin/env python
# coding: utf-8

# In[40]:


from pathlib import Path
from collections import deque


# In[41]:


debug = False
#inputfile = Path("input_small.txt")
inputfile = Path("input_big.txt")

fh = open(inputfile, "r")
data = fh.readlines()
fh.close()


# In[42]:


split_index = data.index("\n")
towers = data[:split_index]
movement_text = data[split_index + 1:]
#columns = towers[-1].split()


# In[ ]:





# In[43]:


data_stacks = []
for i in range(int((len(towers[-1]) + 1) / 4)):
    data_stacks.append(deque())
    
for row in range(len(towers)-2, -1, -1):
    for column in range(3):
        entry = towers[row][3*column+column:4*(column+1)]
        if(entry[:3] != " "*3):
            data_stacks[column].append(entry)


# In[44]:


movement = [x.split() for x in movement_text]


# In[45]:


#movement


# In[46]:


# perform movement
for action in movement:
    num_blocks = int(action[1])
    from_column = int(action[3])-1
    to_column = int(action[5])-1
    for block in range(num_blocks):
        if debug:
            print(f"Move {num_blocks} from {from_column} to {to_column}")
            print(f"BEFORE: from column content: {data_stacks[from_column]}")
            print(f"BEFORE: to column content: {data_stacks[to_column]}")
        current = data_stacks[from_column].pop()
        data_stacks[to_column].append(current)
        if debug:
            print(f"AFTER: from column content: {data_stacks[from_column]}")
            print(f"AFTER: to column content: {data_stacks[to_column]}")
#print(data_stacks)        


# In[ ]:




