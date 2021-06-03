def rrt_bidirectional(initial_position, target_position, width, height, map, map_resolution, map_origin, tree_viz):

        # tree a
	# Create the root node
  	root_node = Node(initial_position)
	create_new_branch_point(closest_node.coordinates, random_point,max_branch_length)
        
        		 

        # tree b
        
        root_node = Node(target_position)
        create_new_branch_point(closest_node.coordinates,random_point,max_branch_length)


	# A list to keep all nodes in the tree
  	nodes = [root_node]
  	# Iteration counter
  	interations = 0
  	# Iterations limit
  	max_iterations = 10000
  	# Incremental distance (for simplicity value is expressed in grid cells)
  	max_branch_lenght = 20
  	# Tolerance margin allowed around target position (value in grid cells)
  	goal_tolerance = 10
  	# A list to hold the output path from start to goal
  	path = []	




        while True:
            for q in self.Q:  # iterate over different edge lengths
                for i in range(q[1]):  # iterate over number of edges of given length to add
                    x_new= find_closest_node(random_point, nodes)
		    x_nearest= find_closest_node(random_point, nodes)
                    if x_new is None:
                        continue

                    # get nearby vertices and cost-to-come
                    L_near = find_closest_node(random_point, nodes)

                    # check nearby vertices for total cost and connect shortest valid edge
                    create_new_branch_point(closest_node.coordinates, random_point, max_branch_length)

                    if x_new in nodes[0].E:
                        # rewire tree
                        self.rewire(0, x_new, L_near)

                        # nearby vertices from opposite tree and cost-to-come
                        L_near = find_closest_node(random_point, nodes)

                        create_new_branch_point(closest_node.coordinates, random_point, max_branch_length)

                    if test_goal(latest_node.coordinates, target_position, goal_tolerance):

                        rospy.loginfo('RRT: Goal reached')
			break
                rospy.loginfo('RRT: Path search ended')

  		# Reconstruct path by working backwards from target
  		path.append(target_position)
  		node = latest_node
  		while node.parent:
      			path.append(node.coordinates)
      			node = node.parent
  		path.append(node.coordinates)
  		# Reverse list
  		path.reverse()
  		rospy.loginfo('RRT: Done reconstructing path')
            

