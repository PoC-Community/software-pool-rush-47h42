FROM node:alpine3.17
ENV FRONTEND=docker
WORKDIR /app
COPY package*.json ./
# RUN apk add
RUN npm install
RUN npm install react-webcam
COPY . .
RUN npm run build
ENTRYPOINT ["npm", "run", "start"]
# CMD ["start"]