#include "aux_function.h"
#include "iostream"
#include "vector"

template<typename value_type>
struct State
{
    int n;
    int m;
    value_type maxValue;
    State(int a,int b,value_type c)
        : n(a),m(b),maxValue(c)
    {
    }

};


int N=3;
int M=4;
int main(int argc, char *argv[])
{
    if(argc==2 && std::string(argv[1])=="-h")
    {
        print_help();
    }
    std::vector<std::vector<State<double>>> stats(N);
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;i++)
        {
            stats[i].push_back(State<double(i,j,0));
        }
    }
    std::vector<std::vector<double>> values_matrix(N);
    for(auto values:values_matrix)
    {
        for(int i=0;i<M;i++)
        {
            values.push_back(1);
        }
    }

    return 0;
}
