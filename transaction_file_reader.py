import dataclasses
from typing import List


@dataclasses.dataclass
class Transaction:
    txid: str
    fee: float
    weight: float
    parent_ids: List[str]


class TransactionFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_transactions(self):
        with open(self.file_path) as file:
            for line in file:
                line_parts = line.strip().split(",")
                print(line_parts)
                transaction = Transaction(
                    txid=line_parts[0],
                    fee=float(line_parts[1]),
                    weight=float(line_parts[2]),
                    parent_ids=[line_parts[3]]
                )
                print(transaction)


if __name__ == '__main__':
    TransactionFileReader("mempool.csv").get_transactions()
