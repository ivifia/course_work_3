from src.utils import request
from src.func import executed, card ,check
from datetime import datetime
def main():
    for op in executed():
        date = datetime.fromisoformat(op["date"]).strftime("%d.%m.%Y")
        description = op.get("description", '')
        from_account = op.get("from", '')
        to_account = op.get("to", '')

        if 'Счет' in from_account:
            from_account = f"{check(from_account)}"
        else:
            from_account = card(from_account)

        if 'Счет' in to_account:
            to_account = f"счет {check(to_account)}"
        else:
            to_account = card(to_account)

        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']

        if op["description"] == "Открытие вклада":
            print(f"{date} {description}"
        f"-> {to_account}\n"
        f"{amount} {currency}")
        else:
            print(f'''{date} {description}
        {from_account} -> {to_account}
        {amount} {currency}
        ''')

main()