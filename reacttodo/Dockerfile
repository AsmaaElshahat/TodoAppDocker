FROM node:16-alpine

WORKDIR /app/frontend/

COPY package*.json /app/frontend/
RUN npm install

COPY . /app/frontend/

# port where the Django app runs  
EXPOSE 3000

CMD ["npm", "start"]