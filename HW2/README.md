# HW2 - A/B Testing with Multi-Armed Bandits

This repository contains my second homework for DS223 - Marketing Analytics. The assignment focuses on using **multi-armed bandit algorithms** to optimize advertisement selection. Specifically, we implement **Epsilon-Greedy** and **Thompson Sampling** strategies to learn which ad performs best over multiple trials.

---

## Directory Structure

### code/
This folder contains the Python code implementing the experiment:

- [Bandit.py](code/Bandit.py) — Abstract `Bandit` class defining the interface for all bandit algorithms
- Additional helper scripts for running experiments.

### data/
Contains the results of the experiments:

- [`epsilon_greedy_results.csv`](data/epsilon_greedy_results.csv) — Rewards collected using Epsilon-Greedy.
- [`thompson_sampling_results.csv`](data/thompson_sampling_results.csv) — Rewards collected using Thompson Sampling.

### img/
Contains visualizations of the experiment:

- [`plot1_rewards.png`](img/plot1_rewards.png) — Rewards over time for each algorithm.
- [`plot2_regrets.png`](img/plot2_regrets.png) — Cumulative regret for both algorithms.

### HW2 Specifics
- [`requirements.pdf`](HW2/requirements.pdf) — Contains the homework requirements and instructions.
- [`requirements.txt`](HW2/requirements.txt) — Lists Python dependencies needed to run the code.

---

## Homework Overview

The goal of this homework is to design an experiment with **four advertisement options (bandits)** and compare the performance of **Epsilon-Greedy** and **Thompson Sampling** algorithms.

### Experiment Setup

- **Bandit Rewards:** `[1, 2, 3, 4]`  
- **Number of Trials:** `20000`  
- **Algorithms:**
  - **Epsilon-Greedy:** Epsilon decays over time (`epsilon = 1/t`). Selects ads based on estimated rewards.
  - **Thompson Sampling:** Uses Bayesian inference with known precision to select ads probabilistically.

### Reporting

- Visualize the learning process for each algorithm (`plot1_rewards.png`).
- Visualize cumulative rewards and cumulative regret (`plot2_regrets.png`).
- Store rewards in CSV files (`Bandit, Reward, Algorithm`).
- Print cumulative reward and cumulative regret.

### Submission Notes

- All code is documented (recommended to use `pyment` for docstrings).  
- Push all code, data, and visualizations to GitHub.  
- Submit the **GitHub repository link** to Moodle.  
- Late submissions are treated according to the course syllabus.

### Bonus 

- Suggest improvements for the current implementation plan.  
- Ideas for better exploration-exploitation strategies or code optimization can earn extra points.

---

## References

- DS223 - Marketing Analytics course materials.  
- Multi-Armed Bandit literature for Epsilon-Greedy and Thompson Sampling.


