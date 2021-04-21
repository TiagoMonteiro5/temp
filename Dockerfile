FROM python:3 
COPY . /recommendations
WORKDIR /recommendations
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
EXPOSE 8080
RUN ./cloud_sql_proxy -instances=cn2021-steam-reviews:europe-west2:teste -dir=/cloudsql &
CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "8080"]
CMD ["review.py"]