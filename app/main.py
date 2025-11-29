from fastapi import FastAPI, Request, HTTPException
import re
from datetime import datetime
from typing import List

app = FastAPI(
    title="Email Validation API",
    description="Simple email validation + domain blocking + logging API",
    version="1.0.0"
)

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

#blocked email domains
BLOCKED_DOMAINS: List[str] = [
    "Blocked.Domains",

]


def is_valid_email(value: str) -> bool:
    return bool(EMAIL_REGEX.match(value))


def is_blocked_domain(value: str) -> bool:
    try:
        domain = value.split("@")[1]
        return domain in BLOCKED_DOMAINS
    except Exception:
        return False


def write_log(ip: str, email: str, status: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a") as f:
        f.write(f"[{timestamp}] IP={ip}, EMAIL={email}, RESULT={status}\n")


@app.get("/validate/email")
async def validate_email(request: Request, value: str):
    ip = request.client.host

    if not is_valid_email(value):
        write_log(ip, value, "INVALID_FORMAT")
        return {"valid": False, "reason": "invalid format"}

    if is_blocked_domain(value):
        write_log(ip, value, "BLOCKED_DOMAIN")
        return {"valid": False, "reason": "blocked domain"}

    write_log(ip, value, "OK")
    return {"valid": True, "reason": "OK"}
