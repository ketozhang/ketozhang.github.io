---
title: Software Job Interview
---

## Data Structure and Algorithms

For every structure understand the Big-O time and space complexity for the following operations:

1. Insert
1. Delete
1. Sort
1. Bulk Insert

### Basic
* List/Array
  * <https://leetcode.com/problems/copy-list-with-random-pointer/>
    * [x] 1: Implementation is slow, very disorganized, plan it out
    * [x] 2: Still quite slow O(N), organization is much better. If two array indexes each other, consider mapping them (dict).
  * <https://leetcode.com/problems/merge-two-sorted-lists/>
    * [x] 1: Failed, too much time generating MaxHeap, next time use standard library. Missed the fact that the list were sorted; could've used comparison because of this fact.
    * [x] 2: Excellent!
  * Return the most common values of an array. If there's a tie, return them all.
  * [Zombie in Matrix](https://leetcode.com/discuss/interview-question/411357/)
    * [x] 1: Excellent, only issue is solution required mutation of the input. Requiring a deepcopy of an input is not a good indicator. You should've used the idea that only indices need to be iterated not the whole grid.
* Dictionary/Map
  * [Top K Frequently Mentioned Keywords](https://leetcode.com/discuss/interview-question/542597/)
    * [x] 1: Strings possible contain `[^a-z0-9]`, replace those with whitespace; the review itself doesn't matter, just make sure to count each word once (set) then store them in a list. Counter returns value and count. Heapq would be easy to get first k.
  * [Favorite Genres](https://leetcode.com/discuss/interview-question/373006)
    * [x] 1: Excellent, solution is equivalently $\mathcal O(N^2)$
* Tree (CS 61B)
  * [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/submissions/)
    * 1: Excellent, it did take a while to fix some bugs. Solutions is a bit slow. Note that binary trees can be easily represented by strings.
  * [x] Min/max heap
  * [ ] Binary search tree
  * [ ] Trie


### Intermediate
* Hashmaps (CS61B)
* Caches (CS 61B and 186)
* Graphs
  * [Critical Nodes](https://leetcode.com/discuss/interview-question/436073/)
    * [x] 1: Failed, while a connected graph requires $E >= N-1$, a disconnected graph can also have $E = N-1$.
  * [Critical Connections](https://leetcode.com/discuss/interview-question/372581)
    * [x] 1: Failed to code up bridge algorithm. You need to pseudocode more before trying
    * [x] 2: Success to code up brute force algorithm. Works really well and although slow $\mathcal O(E^2 + EV)$ at worst case.

### Exotic
* B+ Trees (CS 186)

## Resources
* [Interview Behavior Question Guide](https://docs.google.com/document/d/1f_JZNuSEShzCPORxfSE8cAKR1RiqV7NgygyRtAncxVI/edit)
* [Amazon System Design Preparation](https://www.youtube.com/watch?v=gNQ9-kgyHfo)
* [Amazon Code Sampling (SIP)](https://www.youtube.com/watch?v=mjZpZ_wcYFg)
* [Two examples for each of Amazon’s 14 Leadership Principles](https://www.youtube.com/watch?v=RzlUQCy84rQ)
* [Amazon Assessment Debugging](https://docs.google.com/document/d/188JrZmqv7Nm7EULXItESSLmSEr7vBziqRUPew2oyWKY/edit)
* [Amazon Assessment Questions AC](https://aonecode.com/amazon-online-assessment)
* [Amazon Assessment Questions LC](https://leetcode.com/discuss/interview-question/344650/Amazon-Online-Assessment-Questions)
* [LeetCoder Advice on 0 to Clearing all Interviews](https://leetcode.com/discuss/career/216554/from-0-to-clearing-uberappleamazonlinkedingoogle)
* [Scalable Systems Primer](https://github.com/donnemartin/system-design-primer)

## Systems Design

* Don't jump into solving problems
* Ask questions!
  1. Ask about the product (usually given)
  1. Ask about content
  1. Ask about users (size, usage)
  1. Ask about performance (throughput, concurrency)
  1. Ask about what action/API is needed
* Start focusing on your expertise (backend, frontend, production server)

### Backend
Defining the schema, just field names are fine

* Highlight possibly special fields to that particular product (e.g., multiple payment methods)
* Identify high-usage queries to determine schema indices/keys.

### Web Server
Defining the API

* Go through API URL endpoint structure (`domain/resource/params?query_params`)
* Speak in HTTP requests
* A POST and PUT would need a JSON input.
* Each definable actions can be grouped into individual services. Each services may belong to a database table, but they should interact.

### Frontend

* Start with the front page with basic services (e.g., search box)
* Keep asking if they expect any other services (e.g., recommendations)
* Head to the next page  by following a service action (e.g., clicking the search bar)


### Improvements for Performance

* **Load Balancer**

  The idea of having a router to route requests to specific computers in attempt to reduce the traffic/load of a single computer. The added benefit is redundancy of servers which if one goes down there exist other possible routes.

* **Cached Database**

  A copy of the database whether it's a full copy (rare) or a usage-base copy (more common) to both increase the data-access speed and create a layer of redundancy if the database goes down.

* **Database Load Balancing**

  Similar to having multiple servers for web requests, multiple copies of a database on separate resources (often read-only copies) can not only solve load issues but also provide redundancy.

* **Content Delivery Network**

  A network of servers (often intelligently geographically placed) to server web assets (images, videos, CSS, etc).
