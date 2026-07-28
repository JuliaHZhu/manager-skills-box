# Blast Radius Algorithm

## Overview

Blast Radius performs a **bounded best-first search (BFS)** over the code dependency graph to find all nodes impacted by a change to a given starting node.

## Algorithm

1. **Lookup** the starting `code_nodes` row by `name`.
2. **Initialize** a queue with `(node_id, depth=0)` and a visited set.
3. **BFS loop**:
   - Dequeue `(nid, depth)`.
   - Query `code_edges` for all edges where `src_id=nid` or `dst_id=nid`.
   - For each unseen neighbor with allowed `kind` (calls/imports/inherits/uses):
     - Mark visited, enqueue `(neighbor, depth+1)`.
   - Stop when `max_nodes` (default 500) reached or queue empty.
4. **Enrich** results with `code_nodes` details (file, kind, signature, language).

## Edge Kinds

- `calls` — function/method call
- `imports` — module/import dependency
- `inherits` — class inheritance
- `uses` — variable/constant usage

## Complexity

- Time: O(E) within the bounded subgraph
- Space: O(V) for visited set + queue
