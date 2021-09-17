FROM nginx:1.21.3-alpine
#delete existed conf file
RUN rm /etc/nginx/conf.d/default.conf
# copy your own nginx conf file
COPY nginx.conf /etc/nginx/conf.d
