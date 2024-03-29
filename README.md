# Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle

*Abstract*
Usually, optimal control leads to computationally costly solutions. Whereas a cheap solution may lead to an unstable control. There are many applications in which precise optimal control is not necessary and rather computational speed is required. This paper presents a novel technique to calculate a control input which generates a near optimal trajectory for an omni-directional vehicle-based system. This control input is generated at a significantly lower cost.
The complex non-linear system has been linearized by restricting the admissible controls. By applying a simple constraint on the control input, a near optimal trajectory is generated. As the computational cost of this strategy is low, a beneficial trade off between cost and optimality is achieved.


For running the admissible control plot

In the 119376348_Proj1->Files Open Admissible_control_plot.py file in a python environment and hit run
You will need the following libraries for the code to run 
math, numpy, matplotlib, sympy

For running the trajectory simulation plot

In the 119376348_Proj1->Files Open trajectory_simulation.py file in a python environment and hit run
You will need the following libraries for the code to run 
math, numpy, matplotlib**

*Results:*

1. Mapping of workspace

In the paper

![image](https://github.com/YashasShetty/Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle/assets/112819834/6787ccc6-3719-4579-a021-306a57e7e3e0)

Our result

![image](https://github.com/YashasShetty/Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle/assets/112819834/53ac0fdf-2915-4f73-a74e-b6119adb0004)


2. Restricting admissible controls

In the paper

![image](https://github.com/YashasShetty/Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle/assets/112819834/62eacf7d-0f46-47fa-9904-e4141a1e0c40)

Our result

![image](https://github.com/YashasShetty/Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle/assets/112819834/6da0c631-babb-4414-bdd2-5f74b81e92cd)


3. Trajectory Output

In the paper

![image](https://github.com/YashasShetty/Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle/assets/112819834/51fff040-d26a-4e37-aa5f-a14f0ebc45ce)

Our result

![image](https://github.com/YashasShetty/Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle/assets/112819834/40391bc7-7176-4c26-9a4c-fe6e602112ef)

4. Controller plot

In the paper

![image](https://github.com/YashasShetty/Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle/assets/112819834/f931873c-1ec9-45b7-a6df-4501537f8a8c)

Our result

qx:

![image](https://github.com/YashasShetty/Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle/assets/112819834/60654a26-c5be-44b5-90e3-c9997c983d6a)

qy:

![image](https://github.com/YashasShetty/Near-optimal_dynamic_trajectory_generation_and_control_of_an_omnidirectional_vehicle/assets/112819834/04dd7666-d017-422c-8cb2-b9a78135fcaa)
