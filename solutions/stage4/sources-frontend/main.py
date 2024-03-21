# Imports
import os
import gradio as gr
from celery import Celery
from celery.result import AsyncResult
# Celery configuration (global)
CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]  # 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
CELERY_RESULT_BACKEND = os.environ["CELERY_RESULT_BACKEND"]  # 'rpc://'
# Initialize Celery
celeryapp = Celery(broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
celeryapp.config_from_object('celeryconfig')

# In some function, for task submission
def process_image_proxy(image):
    task_id = celeryapp.send_task('worker.process_image', args=(image,), serializer="pickle")
    generated_text = AsyncResult(task_id, app=celeryapp).get()
    return generated_text

title = "Interactive demo: TrOCR"
description = "Demo for Microsoft's TrOCR, an encoder-decoder model consisting of an image Transformer encoder and a text Transformer decoder for state-of-the-art optical character recognition (OCR) on single-text line images. This particular model is fine-tuned on IAM, a dataset of annotated handwritten images. To use it, simply upload an image or use the example image below and click 'submit'. Results will show up in a few seconds."
article = "TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models | Github Repo"
examples =[["image_0.png"], ["image_1.png"], ["image_2.png"]]

iface = gr.Interface(fn=process_image_proxy,
                     inputs=gr.Image(type="pil"),
                     outputs=gr.Textbox(),
                     title=title,
                     description=description,
                     article=article,
                     examples=examples)
iface.launch(server_name="0.0.0.0", debug=True)