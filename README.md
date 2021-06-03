# RRTandBiRRT
## MLDA RMUA selection task in python
Updated on 3rd June 2021

### Task overview:
Rapidly-Exploring Random Trees (RRT) is a famous planning algorithm developed by Lavalle et al. It has multiple applications including aerial robotics and self-driving cars. I was required to implement the RRT algorithm for a simple 2D environment and wrap your implementation using ROS.

### Specifications:
1. State Space: The state space is (x,y), i.e. 2 degrees of freedom. The state space should be represented as a nav_msgs/OccupancyGrid message. A map server ROS node should be implemented which can read an image file (PNG/JPG/PGM) representing a map and convert it to a nav_msgs/OccupancyGrid message and publish it on the ROS topic /map.

2. Planner: A planner ROS node should be implemented which subscribes to the ROS topic /map and receives the nav_msgs/OccupancyGrid message. The node should also be able to read the starting position and goal specified in (x,y) coordinates provided by us (through ROS topics). The planner node should then be able to plan a path from the starting position to the requested goal using RRT and publish the path to the goal as a nav_msgs/Path message.

3. Visualization: The best way to see the algorithm work is through visualization. The planner node should have the option of enabling visualization such that each step of the planning algorithm can be visible and we can see the tree building before a final path is found. This can be done using an image processing library like OpenCV or any other tool of choice.

### Bonus Specifications:

4. The version/flavor of RRT: Minimum deliverable is to implement vanilla RRT. Bonus points for implementing modified RRT versions like RRT*, anytime-RRT, Informed-RRT, etc. 

5. Mapping: Provide an MS Paint like environment to draw custom maps that can be used to test your RRT implementation. This tool would ideally use OpenCV to provide the user with a blank image (representing free-space) as a canvas where the user can draw obstacles using the mouse as a paintbrush. This map can then either be saved in the system or be published as a nav_msgs/OccupancyGrid message directly. The planner node should be able to find a path from the starting position to the goal in this custom map using your RRT implementation.

### Execution overview
The execution of the above task was conducted in python. Some alternate routes were taken to make the path planning more efficient too. For example, instead of using the nav_msgs/OccupancyGrid message, the PathPlanningPlugin was used with a costmap to get a more efficient map interpretation directly with respect to RViz. The scripts for the RRT Planner can be found in the scripts folder named "mlda_task_solution.py" along with its server "mlda_task_solution_server.py". The path planning utilised a simple collision avoidance algorithm along with an off-the-shelf Bresenham line tracing algorithm for implementing the line drawing on RViz. The map utilised for testing out was having drawn obstacles on a white background. In the RViz interface you can set the 2D Nav Goal and set where the target position is, and watch the tree for the path planning execute over time.

For the extra specifications, you can find the "mlda_task_extra.py" file which has the function to be called for bidirectional RRT*, which I found to be the best RRT upgrade implementing the random but optimised tree from both the root node and the target node thus ensuring a faster pace of path planning. The work on the paint based GUI for drawing the obstacles is still ongoing and the repo will be updated with the same once done.

To start off, clone the repository:
```shell
    git clone https://github.com/PrithvirajRay/RRTandBiRRT.git
    ```

Continue by launching the task solution file for the RRT algorithm:
```shell
    roslaunch mlda_task_solution.launch
    ```
