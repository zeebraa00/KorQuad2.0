#!/usr/bin/env python
# coding: utf-8

# In[35]:


import json
import pandas as pd


# ## KorQuad 1.0

# In[36]:


corpus_fname_01 = "..//Data/input/KorQuAD_v1.0_train.json"
output_fname_01 = "../Data/output/korquad_v01.txt"


# In[37]:


with open(corpus_fname_01) as f1, open(output_fname_01, 'w', encoding ='utf-8') as f2:
    dataset_json = json.load(f1)
    dataset = dataset_json['data']
    for article in dataset:
        w_lines = []
        for paragraph in article['paragraphs']:
            w_lines.append(paragraph['context'])
            for qa in paragraph['qas']:
                q_text = qa['question']
                for a in qa['answers']:
                    a_text = a['text']
                    w_lines.append(q_text + " " + a_text)
        for line in w_lines:
            f2.writelines(line + '\n')


# In[38]:


dataset[0]


# In[39]:


w_lines


# ## KorQuad 2.0

# In[40]:


corpus_fname_02 = "../Data/input/korquad2.1_train_00.json"
output_fname_02 = "../Data/output/processed_korquad_train_00.txt"


# In[41]:


with open(corpus_fname_02) as f1, open(output_fname_02, 'w', encoding ='utf-8') as f2:
    dataset_json_02 = json.load(f1)
    dataset_02 = dataset_json_02['data']
    for article in dataset_02:
        w_lines = []
        '''for paragraph in article['paragraphs']:
            w_lines.append(paragraph['context'])
            for qa in paragraph['qas']:
                q_text = qa['question']
                for a in qa['answers']:
                    a_text = a['text']
                    w_lines.append(q_text + " " + a_text)'''
        for line in w_lines:
            f2.writelines(line + '\n')
                    


# In[42]:


dataset_02 = dataset_json_02['data']


# In[43]:


dataset_json_02.keys()


# In[44]:


dataset_json_02['data'][0]


# In[45]:


dataset_json_02['data'][1]


# In[46]:


len(dataset_json['data'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




