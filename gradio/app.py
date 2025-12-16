import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import gradio as gr
from common.preprocessing import predict_yield

interface = gr.Interface(
    fn=predict_yield,
    inputs=[
        gr.Dropdown(['North','East','South','West']),
        gr.Dropdown(['Clay','Sandy','Loam','Silt','Peaty','Chalky']),
        gr.Dropdown(['Wheat','Rice','Maize','Barley','Soybean','Cotton']),
        gr.Dropdown(['Sunny','Rainy','Cloudy']),
        gr.Slider(0,1000),
        gr.Slider(10,50),
        gr.Checkbox(),
        gr.Checkbox(),
        gr.Slider(30,300)
    ],
    outputs="number",
    title="Crop Yield Prediction"
)

interface.launch()
