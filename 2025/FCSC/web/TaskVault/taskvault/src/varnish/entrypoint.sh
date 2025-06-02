/bin/cat > /etc/varnish/default.vcl << EOF
vcl 4.0;

backend default {
    .host = "taskvault-apache2";
    .port = "8000";
}

backend flag_backend {
    .host = "taskvault-app";
    .port = "1337";
}

sub vcl_backend_fetch {
    if (bereq.http.host == "give_me_the_flag") {
        set bereq.backend = flag_backend;
    } else {
        set bereq.backend = default;
    }
}

sub vcl_recv {
    if (req.url == "/" || req.url == "/favicon.jpeg") {
        set req.http.X-Admin-Key = "${ADMIN_KEY}";
    }
    return(pass);
}

sub vcl_backend_response {
    set beresp.do_esi = true;
}
EOF

exec varnishd -F -a :8000 -s malloc,256m -f /etc/varnish/default.vcl
