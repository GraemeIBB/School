Complexity of $O(b^d)$ in terms of space complexity, where d is the depth of the shallowest solution ( the length of the shortest path from the source node to any given goal node) and b is the branching factor (the maximum number of successors for any given state). Not optimal if the graph can be calculated

Can be seen as an extension to Dijkstra's algorithm - through the use of [[heuristic]](s)

**A**** terminates once it finds the shortest path to a specified goal, rather than generating the entire shortest-path tree from a specified source to all possible goals

<hr>

A* is defined as an informed search algorithm, or a best-first search. This means that it is formulated in termas of weighted graphs: strating from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining a tree of paths originating at the start of node and extending those paths one edge at a time until the goal node is reached.

At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on the cost of the path and an estimate of the cost required to extend the path all the way to the goal. Specifically, A* selects the path that minimizes: 
$f(n) = g(n) + h(n)$ 

Where n is the next node on the path, g(n) is the cost of the path from teh the start node to n, and h(n) is a [[heuristic]] function that estimates the cost of the cheapest path from n to the goal. The heuristic function is problem specific

Typical implementations of A* use a priority queue to perform the repeated selfction of minimum (estimated) cost nodes to expand. This p queue is known as the **open set, fringe, or frontier.** 