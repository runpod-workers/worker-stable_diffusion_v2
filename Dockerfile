FROM runpod/pytorch:3.10-2.0.0-117

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

WORKDIR /

# Install Python dependencies (Worker Template)
COPY builder/requirements.txt /requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /requirements.txt && \
    rm /requirements.txt

# Fetch the model
COPY builder/model_fetcher.py /model_fetcher.py
RUN python /model_fetcher.py --model_url https://huggingface.co/SG161222/Realistic_Vision_V3.0
RUN rm /model_fetcher.py

# Add src files (Worker Template)
ADD src .

CMD [ "python", "-u", "/rp_handler.py" ]
