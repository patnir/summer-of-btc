"""
blocks - set of transactions

Transaction:
    fee: number
    weight: number
    parent_transactions: Transaction[]
    time: timestamp, probably?

Miner selects Transactions[] Ordered (by time probably) where sum(Transactions.weight)
    < max block weight
    allow Transaction[] where Transaction.parent_transactions.all.timestamps()
        < specific transaction .timestamp

Goal: Miner has a block with the fattest fees lololol

weight of the block must not exceed 4,000,000

I've recognized that this is a variation of the knapsack problem.
source of algo i modified: https://www.geeksforgeeks.org/printing-items-01-knapsack/
"""
import os
import pandas as pd


class KnapsackSolver:
    def __init__(self, weight, transaction_file_path, block_file_path):
        self.transactions = pd.read_csv(transaction_file_path)
        self.max_weight = weight
        self.block_file_path = block_file_path
        self.block = []

    def write_block(self):
        with open(self.block_file_path, "w+") as file:
            for _, item in self.block:
                file.write(f"{item}\n")

    def add_to_block(self, index, tx_id):
        self.block.append((index, tx_id))

    def solve(self):
        self.knapsack(
            self.max_weight,
            self.transactions["weight"],
            self.transactions["fee"],
            len(self.transactions)
        )
        # sorting block
        self.block = sorted(self.block, key=lambda x: x[0])
        print("writing block")
        self.write_block()

    def knapsack(self, weight, weights, fees, total_transactions):
        knapsack_2d_array = [[0 for _ in range(weight + 1)] for _ in range(total_transactions + 1)]
        print("building 2d knapsack array [this takes the longest time]")
        for i in range(total_transactions + 1):
            for weight_index in range(weight + 1):
                if i == 0 or weight_index == 0:
                    knapsack_2d_array[i][weight_index] = 0
                elif weights[i - 1] <= weight_index:
                    knapsack_2d_array[i][weight_index] = \
                        max(fees[i - 1]
                            + knapsack_2d_array[i - 1][weight_index - weights[i - 1]],
                            knapsack_2d_array[i - 1][weight_index])
                else:
                    knapsack_2d_array[i][weight_index] = knapsack_2d_array[i - 1][weight_index]

        res = knapsack_2d_array[total_transactions][weight]
        weight_index = weight

        print("traversing 2d knapsack array")
        for i in range(total_transactions, 0, -1):
            if res <= 0:
                break
            if res == knapsack_2d_array[i - 1][weight_index]:
                continue

            self.add_to_block(
                self.transactions["original_index"][i - 1], self.transactions["tx_id"][i - 1]
            )
            res = res - fees[i - 1]
            weight_index = weight_index - weights[i - 1]


if __name__ == '__main__':
    current_directory = os.getcwd()
    transaction_file = f"{current_directory}/earlier_parent_filtered_transactions_reduced.csv"
    block_file = f"{current_directory}/block.txt"

    KnapsackSolver(400000, transaction_file, block_file).solve()
