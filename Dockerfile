FROM python:3-onbuild
COPY * /
RUN pip3 install -r requirements.txt
CMD [ "python", "./main.py" ]