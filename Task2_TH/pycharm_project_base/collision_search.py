# Your task is to find a collision for a modified version of the SHA-2 hash function.
# We use the SHA-256, which generates a 256-bit output.
# For the exercises, the output of the hash function is truncated to 64 bits using the following
# rule: let h = A∥B∥C∥D∥E∥F∥G∥H the 256-bit output of SHA-256, with A, B, C, D, E, F, G and H being 32-bit chunks.
# The modified hash is computed using a bitwise XOR and aconcatenation: h′ =E⊕F⊕G⊕H∥A⊕B⊕C⊕D.

# Your colliding messages need to start with the same prefix, which is a concatenation of your matriculation
# numbers in ascending order (in standard ASCII encoding). There are no restrictions for the message after this prefix.
# For instance, a group with members 1030123 and 1030456 needs to find colliding messages of form m1 = 10301231030456X and
# m1 = 10301231030456Y , with X ̸= Y and a freely chosen length of X and Y .

# SHA-256("10301231030456") = 0xc899398cd246818ffab4ba8842f3251ac2fc27d690979d1891322345818ff381
# SHA-256-mod("10301231030456") = 0x42d66a0aa2982791
# You should use an existing SHA-2 implementation, do not implement it yourself.
# The memory requirements of your program must not exceed 2GB (RAM and HDD).
# Look for solutions that do not require such a large amount of memory.

# Tip:
# Start off with collision search for smaller hashes, e.g., only the first 32 bits of the hash.
# Expect that the collision search takes some time. Depending on your code and machine, the search can take more than an hour.