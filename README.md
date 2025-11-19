
Population Equilibrium Calculator

Calculates the steady-state equilibrium for a population using two methods:

    balans: A direct calculation for simple 2-state models.

    balans_2: An iterative Markov Chain solver for N-state models.

1. balans (2-State Model)

Provides a direct answer given initial numbers and transition rates.
Python

# Args: healthy_num, sick_num, falling_sick_rate, getting_healthy_rate
healthy, sick = balans(150, 120, 0.2, 0.1)

print(f"Equilibrium: {healthy:.0f} healthy, {sick:.0f} sick")
# Output: Equilibrium: 90 healthy, 180 sick



2. balans_2 (N-State Model)

This interactive function prompts for:

    Number of states (N)

    Initial population for each state

    An N x N Transition Matrix

The Transition Matrix [row i, col j] is the probability of moving from state i to state j. Each row must sum to 1.

Example (Replicating Method 1)

    State 1: Healthy

    State 2: Sick

    falling_sick_rate = 0.2

    getting_healthy_rate = 0.1

Inputs:

    States: 2

    Populations: 150 (state 1), 120 (state 2)

    Matrix Row 1 (from Healthy): 0.8 0.2

        (Prob. Healthy -> Healthy = 1.0 - 0.2 = 0.8)

    Matrix Row 2 (from Sick): 0.1 0.9

        (Prob. Sick -> Sick = 1.0 - 0.1 = 0.9)

Output:

Final distribution: [90.0, 180.0]
