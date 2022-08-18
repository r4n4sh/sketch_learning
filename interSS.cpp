#include "interSS.h"

// constructor
SpaceSaving::SpaceSaving(int capacity)
{
    k = capacity;
    minHeap.resize(k, nullptr);

    // initialize the min-heap with k dummy entries
    for (int i = 0; i < k; i++)
    {
        Node *n = new Node("dummy", INT_MAX, INT_MAX, i, 0);
        minHeap[i] = n;
    }
    ts = 0;
}

// destructor
SpaceSaving::~SpaceSaving()
{
    for (auto &&i : minHeap)
    {
        delete i;
    }
    minHeap.clear();
    dict.clear();
}

// swap the values of two nodes
void SpaceSaving::swap(Node *a, Node *b)
{
    Node *tmp1 = new Node(a->id, a->inter, a->error, a->index, a->ts);
    Node *tmp2 = new Node(b->id, b->inter, b->error, b->index, b->ts);

    a->id = tmp2->id, a->inter = tmp2->inter, a->ts = tmp2->ts, a->error = tmp2->error;
    b->id = tmp1->id, b->inter = tmp1->inter, b->ts = tmp1->ts, b->error = tmp1->error;

    if (dict.find(tmp1->id) != dict.end())
    {
        dict[tmp1->id] = b;
    }

    if (dict.find(tmp2->id) != dict.end())
    {
        dict[tmp2->id] = a;
    }
}

// main algorithm
void SpaceSaving::spaceSaving(string id)
{
    ++ts;

    // increment the weight of input if it is on the heap
    if (dict.find(id) != dict.end())
    {
    //    std::cout << "Updating inter arrival of: "<< id << " from: " << dict[id]->inter << " to: " << ts - dict[id]->ts << " last TS: " << dict[id]->ts << std::endl;
        dict[id]->inter = ts - dict[id]->ts;
        dict[id]->ts = ts;
        int i = dict[id]->index;
        updateHeap(i);
    }
    // o.w. replace the maximum with the new input
    else
    {

        Node *max = minHeap[0];

        if (max->id != "dummy")
        {
            dict.erase(max->id);

            // insert new input on dictionary and minHeap
            //std::cout << "take place of the max, max interarrival is: "<< max->inter << ", INT_MAX: " << INT_MAX << std::endl;
            int newts;
            if (max->inter == INT_MAX) {
                newts = INT_MAX -1;
            } else {
                newts = max->inter;
            }

            Node *n = new Node(id, newts, newts, 0, ts);
            minHeap[0] = n;
            dict[id] = n;

            // we will always delete minHeap[0]
            // instead of actually deleting it, insert the new element in this position
            updateHeap(0);
        }
        else
        {
            Node *n = new Node(id, INT_MAX - 1 , INT_MAX- 1, 0, ts);// We enter a large value of interarrival since we want to nominate items with only ONE arrival, but we substract 1 from their value to give them a chance
            minHeap[0] = n;
            dict[id] = n;
            updateHeap(0);
        }
    }
}

void SpaceSaving::updateHeap(int i){
    // maximum index = k - 1
    while (left(i) < k || right(i) < k)
    {
        int curr = minHeap[i]->inter;

        if (left(i) < k && right(i) < k)
        {
            int leftChild = minHeap[left(i)]->inter;
            int rightChild = minHeap[right(i)]->inter;
            int largerChild = (leftChild <= rightChild) ? rightChild : leftChild;
            int largerChildIndex = (leftChild <= rightChild) ? right(i) : left(i);

            // swap with the larger child
            if (curr < largerChild)
            {
                swap(minHeap[i], minHeap[largerChildIndex]);
                i = largerChildIndex;
            }
            else
            {
                break;
            }
        }
        else if (left(i) < k)
        {
            int largerChild = minHeap[left(i)]->inter;
            int largerChildIndex = left(i);

            if (curr < largerChild)
            {
                swap(minHeap[i], minHeap[largerChildIndex]);
                i = largerChildIndex;
            }
            else
            {
                break;
            }
        }
        else
        {
            std::cout << "Should not run into this case" << std::endl;
            // this case needs attention for further debugging
            if (curr < minHeap[right(i)]->inter)
            {
                swap(minHeap[i], minHeap[right(i)]);
                i = right(i);
            }
            else
            {
                break;
            }
        }
    }
}


int SpaceSaving::interArrival(string id)
{
    ++ts;
    if (dict.find(id) != dict.end())
    {
        return dict[id]->inter;
    } else {
        int i = 0;
        while(minHeap[i]->inter == INT_MAX - 1) i++;
        std::cout << "Inter arrival of NON existing item: " << id << std::endl;
        Node *max = minHeap[i];
        return max->inter;
    }
}

// print the min-Heap
void SpaceSaving::print()
{
    for (int i = 0; i < k; i++)
    {
        cout << "Item: " << minHeap[i]->id << "; ";
        cout << "Inter arrival time: " << minHeap[i]->inter << "\n";
    //    cout << "Error: " << minHeap[i]->error << "\n";
    }
}


// print the min-Heap
Statistics SpaceSaving::statisticInterArr()
{
    int sum = 0;
    int max = 0;
    int onceArrcount = 0;
    for (int i = 0; i < k; i++)
    {
        if (minHeap[i]->inter != INT_MAX - 1) {
            sum += minHeap[i]->inter;
            if (minHeap[i]->inter > max)
                max = minHeap[i]->inter;
        }
        else {
            ++onceArrcount;
        }
    }

    double average = (double) sum / (double) k ;

    std::cout << average << "," << max;
    Statistics stat(average, max, onceArrcount);
    return stat;
}