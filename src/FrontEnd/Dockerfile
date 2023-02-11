FROM node:alpine3.17
WORKDIR /app
COPY . .
ENV FRONTEND=docker
RUN npm install
RUN npm run build --prefix ./
ENTRYPOINT ["npm", "run", "start"]