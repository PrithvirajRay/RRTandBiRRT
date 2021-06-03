# RRTandBiRRT
MLDA RMUA selection task in python

Task overview:
Rapidly-Exploring Random Trees (RRT) is a famous planning algorithm developed by Lavalle et al. It has multiple applications including aerial robotics and self-driving cars. I was required to implement the RRT algorithm for a simple 2D environment and wrap your implementation using ROS.

Specifications:
    1. State Space: The state space is (x,y), i.e. 2 degrees of freedom. The state space should be represented as a nav_msgs/OccupancyGrid message. A map server ROS node should be implemented which can read an image file (PNG/JPG/PGM) representing a map and convert it to a nav_msgs/OccupancyGrid message and publish it on the ROS topic /map.

    2. Planner: A planner ROS node should be implemented which subscribes to the ROS topic /map and receives the nav_msgs/OccupancyGrid message. The node should also be able to read the starting position and goal specified in (x,y) coordinates provided by us (through ROS topics). The planner node should then be able to plan a path from the starting position to the requested goal using RRT and publish the path to the goal as a nav_msgs/Path message.

    3. Visualization: The best way to see the algorithm work is through visualization. The planner node should have the option of enabling visualization such that each step of the planning algorithm can be visible and we can see the tree building before a final path is found. This can be done using an image processing library like OpenCV or any other tool of choice.

Bonus Specifications:

If you have implemented all of the features above, well done to you! Now here are some bonus specifications for those who are up for a challenge!
    4. The version/flavor of RRT: Minimum deliverable is to implement vanilla RRT. Bonus points for implementing modified RRT versions like RRT*, anytime-RRT, Informed-RRT, etc. Every different modified version of RRT you implement gets you more points!

    5. Mapping: Provide an MS Paint like environment to draw custom maps that can be used to test your RRT implementation. This tool would ideally use OpenCV to provide the user with a blank image (representing free-space) as a canvas where the user can draw obstacles using the mouse as a paintbrush. This map can then either be saved in the system or be published as a nav_msgs/OccupancyGrid message directly. The planner node should be able to find a path from the starting position to the goal in this custom map using your RRT implementation.

Rules:
    1. Language of implementation must be C++ (preferred) or Python.
    2. We are currently using ROS Melodic which is preferred for this task. ROS Noetic or any distribution of ROS2 is also acceptable.
    3. Provide a nice-looking README.md for the project which describes in brief how to run the individual nodes, load a map image file, provide the starting position and goal, and enable visualization. Presentation matters, so bonus points for providing us with a beautiful README.
    4. Test map image files can be found here. The white regions in each image represent obstacles while the black regions represent free space.

Please revert to us by the deadline mentioned in the email. If you have any questions, do not hesitate to reach out to: mldarmua@e.ntu.edu.sg. Happy coding!
