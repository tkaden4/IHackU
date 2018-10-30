# Staff

## Setup
```Bash
gunicorn -w 4 0.0.0.0:<PORT> stolen:create_app
```

## Solution

```Bash
curl -H "Authorization: Basic <PROVIDED_CREDENTIALS>" <CHALLENGE_URL>:<PORT>
```
... or any other method that lets you set the Authorization header.

Key: ihacku{challenge-completed}
