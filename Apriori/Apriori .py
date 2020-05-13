#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#A priori Algorithm


# In[11]:


tid=[['i1','i2','i3'] ,['i2','i4'],['i2','i3'] ,['i1','i2','i3']]
import pandas as pd
#converting the given tid into dataframe, in order to use the apriori method
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(tid).transform(tid)
df = pd.DataFrame(te_ary, columns=te.columns_)
from mlxtend.frequent_patterns import apriori
#apriori(df, min_support=0.6)
apriori(df, min_support=0.6, use_colnames=True)
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
frequent_itemsets
#requent_itemsets[ (frequent_itemsets['length'] == 2) & (frequent_itemsets['support'] >= 0.8) ]


# In[ ]:




