# Vietnamese-checker

## Knowledge about Vietnamese
[Vietnamese document](Vietnamese_rule.vn.md)

## Vietnamese-checker API

### POST

POST: https://vietnamese-checker.vercel.app/

Input format:
```json
{
    "text": "Việt"
}
```

Output format:
```json
{
    "result": true
}
```

### GET

GET: https://vietnamese-checker.vercel.app/word

Replay 'word' to any word you want to check

Output format:
```json
{
    "result": true // or false
}
```

### Example:
```bash
curl -X POST https://vietnamese-checker.vercel.app/ --header 'Content-Type: application/json' --data '{"text": "Việt"}'
```
```bash
curl https://vietnamese-checker.vercel.app/Việt
```

## For developer
First, install enviroment
```bash
pip install -r requirements.txt
```

To run demo api, use
```bash
python app.py
```

For run and listen all updation, use
```bash
flask --app app.py --debug run
```

___Welcome all pull request ^^___

