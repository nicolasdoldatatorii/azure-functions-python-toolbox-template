FROM pernodricard/pr-python-toolbox-data:azure-functions-python3.6

COPY . /home/site/wwwroot

RUN cd /home/site/wwwroot && \
    pip install -r requirements.txt