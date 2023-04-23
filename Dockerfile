 FROM node 
 WORKDIR /smp-front 
 COPY package.json . 
 RUN npm i --force
 COPY . . 
 EXPOSE 5173 
 CMD ["npm", "run", "dev"] 