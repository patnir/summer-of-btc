# summer-of-btc

Steps so far: 

#### Data cleaning

Eliminated transactions that had parents that came after them in the block - result in `earlier_parent_filtered_transactions.csv`

#### First solve a small part of the problem 

Going to first tackle just solving the _maximize_ `fee` for the _minimum_ `weight` problem 

#### Knapsack

Recognized that this was the knapsack problem and solved it dynamically with a 2D array for a small case - `earlier_parent_filtered_transactions_reduced.csv`

#### Scale issues

As I was trying to solve the larger case, my personal computer was running out of memory and timing out. So I created a beefy EC2 instance to run the code on.
Recognized that the memory was still going to be an issue and see if I could solve this recursively instead

