---
title: Linked List
---

A sequential collection of elements where each element contains a value and a pointer.

* The pointer points to the next item in te list.
* The last pointer points to the null terminator used to signify the end of a list.

**Pros:**

* Easy insertion and deletion without allocation as the data does not need to be stored contiguously in memory due to pointers.

**Cons:**

* Access any particular index requires traversing.

**Examples:**

* Java's LinkedList and ArrayList

## Singly Linked List


## Doubly Linked List

The doubly linked list adds two pointers to each element: a next and a prev pointer. The first element's next pointer and last element's prev pointer points to the null terminator.

## Sentinel Node

A **sentinel node** is a node that points to the first and last element.

* Sentinel node provides a easy way to append to the ends of the list.

## Circular Linked List

Instead of the last pointer pointing to the null terminator, the last pointer points to the first first element.