# base image  
FROM python:3.10-bullseye

# setup environment variable  
ENV DockerHOME=/home/app/webapp  

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# copy whole project to your docker home directory. 
COPY . $DockerHOME 
 
# run this command to install all dependencies  
RUN pip install -r requirements.txt 

# run this command to install all dependencies  


# run this command to install all dependencies  

# port where the Django app runs  
EXPOSE 8000  

# start server  
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]