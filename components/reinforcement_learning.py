import random

import numpy as np


def choose_action(state, Q, exploration_prob):
    """
    Function to choose the action based on epsilon-greedy policy.

    Parameters:
    - state: Current state for which an action needs to be selected.
    - Q: Q-table storing the expected rewards for state-action pairs.
    - exploration_prob: Probability of exploration.

    Returns:
    - The selected action index.
    """

    # Exploration: Randomly choose an action if the state is not in the Q-table
    if state not in Q:
        return random.choice(list(range(len(Q))))  # Explore

    # Exploration vs. Exploitation trade-off
    # With probability 'exploration_prob', explore by choosing a random action
    if np.random.rand() < exploration_prob:
        return random.choice(list(range(len(Q))))  # Explore
    else:
        # Exploitation: Choose the action with the highest expected reward (based on Q-values)
        return np.argmax(Q[state])  # Exploit


def evaluate_response():
    """
    Function to simulate user feedback on the response.

    Returns:
    - 1 for a helpful response, -1 otherwise.
    """
    return 1 if input("Was that response helpful? (yes/no): ").lower() == 'yes' else -1


def update_q_value(state, action, reward, Q, learning_rate, discount_factor):
    """
    Function to update Q-value in the Q-table based on the reward received.

    Parameters:
    - state: Current state.
    - action: Chosen action index.
    - reward: Reward received for the action.
    - Q: Q-table storing the expected rewards for state-action pairs.
    - learning_rate: Rate at which the agent learns from new information.
    - discount_factor: Rate at which future rewards are discounted.

    Returns:
    - None (updates Q-table in place).
    """
    current_q_value = Q[state][action]
    max_future_q_value = np.max(Q[state])
    new_q_value = (1 - learning_rate) * current_q_value + learning_rate * (
            reward + discount_factor * max_future_q_value)
    Q[state][action] = new_q_value


def print_q_table(Q):
    """
    Function to print the Q-table.

    Parameters:
    - Q: Q-table storing the expected rewards for state-action pairs.

    Returns:
    - None (prints the Q-table).
    """
    for state, values in Q.items():
        print(f"State: {state}")
        print("Q-Values:", values)
        print()
