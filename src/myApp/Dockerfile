#Download Node Alpine image
FROM node:18.18.0-alpine As build

#Setup the working directory
WORKDIR /app

#Copy package.json
COPY package.json package-lock.json ./

#Install dependencies
RUN npm install

#Copy other files and folder to working directory
COPY . .

#Build Angular application in PROD mode
RUN npm run build

#Download NGINX Image
# Stage 2
FROM nginx:1.25.2-alpine 

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

#Copy built angular files to NGINX HTML folder
COPY --from=build /app/dist/* /usr/share/nginx/html/
