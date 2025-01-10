FROM cgr.dev/chainguard/node:latest-dev as base
ENV NODE_ENV=development
 
WORKDIR /dev-app
 
COPY --chown=node:node package.json .

ADD ./src ./src

RUN npm install

# lint and test
# FROM base as lint-and-test

# RUN npm run lint

# RUN npm run test

# build
# FROM test as build
# RUN npm run build

# prod package installations
FROM base as prod-dependency-installations
ENV NODE_ENV=production
WORKDIR /prod-app

COPY --chown=node:node package.json .

RUN npm install --ignore-scripts

FROM cgr.dev/chainguard/node:latest
WORKDIR /app

# copy dist directory
# COPY --from=build /dev-app/dist ./

COPY --from=prod-dependency-installations /prod-app/node_modules ./node_modules

COPY --chown=node:node package.json .

ADD ./src ./src
 
# CMD ["node", "dist/server.js"]

ENTRYPOINT ["npm", "run", "start"]