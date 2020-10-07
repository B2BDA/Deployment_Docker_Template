FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 8080
WORKDIR /usr/app/
RUN pip install Flask
RUN pip install numpy
RUN pip install pandas
RUN pip install -U scikit-learn scipy matplotlib
CMD python app.py