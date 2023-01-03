# only run this in development!

FROM node:19 as builder

WORKDIR /usr/src/app

ADD package.json package-lock.json tsconfig.json tsconfig.node.json tailwind.config.cjs postcss.config.cjs vite.config.ts openapitools.json ./

RUN npm install

ENTRYPOINT npm run dev