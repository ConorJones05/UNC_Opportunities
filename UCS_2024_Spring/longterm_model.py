import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

class State:
    def __init__(self, portfolio_balances, portfolio_rates, portfolio_risks, portfolio_age, debt_balances, debt_rates, penalties_incurred, time_remaining_penalties, inflation_rate):
        self.portfolio_balances = portfolio_balances
        self.portfolio_rates = portfolio_rates
        self.portfolio_risks = portfolio_risks
        self.portfolio_age = portfolio_age
        self.debt_balances = debt_balances
        self.debt_rates = debt_rates
        self.penalties_incurred = penalties_incurred
        self.time_remaining_penalties = time_remaining_penalties
        self.inflation_rate = inflation_rate

    def get_state_representation(self):
        return {
            'portfolio_balances': self.portfolio_balances,
            'portfolio_rates': self.portfolio_rates,
            'portfolio_risks': self.portfolio_risks,
            'portfolio_age': self.portfolio_age,
            'debt_balances': self.debt_balances,
            'debt_rates': self.debt_rates,
            'penalties_incurred': self.penalties_incurred,
            'time_remaining_penalties': self.time_remaining_penalties,
            'inflation_rate': self.inflation_rate,
        }

class ActionSpace:
    def __init__(self, num_portfolios, risk_threshold, allow_merge=True):
        self.num_portfolios = num_portfolios
        self.risk_threshold = risk_threshold
        self.allow_merge = allow_merge

    def sample(self):
        while True:
            # Randomly sample the proportion of funds allocated to each portfolio
            allocation = np.random.dirichlet(np.ones(self.num_portfolios))
            total_risk = np.dot(allocation, self.risk_threshold)
            if total_risk <= self.risk_threshold:
                break
        if self.allow_merge:
            merge_decision = np.random.choice([True, False])
        else:
            merge_decision = False
        return allocation, merge_decision

class RewardFunction:
    def __init__(self, target_portfolio_value, target_risk, penalty_weight):
        self.target_portfolio_value = target_portfolio_value
        self.target_risk = target_risk
        self.penalty_weight = penalty_weight

    def calculate_reward(self, portfolio_value, portfolio_risk, penalties_incurred):
        # Reward for increasing portfolio value
        profit_reward = portfolio_value - self.target_portfolio_value
        
        # Penalty for exceeding target risk
        risk_penalty = abs(portfolio_risk - self.target_risk)
        
        # Penalty for incurred penalties
        penalty_penalty = sum(penalties_incurred.values()) * self.penalty_weight
        
        # Total reward
        reward = profit_reward - risk_penalty - penalty_penalty
        return reward

class Environment:
    def __init__(self, initial_state, reward_function, max_steps):
        self.state = initial_state
        self.reward_function = reward_function
        self.max_steps = max_steps
        self.current_step = 0

    def reset(self):
        # Reset the environment to its initial state
        self.current_step = 0
        return self.state

    def step(self, portfolio_allocation, merge_decision):
        # Update state based on agent's actions
        self.update_state(portfolio_allocation, merge_decision)
        
        # Calculate reward
        portfolio_value = sum(self.state.portfolio_balances.values())
        portfolio_risk = sum(self.state.portfolio_risks.values())
        penalties_incurred = self.state.penalties_incurred
        reward = self.reward_function.calculate_reward(portfolio_value, portfolio_risk, penalties_incurred)
        
        # Increment step counter
        self.current_step += 1
        
        # Check if episode is done
        done = self.current_step >= self.max_steps  # Or define another termination condition
        
        # Return state, reward, done flag
        return self.state, reward, done

    def update_state(self, portfolio_allocation, merge_decision):
        # Update portfolio balances, debt balances, etc. based on agent's actions
        # This involves applying the portfolio allocation and merging decisions to the state
        # For simplicity, we'll assume that the state is updated accordingly
        pass

class PolicyNetwork(tf.keras.Model):
    def __init__(self, num_actions):
        super(PolicyNetwork, self).__init__()
        self.dense1 = tf.keras.layers.Dense(64, activation='relu')
        self.dense2 = tf.keras.layers.Dense(64, activation='relu')
        self.dense3 = tf.keras.layers.Dense(num_actions, activation='softmax')

    def call(self, state):
        x = self.dense1(state)
        x = self.dense2(x)
        return self.dense3(x)

class PolicyGradientAgent:
    def __init__(self, num_actions, learning_rate=0.001, gamma=0.99):
        self.policy_network = PolicyNetwork(num_actions)
        self.optimizer = tf.keras.optimizers.Adam(learning_rate)
        self.gamma = gamma
        self.episode_rewards = []
        self.episode_log_probs = []

    def select_action(self, state):
        action_probs = self.policy_network(np.array([state]))
        action = np.random.choice(range(len(action_probs[0])), p=action_probs.numpy()[0])
        return action, tf.math.log(action_probs[0][action])

    def train_step(self, states, actions, rewards):
        with tf.GradientTape() as tape:
            log_probs = tf.stack(self.episode_log_probs)
            discounted_rewards = self._compute_discounted_rewards(rewards)
            loss = -tf.reduce_mean(log_probs * discounted_rewards)

        gradients = tape.gradient(loss, self.policy_network.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.policy_network.trainable_variables))
        
        self.episode_rewards = []
        self.episode_log_probs = []

    def _compute_discounted_rewards(self, rewards):
        discounted_rewards = np.zeros_like(rewards)
        running_add = 0
        for t in reversed(range(len(rewards))):
            running_add = running_add * self.gamma + rewards[t]
            discounted_rewards[t] = running_add
        return discounted_rewards

# Example usage
num_actions = 3  # Number of actions in the action space
agent = PolicyGradientAgent(num_actions)

# Example environment variables
portfolio_balances = {'portfolio1': 10000, 'portfolio2': 15000, 'portfolio3': 20000}
portfolio_rates = {'portfolio1': 0.08, 'portfolio2': 0.06, 'portfolio3': 0.07}
portfolio_risks = {'portfolio1': 7, 'portfolio2': 4, 'portfolio3': 6}
portfolio_age = {'portfolio1': 5, 'portfolio2': 3, 'portfolio3': 1}
debt_balances = {'debt1': 5000}
debt_rates = {'debt1': 0.06}
penalties_incurred = {'early_withdrawal_penalty': 100}
time_remaining_penalties = {'early_withdrawal_penalty': 10}
inflation_rate = 0.025  # 2.5%
target_portfolio_value = 100000
target_risk = 20
penalty_weight = 0.5
max_steps = 100  # Maximum number of steps per episode

initial_state = State(portfolio_balances, portfolio_rates, portfolio_risks, portfolio_age, debt_balances, debt_rates, penalties_incurred, time_remaining_penalties, inflation_rate)
reward_function = RewardFunction(target_portfolio_value, target_risk, penalty_weight)
env = Environment(initial_state, reward_function, max_steps)

# Training loop with monitoring and evaluation
num_episodes = 1000  # Define the number of episodes for training
episode_rewards = []

for episode in range(num_episodes):
    state = env.reset()
    episode_states = []
    episode_actions = []
    episode_rewards = []

    done = False
    while not done:
        action, log_prob = agent.select_action(state.get_state_representation())
        next_state, reward, done = env.step(action, merge_decision=False)  # Assuming merge decision is always False
        
        episode_states.append(state)
        episode_actions.append(action)
        episode_rewards.append(reward)

        state = next_state

    # Train the agent using collected experiences from the episode
    agent.train_step(episode_states, episode_actions, episode_rewards)

    # Logging
    total_reward = np.sum(episode_rewards)
    episode_rewards.append(total_reward)
    print(f"Episode {episode + 1}: Total Reward = {total_reward}")

# Plotting training metrics
plt.plot(episode_rewards)
plt.xlabel('Episode')
plt.ylabel('Total Reward')
plt.title('Training Progress')
plt.show()

# Evaluation
evaluation_episodes = 100  # Define the number of episodes for evaluation
eval_rewards = []

for _ in range(evaluation_episodes):
    state = env.reset()
    total_reward = 0
    done = False
    while not done:
        action, _ = agent.select_action(state.get_state_representation())
        next_state, reward, done = env.step(action, merge_decision=False)  # Assuming merge decision is always False
        total_reward += reward
        state = next_state
    eval_rewards.append(total_reward)

avg_eval_reward = np.mean(eval_rewards)
print(f"Average Evaluation Reward: {avg_eval_reward}")
