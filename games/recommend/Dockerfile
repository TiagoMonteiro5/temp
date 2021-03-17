FROM python:3 
COPY . /recommendations
WORKDIR /recommendations
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"] 
CMD ["recommend.py"] 
