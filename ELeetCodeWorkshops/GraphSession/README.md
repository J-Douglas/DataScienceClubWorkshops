# E-Leet Coding Workshop

## Summary

This was the workshop I presented for the Waterloo Data Science Club (WDSC) in Fall 2022. This workshop went over the approach and analysis for solving graph LeetCode problems. I first explained the basics of graphs including what is a graph, how they're stored, and the space and time complexity of basic operations involving graphs. Next, I outlined the type of graph questions that may appear in a technical interview. Then, I gave a higher-level description of depth first search and gave the pseudocode for the algorithm. Finally, I presented the [Longest Common Subsequence](https://leetcode.com/problems/number-of-islands/) problem where I discussed the key observations for tackling this problem before going over the implementation with students using DFS.

## Depth First Search (DFS) Approach

For the DFS approach, we first create a visited set and a count of islands variable. We then iterate through every cell in the grid. If the cell is an unvisited land cell, we increment the count of islands variable and call the DFS algorithm. When we call DFS on a land cell, we visit every land cell in the island. Therefore, whenever we visit a land cell that is not visited, we are visiting a new island. In this context, the DFS algorithm is implemented by recursively calling DFS on unvisited adjacent land cells. If you're given a m x n grid, the space and time complexity is O(m x n). You can find the code for the DFS approach [here](https://github.com/J-Douglas/DataScienceClubWorkshops/blob/main/ELeetCodeWorkshop/GraphSession/NumberOfIslands.py). 
