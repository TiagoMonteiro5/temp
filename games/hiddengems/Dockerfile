FROM python:3 
COPY . /hidden_gems 
WORKDIR /hidden_gems
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"] 
CMD ["hiddengems.py"] 
