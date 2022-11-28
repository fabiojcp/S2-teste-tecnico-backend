from transactions.models import Transaction

def normalize_file_txt(file) -> dict:
    decode_file = file.read().decode("utf-8")
    split_file = decode_file.split("\r\n")

    for line in split_file:
        data = {
            "tipo": line[0],
            "data": f"{line[1:5]}-{line[5:7]}-{line[7:9]}",
            "valor": round(int(line[9:19]) / 100, 2),
            "ssn": line[19:30],
            "card": line[30:42],
            "hora": f"{line[1:5]}-{line[5:7]}-{line[7:9]} {line[42:44]}:{line[44:46]}:{line[46:48]}",
            "emissor": line[48:62].strip(),
            "loja": line[62:].strip(),
        }

        Transaction.objects.create(**data)

