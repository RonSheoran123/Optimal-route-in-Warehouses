# Optimal-route-in-Warehouses
In a Distribution Center (DC), walking time from one location to another during the picking route can account for 60% to 70% of the operator’s working time.
Hence, reducing the walking time is one of the most effective ways to improve overall productivity.

Here, we have a 2-dimensional warehouse model(axis-x,axis-y),to which we will find the optimal route for order retrievel by using Single Picker Routing Problem (SPRP).
SPRP is a specific application of the general Traveling Salesman Problem (TSP) answering the question:

“Given a list of storage locations and the distances between each pair of locations, what is the shortest possible route that visits each storage location and returns to the depot ?”

**Method: Order Batching**
Orders are divided into "waves", where each wave consists 'n' number of orders.For each wave, the starting and ending points are same. The optimal path is calculated by finding the _next shortest distance between two orders_. The experiment is ran for various 'orders per wave' and the results are compared through a bar graph.
For every wave, a graphical reprentation of its path is also plotted.

**Results**
The total distance covered for each wave decreases exponentially as the number of orders per wave increases(with a **72.28%** decrease in total distace from 1 order/wave to 10 orders/wave). Suitable orders/wave can be chosen according to the capacity of equipments such as forklift.

**Constraints**
1) It is assumed that only one vehicle is available for use.
2) The time window in which the order has to be retrieved is ignored(due to unavailability of such a dataset to use).

**Total distance covered vs Orders per wave**

<img width="775" alt="Screenshot 2023-07-21 132922" src="https://github.com/RonSheoran123/Optimal-route-in-Warehouses/assets/106268100/f9950521-e52b-493d-9d13-fcb841344f7c">


**Route for a wave with 11 orders**

<img width="471" alt="image" src="https://github.com/RonSheoran123/Optimal-route-in-Warehouses/assets/106268100/ebc6d59a-0d58-42c2-be41-31b2f37bbf9b">
