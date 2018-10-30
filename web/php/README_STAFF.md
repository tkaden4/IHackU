# Staff

Key: ihacku{php_really_sucks_doesnt_it}

`docker build . -t <NAME> && docker run -p <OUT_PORT>:80 -d <NAME>`


## Solution

With an IV of zero, we can easily decript the DES-encoded parameter.

We then assume we can do path-traversal, so we DES-CBC encode `index.php`
to see what else we have. The key is in the file.
