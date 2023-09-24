server {
    listen ${LISTEN_PORT};

    location /static {
        alias /vol/web;
    }

    location / {
        include /etc/nginx/headers.conf;

        # we don't want nginx trying to do something clever with
        # redirects, we set the Host: header above already.
        proxy_redirect        off;
        proxy_pass            http://${APP_HOST}:${APP_PORT};
        client_max_body_size  10M;
    }
}
