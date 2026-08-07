# Resmi postgres imajı sadece en_US.UTF-8 locale'ini üretiyor (docker-library
# postgres Dockerfile'ında böyle geliyor). Bizim collation/ctype için
# tr_TR.UTF-8 lazım, o yüzden üstüne kendi locale'imizi ekliyoruz.
FROM postgres:16

RUN localedef -i tr_TR -c -f UTF-8 -A /usr/share/locale/locale.alias tr_TR.UTF-8

ENV LANG=tr_TR.UTF-8
