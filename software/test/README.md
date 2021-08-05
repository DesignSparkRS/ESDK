# Python examples for testing peripherals

The simple examples in this directory are for use in testing peripherals and to
aid development.

## Installation

### Initial

This only needs to be done once.

Create a file called .ssh/id_rsa with contents:

```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAQEAwbzLYeLcTp90smS1UQfcEXOXRFdhFziPwlHlvv68l0ATUJlBMFuH
UhJ9ZsJPhCtZawSbJH8RQ/rG/XE+ifx2LnPCP5m7NKqzpQlTrAUDqX+EB/WDR6Z3HsJ/mo
ecSHyU+i/plErQlhVq5DZXBj9yi35aqSwa3zkeLNF9IQnFH2THV14GzMGWRY30RyqorujG
Jg23HeyfGaxKHjQP7a0DB8vz0gbJk5fIwtfa5TwycibNaMcJ89J1C9vwEtgMMS9YxWeYmS
IDMtHeFSv7uyPCyXb9fJKu3D2Hqk1JNV2EgGC8i0kFItL/iirJSVkTBSuSKr7jsKBJxVtx
BTJNI8neeQAAA8B98ghFffIIRQAAAAdzc2gtcnNhAAABAQDBvMth4txOn3SyZLVRB9wRc5
dEV2EXOI/CUeW+/ryXQBNQmUEwW4dSEn1mwk+EK1lrBJskfxFD+sb9cT6J/HYuc8I/mbs0
qrOlCVOsBQOpf4QH9YNHpncewn+ah5xIfJT6L+mUStCWFWrkNlcGP3KLflqpLBrfOR4s0X
0hCcUfZMdXXgbMwZZFjfRHKqiu6MYmDbcd7J8ZrEoeNA/trQMHy/PSBsmTl8jC19rlPDJy
Js1oxwnz0nUL2/AS2AwxL1jFZ5iZIgMy0d4VK/u7I8LJdv18kq7cPYeqTUk1XYSAYLyLSQ
Ui0v+KKslJWRMFK5IqvuOwoEnFW3EFMk0jyd55AAAAAwEAAQAAAQEAvCvJRuv3mw3ZZKPY
UDnYD8M7uw87qDgxuUWeZmI5fpanq/MOlA9yYc6/qh006mTIVt+EaHBarrJWsDdbzN4/U2
Lv2qJQaBkcn0Ft2XiNVAYckTZvKhqPPHshQVBSBT2r3UzIDFaWPg/TYJE++TyK3t385K+H
8iQiINngNUSuB4xDSWeMpiw916rb3z2WnC3Fz/ir0MFYE7c6CywLl0hXD5R0uc21U2WwvW
pduY8oYcm6HSRW1RDbDDImm0UtWUVP15FyPphe8ANYZjv4h1PwZ2txyLzkwe/ORTqjaQAb
YYAbuX6etbuVy5fs9NvSJ+AvdpDoZgNYUr8IOdDGp70gWQAAAIEAipXGVAd/r86+6L0uig
Kv+hxk1LE/5J4uplSGOzFq3vwf9KaYofhrgVclLB5NQ6keCpC5NgLWwsXI+QhQnlm/P4Xd
MWoORBtbrQcNOarW7RA1EwH590hj286gMY/i/v/haNhuXPJx4E5S/dqDPJpUn6wO4yU+QN
6lYmC2mUyL9QYAAACBAO5y//E611vM+4bB0yi6Zo3Zopri8bbUDGBJFxSVaMwyG1yHY3w2
+pltT2k6DMwqG8StIqBwwjbzENeBHeadB4FkGLdoK73MXtV+WyenoYpIsj2dKp+AAS7Ino
cTbvs5fJAK9oGH7kTSlnbiWWRDqew7fokhK4HbhyR66hjeUs7TAAAAgQDP/09Q8rb3mxmP
amwj15ERdzETz6jFncrHMhRXDR/fUmn9+UCOStmTKEiv0B4Gnc9yyGfJ2/YXvcS46RBtQJ
8Sz1RsIE874hnICKdYWJmvRIPyQ66QLGH9aCqDSD6uE9NFANkIUjYbcX1U1hu79unvQ5X5
B4fFLaFjSrG7mdWGAwAAAAdwaUBhYnBpAQI=
-----END OPENSSH PRIVATE KEY-----
```

Then execute the following commands:

```
$ sudo apt update && sudo apt dist-upgrade

$ sudo apt install git

$ git@github.com:DesignSparkrs/ESDK.git

$ cd ESDK/software/test

$ python3 -m venv venv

### Updating

