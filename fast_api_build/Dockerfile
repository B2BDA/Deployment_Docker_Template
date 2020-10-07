FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 80
WORKDIR /usr/app/
RUN pip install Flask
RUN pip install numpy
RUN pip install pandas
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install -U scikit-learn scipy matplotlib
CMD ["uvicorn", "fastAPI_test:app", "--host", "0.0.0.0", "--port", "80"]

