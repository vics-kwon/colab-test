import opensim as osim
from osim.env import ProstheticsEnv

env = ProstheticsEnv(visualize=False)
observation = env.reset()
total_reward = 0.0
for i in range(200):
    # make a step given by the controller and record the state and the reward
    observation, reward, done, info = env.step(env.action_space.sample())
    total_reward += reward
    if done:
        break

# Your reward is
print("Total reward %f" % total_reward)