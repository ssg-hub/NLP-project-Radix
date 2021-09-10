'''
Created on Sep 8, 2021

@author: Shilpa Singhal
'''
import pandas as pd
import gradio as gr


def start(name):
    a = "Hello Team Radix and " + name +"! "
    b = "Welcome to the CV Mining and Matching Project "
    c = "                          by Pauwel and Shilpa"
    return a+b+c

face = gr.Interface(fn=start, inputs="text", outputs='textbox')
face.launch(share = True)

#########################################
'''def frame(saved_df ):
    df_pkl = pd.read_pickle(saved_df)
    return df_pkl

iface = gr.Interface(frame,
    inputs=None,
  [ gr.outputs.Dataframe(headers=["name", "age", "gender"],\
       datatype=["str", "str", "str"], row_count=5)  ],

  #description="Enter gender as 'M', 'F', or 'O' for other."
)

iface.test_launch()'''