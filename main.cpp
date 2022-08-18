#include "interSS.h"
#include <cmath> 
#include <ctime>
#include <fstream>


typedef struct pkt_data PKTDATA;


struct pkt_data 
{
  unsigned int count;
  unsigned long int lastpkt;
  unsigned long int inter_arrival;
};

int main(int argc, char const *argv[])
{
    std::unordered_map<string, PKTDATA> countersMap;// key (flow id) , counter
    int ts = 0;

    if (argc != 3)
    {
        cerr << "Error: Expected 3 Arguments" << endl;
        exit(1);
    }

    vector<string> input;

    ifstream ifs;
    ifs.open(argv[1]);
    if (!ifs)
    {
        cerr << "Open Failed" << endl;
        exit(1);
    }

    string line;
    while (true)
    {
        getline(ifs, line);
        if (!ifs)
        {
            break;
        }
        input.push_back(line);
    }

    int capacity = stoi(argv[2]);
    SpaceSaving obj(capacity);

    clock_t t;
    t = clock();
    for (auto &&id : input)
    {
        obj.spaceSaving(id);

        //Exact calculation
        ++ts;
        unsigned long int tmplast = countersMap[id].lastpkt;
        countersMap[id].inter_arrival = (ts - tmplast);
        countersMap[id].lastpkt = ts;
    }
    t = clock() - t;

    double time = ((double)t) / CLOCKS_PER_SEC;

    cout << "Running time: " << 1e9 * time/input.size() << " nanoseconds." << "\n";
    cout << "\n";

    double curr_err = 0;
    double emp_err = 0;
    int exactCouter = 0;

    for (auto &&id : input)
    {
        int estInter = obj.interArrival(id);
        int exactInter = countersMap[id].inter_arrival;
        if (exactInter == estInter) {
            ++exactCouter;
        } else {
            std::cout << "exact: " << exactInter << ", est: " << estInter << ", error: " << abs(exactInter - estInter) << std::endl;
        }

        curr_err = exactInter - estInter;
        curr_err = pow(curr_err, 2);
        emp_err += curr_err;


    }

    obj.print();

    emp_err = sqrt((emp_err/ts));
    Statistics stat = obj.statisticInterArr();
    std::cout << "Empirical Error: " << emp_err << ", exact answers: " << exactCouter << std::endl;
    std::cout << "Average interArr: " << stat.average << ", max interArr: " << stat.max << ", once arrival count: " << stat.onceArrcount << std::endl;

    return 0;
}
