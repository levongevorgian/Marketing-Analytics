"""
Run this file at first, to see what it prints.
Instead of using print(), use the respective log level.
"""
############################### LOGGER
from abc import ABC, abstractmethod
from loguru import logger
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random


class Bandit(ABC):
    """
    Abstract Bandit class for multi-armed bandit algorithms.

    Attributes
    ----------
    p : list or np.ndarray
        True rewards for each bandit arm.
    """

    @abstractmethod
    def __init__(self, p):
        """
        Initialize the bandit with given reward probabilities.

        Parameters
        ----------
        p : list or np.ndarray
            The true mean rewards of each bandit arm.
        """
        pass

    @abstractmethod
    def __repr__(self):
        """Return a string representation of the bandit."""
        pass

    @abstractmethod
    def pull(self):
        """Pull an arm and return the chosen arm index."""
        pass

    @abstractmethod
    def update(self, chosen_arm, reward):
        """
        Update the bandit's internal statistics after pulling an arm.

        Parameters
        ----------
        chosen_arm : int
            Index of the pulled arm.
        reward : float
            Observed reward from the arm.
        """
        pass

    @abstractmethod
    def experiment(self, trials=20000):
        """
        Run the bandit experiment for a specified number of trials.

        Parameters
        ----------
        trials : int, optional
            Number of trials to simulate (default is 20000).
        """
        pass

    @abstractmethod
    def report(self):
        """Generate results, save CSV, and log cumulative reward and regret."""
        pass


class Visualization:
    """
    Visualization class for plotting cumulative rewards and regrets.
    """

    def plot1(self, eg_rewards, ts_rewards):
        """
        Plot cumulative rewards for Epsilon Greedy and Thompson Sampling.

        Parameters
        ----------
        eg_rewards : list
            Cumulative rewards from Epsilon Greedy.
        ts_rewards : list
            Cumulative rewards from Thompson Sampling.
        """
        plt.figure()
        plt.plot(eg_rewards, label='Epsilon Greedy')
        plt.plot(ts_rewards, label='Thompson Sampling')
        plt.title('Cumulative Rewards')
        plt.xlabel('Trials')
        plt.ylabel('Cumulative Reward')
        plt.legend()
        plt.grid()
        plt.savefig('plot1_rewards.png')
        plt.show()

    def plot2(self, eg_rewards, ts_rewards, p):
        """
        Plot cumulative regrets for Epsilon Greedy and Thompson Sampling.

        Parameters
        ----------
        eg_rewards : list
            Cumulative rewards from Epsilon Greedy.
        ts_rewards : list
            Cumulative rewards from Thompson Sampling.
        p : list
            True rewards of each bandit.
        """
        max_p = max(p)
        eg_regret = [max_p * (i + 1) - r for i, r in enumerate(eg_rewards)]
        ts_regret = [max_p * (i + 1) - r for i, r in enumerate(ts_rewards)]

        plt.figure()
        plt.plot(eg_regret, label='Epsilon Greedy Regret')
        plt.plot(ts_regret, label='Thompson Sampling Regret')
        plt.title('Cumulative Regrets')
        plt.xlabel('Trials')
        plt.ylabel('Cumulative Regret')
        plt.legend()
        plt.grid()
        plt.savefig('plot2_regrets.png')
        plt.show()


class EpsilonGreedy(Bandit):
    """
    Epsilon Greedy algorithm for multi-armed bandits.

    Attributes
    ----------
    p : list
        True rewards for each bandit.
    epsilon : float
        Exploration probability.
    counts : np.ndarray
        Counts of pulls for each arm.
    values : np.ndarray
        Estimated values for each arm.
    total_reward : float
        Cumulative reward collected.
    rewards : list
        Cumulative rewards per trial.
    choices : list
        Record of chosen arms and rewards.
    algorithm : str
        Name of the algorithm.
    """

    def __init__(self, p, epsilon=1.0):
        """
        Initialize Epsilon Greedy bandit.

        Parameters
        ----------
        p : list
            True rewards of each arm.
        epsilon : float, optional
            Initial exploration probability (default 1.0).
        """
        self.p = p
        self.n = len(p)
        self.epsilon = epsilon
        self.counts = np.zeros(self.n)
        self.values = np.zeros(self.n)
        self.total_reward = 0
        self.rewards = []
        self.choices = []
        self.algorithm = 'EpsilonGreedy'

    def __repr__(self):
        """Return string representation."""
        return f"EpsilonGreedy(epsilon={self.epsilon})"

    def pull(self):
        """Choose an arm using epsilon-greedy policy."""
        if random.random() < self.epsilon:
            return np.random.randint(self.n)
        else:
            return np.argmax(self.values)

    def update(self, chosen_arm, reward):
        """
        Update estimated values and cumulative rewards after pulling an arm.

        Parameters
        ----------
        chosen_arm : int
            Index of the chosen arm.
        reward : float
            Observed reward.
        """
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]
        value = self.values[chosen_arm]
        self.values[chosen_arm] = ((n - 1) * value + reward) / n
        self.total_reward += reward
        self.rewards.append(self.total_reward)
        self.choices.append((chosen_arm, reward))

    def experiment(self, trials=20000):
        """
        Run Epsilon Greedy experiment for a number of trials.

        Parameters
        ----------
        trials : int, optional
            Number of trials to simulate (default 20000).
        """
        for t in range(1, trials + 1):
            self.epsilon = 1 / t
            arm = self.pull()
            reward = np.random.normal(self.p[arm], 1)
            self.update(arm, reward)

    def report(self):
        """Save results to CSV and log cumulative reward and regret."""
        df = pd.DataFrame(self.choices, columns=['Bandit', 'Reward'])
        df['Algorithm'] = self.algorithm
        df.to_csv('epsilon_greedy_results.csv', index=False)
        avg_reward = self.total_reward / len(self.choices)
        regret = np.sum(np.max(self.p) - np.array([self.p[choice[0]] for choice in self.choices]))
        logger.info(f"EpsilonGreedy - Average Reward: {avg_reward:.4f}")
        logger.info(f"EpsilonGreedy - Total Regret: {regret:.4f}")


class ThompsonSampling(Bandit):
    """
    Thompson Sampling algorithm for multi-armed bandits.

    Attributes
    ----------
    p : list
        True rewards for each bandit.
    alpha : np.ndarray
        Alpha parameters for Beta distributions.
    beta : np.ndarray
        Beta parameters for Beta distributions.
    total_reward : float
        Cumulative reward collected.
    rewards : list
        Cumulative rewards per trial.
    choices : list
        Record of chosen arms and rewards.
    algorithm : str
        Name of the algorithm.
    """

    def __init__(self, p):
        """
        Initialize Thompson Sampling bandit.

        Parameters
        ----------
        p : list
            True rewards of each arm.
        """
        self.p = p
        self.n = len(p)
        self.alpha = np.ones(self.n)
        self.beta = np.ones(self.n)
        self.total_reward = 0
        self.rewards = []
        self.choices = []
        self.algorithm = 'ThompsonSampling'

    def __repr__(self):
        """Return string representation."""
        return "ThompsonSampling()"

    def pull(self):
        """Choose an arm using Thompson Sampling policy."""
        samples = [np.random.beta(self.alpha[i], self.beta[i]) for i in range(self.n)]
        return np.argmax(samples)

    def update(self, chosen_arm, reward):
        """
        Update Beta parameters and cumulative rewards after pulling an arm.

        Parameters
        ----------
        chosen_arm : int
            Index of the chosen arm.
        reward : float
            Observed reward.
        """
        if reward >= 0:
            self.alpha[chosen_arm] += reward
        else:
            self.beta[chosen_arm] += abs(reward)
        self.total_reward += reward
        self.rewards.append(self.total_reward)
        self.choices.append((chosen_arm, reward))

    def experiment(self, trials=20000):
        """
        Run Thompson Sampling experiment for a number of trials.

        Parameters
        ----------
        trials : int, optional
            Number of trials to simulate (default 20000).
        """
        for _ in range(trials):
            arm = self.pull()
            reward = np.random.normal(self.p[arm], 1)
            self.update(arm, reward)

    def report(self):
        """Save results to CSV and log cumulative reward and regret."""
        df = pd.DataFrame(self.choices, columns=['Bandit', 'Reward'])
        df['Algorithm'] = self.algorithm
        df.to_csv('thompson_sampling_results.csv', index=False)
        avg_reward = self.total_reward / len(self.choices)
        regret = np.sum(np.max(self.p) - np.array([self.p[choice[0]] for choice in self.choices]))
        logger.info(f"ThompsonSampling - Average Reward: {avg_reward:.4f}")
        logger.info(f"ThompsonSampling - Total Regret: {regret:.4f}")


def comparison():
    """
    Compare Epsilon Greedy and Thompson Sampling algorithms on the same bandit problem.
    """
    p = [1, 2, 3, 4]

    eg = EpsilonGreedy(p)
    ts = ThompsonSampling(p)

    eg.experiment()
    ts.experiment()

    eg.report()
    ts.report()

    vis = Visualization()
    vis.plot1(eg.rewards, ts.rewards)
    vis.plot2(eg.rewards, ts.rewards, p)


if __name__ == '__main__':
    comparison()
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
