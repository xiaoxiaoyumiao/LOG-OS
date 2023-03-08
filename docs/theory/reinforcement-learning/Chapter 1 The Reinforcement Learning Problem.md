**Reinforcement learning problems** describe a learning agent interacting with the environment to achieve the goal. Any method that solves this kind of problem is considered as a **reinforcement learning method**.

**Supervised learning** learns from a training set of labeled examples provided by a knowledgeable external supervisor. **Unsupervised learning** finds structure hidden in collections of unlabeled data. However reinforcement learning doesn't precisely fall into either one of these two paradigms.

A key challenge in RL is the trade-off between exploration and exploitation.

A reinforcement learning system contains 4 elements: a policy, a reward signal, a value function, and a model (optional).
* A **policy** defines the learning agent's way of behaving at a given time.
* A **reward signal** defines the goal in the problems. The environment provides the agent a **reward** at each time step. The reward is a single number.
* A **value function** specifies the **value** of a state, which is the total amount of reward the agent can expect to receive over the future if starting from the state.
* A **model** of the environment describes how the environment will behave. Methods that use models are called **model-based** methods while others are called **model-free** methods.
