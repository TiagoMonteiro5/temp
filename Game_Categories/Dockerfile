FROM python:3
COPY . /game_categories
WORKDIR /game_categories
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["game_categories"]