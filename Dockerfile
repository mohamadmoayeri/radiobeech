# start from an official image
FROM python:3.8

# arbitrary location choice: you can change the directory
RUN mkdir  /radio
WORKDIR /radio


# copy our project code
COPY . /radio

ADD requirements.txt /radio

RUN pip3 install -r requirements.txt


# define the default command to run when starting the container
CMD ["gunicorn","--chdir","radiobeech", "--bind", ":8000", "radiobeech.wsgi:application"]