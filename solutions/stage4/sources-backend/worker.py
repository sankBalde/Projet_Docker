import os
from celery import Celery
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

# Celery configuration
CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]  # 'amqp://rabbitmq:rabbitmq@rabbit:5672/'
CELERY_RESULT_BACKEND = os.environ["CELERY_RESULT_BACKEND"]  # 'rpc://'

# Initialize Celery
celery = Celery("worker", broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND) # 'ocr_worker'
celery.config_from_object('celeryconfig')

# Define our OCR task
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

@celery.task()
def process_image(image):
    # prepare image
    pixel_values = processor(image, return_tensors="pt").pixel_values

    # generate (no beam search)
    generated_ids = model.generate(pixel_values)

    # decode
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return generated_text