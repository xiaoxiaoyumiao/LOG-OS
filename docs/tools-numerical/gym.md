# gym

Python package for reinforcement learning.

## Introduction

The key concept, "environment", abstracts what an agent is interacting with. Agent executes action in an environment, and the environment provides an observation result and a reward as feedback.

```python
import gym
env = gym.make('CartPole-v0') # load an example environment
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample() # choose an action
        observation, reward, done, info = env.step(action) # execute, and get reward
        if done: # "done" indicates ending of the task
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()
```



## Reference

\[1] [https://gym.openai.com/docs/](https://gym.openai.com/docs/)

\[2] [https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa](https://medium.com/@apoddar573/making-your-own-custom-environment-in-gym-c3b65ff8cdaa)

