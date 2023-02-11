FROM node:
ENV BACKEND=docker
EXPOSE 8080
WORKDIR /app
COPY package*.json ./
# RUN apk add
RUN npm install
COPY . .

RUN npm run build
ENTRYPOINT ["npm", "run", "start"]
# CMD ["start"]