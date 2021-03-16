FROM python:3 
COPY . /bestgames 
WORKDIR /bestgames
RUN pip install -r requirements.txt 
ENTRYPOINT ["python"] 
CMD ["games.py"] 
