
# coding: utf-8

# In[56]:


# ! pip install py-readability-metrics


# In[57]:

from flask import Flask, render_template, request, jsonify
from flask import json
import textstat 


# In[ ]:




# In[98]:



app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def summarize():

    # In[61]:

    data = request.get_json(force=True)
    text = data["text"]

    #text= input()

    #


    


    # In[102]:


    #fk.score


    # In[103]:
    result  = textstat.flesch_reading_ease(text)

    return jsonify([{"result":result}])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
