# import gym
# env = gym.make('FrozenLake-v0')
# for i_episode in range(2):
#     observation = env.reset()
#     for t in range(100):
#         env.render()
#         print(observation)
#         action = env.action_space.sample()
#         observation, reward, done, info = env.step(action)
#         if done:
#             print("Episode finished after {} timesteps".format(t+1))
#             break
# env.close()


import gym

env = gym.make("Taxi-v2").env

env.render()