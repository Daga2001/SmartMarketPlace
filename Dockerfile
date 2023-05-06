 FROM node 
 RUN mkdir /smp-front
 WORKDIR /smp-front 
 COPY package.json . 
 RUN npm i --force
 COPY . . 
 EXPOSE 4000 
 CMD ["npm", "run", "dev"] 