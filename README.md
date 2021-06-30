# summer-of-btc

Steps so far:

#### Data cleaning

Eliminated transactions that had parents that came after them in the block - result
in `earlier_parent_filtered_transactions.csv`

#### First solve a small part of the problem

Going to first tackle just solving the _maximize_ `fee` for the _minimum_ `weight` problem

#### Knapsack

Recognized that this was the knapsack problem and solved it dynamically with a 2D array for a small case
- `earlier_parent_filtered_transactions_reduced.csv`

#### Scale issues

As I was trying to solve the larger case, my personal computer was running out of memory and timing out. So I created a
beefy EC2 instance to run the code on. Recognized that the memory was still going to be an issue and see if I could
solve this recursively instead

I moved the formula to be recursive and the max depth reached in this case as well.

I'm at time, I've spent a total of 8 hours on this and I'm going to call it. 

## FINALLY a solution

I realized that the key to this was analyzing the ratio between fee and weight. It is pretty obvious then that 
you can get a better block (not sure if the most optimal) by picking the blocks that have the best ratio of fee to weight. 
This only works when all the fee and weight numbers are not miles apart from each other. That would have 
led to various skewed results.

## Feedback from jonas

"Additionally, I looked over your solution, and your solution includes
transactions with unconfirmed parents. 
You'll have to filter those out in order to create a valid block."

This goes againts the readme pdf: 
Transactions with parent transactions in the mempool 
may be included in the list, but only if all of their 
parents appear before them in the list.