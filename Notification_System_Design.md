# Notification System Design

## Problem Statement

Students receive many notifications and may miss important updates such as placements and results.

## Solution

A Priority Inbox is implemented to show the most important unread notifications first.

Priority Order:
1. Placement
2. Result
3. Event

Recent notifications are given higher priority.

## Data Structure

Min Heap of size 10

## Algorithm

1. Assign weight to notification type.
2. Calculate priority score.
3. Insert unread notifications into heap.
4. Keep only top 10 notifications.
5. Display notifications in descending priority order.

## Complexity

- Insert: O(log 10)
- Retrieve: O(10 log 10)

## Benefits

- Efficient
- Scalable
- Real-time ranking