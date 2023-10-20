#include <cmath>
#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

float dist(const vector<int>& cityA, const vector<int>& cityB){
    float distance = std::sqrt(std::pow((cityA[0] - cityB[0]), 2) + std::pow((cityA[1] - cityB[1]), 2));
    return distance;
}

vector<vector<float>> createGraph(const vector<vector<int>>& citiesVector){
    vector<vector<float>> graph;
    for (int i = 0; i < citiesVector.size(); i++) {
        vector<float> row;
        for (int j = 0; j < citiesVector.size(); j++) {
            row.push_back(dist(citiesVector[i], citiesVector[j]));
        }
        graph.push_back(row);
        row.clear();
    }
    return graph;
}

float tsp(const vector<vector<float>>& cities) {
    int n = cities.size();
    float memo[1 << n][n];
    
    // Initialize memoization table
    for (int i = 0; i < (1 << n); i++) {
        for (int j = 0; j < n; j++) {
            memo[i][j] = -1;
        }
    }
    for (int i = 0; i < n; i++) {
        memo[1 << i][i] = 0;
    }
    
    // Fill in memoization table
    for (int s = 1; s < (1 << n); s++) {
        for (int i = 0; i < n; i++) {
            if ((s & (1 << i)) == 0) continue;
            for (int j = 0; j < n; j++) {
                if (i == j || (s & (1 << j)) == 0) continue;
                int prev = s ^ (1 << i);
                if (memo[prev][j] == -1) continue;
                float dist = memo[prev][j] + cities[j][i];
                if (memo[s][i] == -1 || dist < memo[s][i]) {
                    memo[s][i] = dist;
                }
            }
        }
    }
    
    // Find shortest route
    float minDist = -1;
    for (int i = 0; i < n; i++) {
        if (minDist == -1 || memo[(1 << n) - 1][i] < minDist) {
            minDist = memo[(1 << n) - 1][i];
        }
    }
    return minDist;
}

int main() {
    // Define the problem
    vector<vector<int>> cities = {
        {1, 4},
        {2, 5},
        {10, 2},
    };
    auto graph = createGraph(cities);
    // Solve the problem using dynamic programming
    float minDistance = tsp(graph);
    
    // Print the shortest distance
    cout << "Shortest distance: " << minDistance << endl;
    
    return 0;
}
