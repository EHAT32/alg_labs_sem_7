#include "iostream"
#include <array>
#include <type_traits>
#include <vcruntime.h>
#include <vcruntime_typeinfo.h>
#include <vector>
#include <algorithm>

template<typename T>
void quickSort(std::vector<T>& vector){
    if (vector.size() <= 1) {
        return;
    }
    else {
        T pivot_element = vector[0];
        std::vector<T> less;
        std::vector<T> greater;
        for (int i = 1; i < vector.size(); i++) {
            if (vector[i] < pivot_element) {
                less.push_back(vector[i]);
            }
            else {
                greater.push_back(vector[i]);
            }
        }
        quicksort(less);
        quicksort(greater);
        for (int i = 0; i < less.size(); i++) {
            vector[i] = less[i];
        }
        vector[less.size()] = pivot_element;
        int offset = less.size() + 1;
        for (int i = 0; i < greater.size(); i++) {
            vector[i + offset] = greater[i];
        }
        less.clear();
        greater.clear();
    }
}

template<typename T>
void heapify(std::vector<T>& vector, const int& heapSize, int i) {
    int largest = i; // Initialize largest as root
    int left = 2 * i + 1; // left = 2*i + 1
    int right = 2 * i + 2; // right = 2*i + 2

    // If left child is larger than root
    if (left < heapSize && vector[left] > vector[largest])
        largest = left;

    // If right child is larger than largest so far
    if (right < heapSize && vector[right] > vector[largest])
        largest = right;

    // If largest is not root
    if (largest != i) {
        std::swap(vector[i], vector[largest]);

        // Recursively heapify the affected sub-tree
        heapify(vector, heapSize, largest);
    }
}

template<typename T>
void heapSort(std::vector<T>& vector) {
    // Build heap (rearrange array)
    int heapSize = vector.size();
    for (int i = heapSize / 2 - 1; i >= 0; i--)
        heapify(vector, heapSize, i);

    // One by one extract an element from heap
    for (int i = heapSize - 1; i >= 0; i--) {
        // Move current root to end
        std::swap(vector[0], vector[i]);

        // call max heapify on the reduced heap
        heapify(vector, i, 0);
    }
}

int main(){
    std::vector<int> vec = {0, 5, 6, 1};
    std::cout << "Initial" << std::endl;
    for (int i: vec) {
        std::cout << i << std::endl;
    }
    heapSort(vec);
    std::cout << "Sorted" << std::endl;
    for (int i: vec) {
        std::cout << i << std::endl;
    } 
    return 0;
};