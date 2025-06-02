#!/bin/bash

# Define the output file
OUTPUT_FILE="output.txt"

#!/bin/bash

# Define the range for the storage slots
START=0
END=1000000

# Define the contract address and RPC URL
CONTRACT_ADDRESS=0xe553b1Ce75b2A4eFA61C407A93873A0B9Eb92598
RPC_URL=https://blind-guy-171.chall.ctf.bzh/rpc

# Loop through each storage slot and fetch the storage value
for ((i=START; i<=END; i++)); do
  cast storage $CONTRACT_ADDRESS $i --rpc-url $RPC_URL >> $OUTPUT_FILE
done
