# Vietnamese-checker

## Knowledge about Vietnamese
[Vietnamese document](Vietnamese_rule.vn.md)

## Vietnamese-checker API

### POST

POST: https://vietnamese-checker.vercel.app/

Input format:
```json
{
    "text": "Việt" // or any word you want to check
}
```

Output format:
```json
{
    "result": true // or false
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
To run demo api you need install enviroment first
```
pip install -r requirements.txt
```
Then run
```
python app.py
```
