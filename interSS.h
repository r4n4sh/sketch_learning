#ifndef SPACESAVING_H
#define SPACESAVING_H

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
 #include <climits>
#include <unordered_map>
#define newline "\n"
using namespace std;


struct Statistics
{
    double average;
    int max;
    int onceArrcount;
    Statistics(double a, int b, int c)
    {
        average = a;
        max = b;
        onceArrcount = c;
    }
};

struct Node
{
    string id;
    int inter, ts, error, index;

    // constructor
    Node(string a, int b, int c, int d, int t)
    {
        id = a;
        inter = b;
        ts = t;
        error = c;
        index = d;
    }
};

template class std::unordered_map<string, Node *>;

typedef unordered_map<string, Node *> umsn;
typedef vector<Node *> vn;

class SpaceSaving
{
private:
    vn minHeap;                                                 // data structure for the summary
    int k;                                                      // capacity of heap
    umsn dict;                                                  // keys on heap
    int ts;                                                     // timestamp

public:
    SpaceSaving(int capacity);                                  // constructor
    ~SpaceSaving();                                             // destructor

    void swap(Node *a, Node *b);                                // swap two nodes

    int parent(int i) { return (i - 1) / 2; }                   // to get index of parent of node at index i
    int left(int i) { return (2 * i + 1); }                     // to get index of left child of node at index i
    int right(int i) { return (2 * i + 2); }                    // to get index of right child of node at index i

    void spaceSaving(string id);                                // main algorithm
    void updateHeap(int i);
    void print();                                               // print the stream summary
    int interArrival(string id);                                // Query inter arrival of id
    Statistics statisticInterArr();                             // Statistic interArr 
};

#endif // SPACESAVING_H