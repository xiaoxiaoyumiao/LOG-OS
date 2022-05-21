# ML Agents

official: https://github.com/Unity-Technologies/ml-agents

## Installation

- Unity version 2020.3.25f1
- ML Agents 2.0.1 Installed by built-in package manager
- ML Agents Extensions 0.4.0 preview installed by adding package from disk, source: https://github.com/Unity-Technologies/ml-agents/releases
- Updated Input System package
- Regenerate project files if needed

## Quick Start

ref: https://gilberttanner.com/blog/ml-agents

take away:

- every agent in Unity has an behavior
- behavior gets observations and determines actions
- behavior can be heuristic, training, or inference

- pretrained models can be used
- by python package `mlagents` you can train agents in unity by creating a server process using command `mlagents-learn` 
- the command accepts a config YAML file as input
- tensorboard event files are generated during training

## Build the executable

Basically there's no much difference compared to a normal build of Unity project. If you want debug information, toggle Development Build. If you want to use the executable on a headless server, toggle Server Build. These can be found in the Unity build settings.

There is one important thing to note that the build backend for training ML agents should be Mono instead of IL2CPP.
    - ref: https://forum.unity.com/threads/unitytimeoutexception-the-unity-environment-took-too-long-to-respond-when-using-an-executable.907010/
    - ref: https://github.com/Unity-Technologies/ml-agents/issues/1777

### About loading and unloading the Unity executable

Suppose the build output files(for example, for Linux there're `.x86_64`, `.so`, `_Data` folder, etc.; for Windows there're `.exe`, `.dll`, `_Data` folder, etc.) are located under `some_path/Build/Debug/`. 

The filename of the executable would be the name of the Unity environment. (for example, if we name the executable `3DBall` when we build for Linux, the executable would be named `3DBall.x86_64` and the library would be named `3DBall.so`, thus the name of the Unity environment would be `3DBall` as well. For Windows it's similar; the name of the executable would be `3DBall.exe` and `3DBall` would still be the name of the environment)

When loading and wrapping the Unity environment with `mlagents_envs.environment.UnityEnvironment`, just provide the path to the environment. For example, in our case it would be `some_path/Build/Debug/3DBall`, which is also the path to the executable, but ignoring the extension of the executable (`.x86_64`, `.exe`, etc). (No harm to add the extension though)

A successful load would look like this if the log level is set to INFO (in my case the E0417 error appeared when running in WSL but not in Windows. Not affecting the run anyway):

```python
>>> unity_env = UnityEnvironment(UNITY_PATH)
E0417 18:20:24.716297000     893 fork_posix.cc:70]           Fork support is only compatible with the epoll1 and poll polling strategies
[INFO] Connected to Unity environment with package version 2.0.1 and communication version 1.5.0
```

To initialize the environment, use `reset()` method (not required if it's wrapped by a gym wrapper. Just use the wrapper to do reset):

```python
unity_env.reset()
```

To unload the Unity environment, use `close()` method:

```python
unity_env.close()
```

## Behavior

The behaviors are specified by the `behavior_specs` property. it's a map-like object. It's values are of type `BehaviorSpec`

## Observations

### Visual Observation

To get visual observation, just add Camera Sensor "component" to the agent and assigns proper camera object to it. There may exist multiple Camera Sensors.

When I used it in HDRP, the observation became blurry. This was solved by un-toggling Project settings -> HDRP default settings -> motion vector (disabling the motion blur post-processing effect).

To obtain visual observation while running on a headless server, use `xvfb-run`. 
    - ref: https://forum.unity.com/threads/ml-agent-server-build-headless-with-visual-observations-and-multiple-gpus.1042456/

## Action

Ensure that the action space is properly set. Branches correspond to different indices in the received action buffer in `OnActionReceived` and branch size corresponds to number of (discrete) actions available for the certain branch. A robot can take actions from multiple branches at one step, but it may only pick one action per branch. In the buffer the action is encoded from 0 to [size-1].
  - ref: https://forum.unity.com/threads/question-about-branches.895220/

### Decision Requester

Remember to add Decision Requester to agent to let it request actions.

Uncheck `take actions between` to disable action repetition when it's not a decision step. (by default it will repeat the latest action for every frame)

ref: https://forum.unity.com/threads/not-sure-about-setreward-and-addreward-functionality.866113/

## Side channels

Implement custom channel class on both C# and python sides.
  - C#: inherit `SideChannel` class, override `OnMessageReceived`, use `QueueMessageToSend` to send message of type `OutgoingMessage`, register channel object with `SideChannelManager.RegisterSideChannel`and unregister with `SideChannelManager.UnregisterSideChannel`
  - python: inherit `SideChannel` class, override `on_message_received` method, use `super().queue_message_to_send` to send message of type `OutgoingMessage`

The `OutgoingMessage` has several method to store data like `write_int32` for python side. They can be called on a same `OutgoingMessage` multiple times and the data would be filled into the message in sequence. Then you can queue the message and send it. The data would be received in the same order they are written into the message.
  - Two sides of a channel are connected by their channel ID, which is a GUID. Just generate one by yourself and ensure that both sides use the same GUID.

From python side, environment parameters are also set through a specific type of side channel `EnvironmentParametersChannel`. See: https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API-Documentation.md#mlagents_envsside_channelenvironment_parameters_channel

Main ref & sample code: https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Custom-SideChannels.md

## Reference

official repo: https://github.com/Unity-Technologies/ml-agents

installation: https://github.com/Unity-Technologies/ml-agents/blob/release_17_docs/docs/Installation.md

training: https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Training-ML-Agents.md#training-configurations

environment executable: https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Executable.md

academy steps: https://forum.unity.com/threads/academy-steps.875938/

agents: https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Design-Agents.md#actions-and-actuators

interfaces, sequence of calling: https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Learning-Environment-Design.md, https://forum.unity.com/threads/sequence-of-called-methods.916352/

side channel: https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Custom-SideChannels.md

`mlagents` python API, unity env: https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Python-API.md

gym wrapper: https://github.com/Unity-Technologies/ml-agents/blob/main/gym-unity/README.md

tut - official, humming birds: https://learn.unity.com/course/ml-agents-hummingbirds

tut & repo - jumping cars, behavior impl: https://towardsdatascience.com/ultimate-walkthrough-for-ml-agents-in-unity3d-5603f76f68b

tut - training parameters: https://www.gocoder.one/blog/introduction-to-unity-ml-agents

tut - videos: https://www.youtube.com/playlist?list=PLzDRvYVwl53vehwiN_odYJkPBzcqFw110

Robotics in Unity: https://github.com/Unity-Technologies/Unity-Robotics-Hub

Another 3D framework for RL: https://github.com/xavierpuigf/virtualhome