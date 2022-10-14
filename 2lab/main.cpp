#include <iostream>
#include <algorithm>

using namespace std; 


void SortBubble3(int * A, int Size)
{
    int j, IndexOfChanged, Low = 0;

    while(Low < Size - 1)
    {
        for(IndexOfChanged = j = Size - 1; j > Low; j--)
        if(A[j-1] > A[j])
        {
            swap(A[j], A[j-1]);
            IndexOfChanged = j;
        }
        Low = IndexOfChanged;
    }
}


void SortMergeAlgoritm(int * A, int Size) 
{
    AH = (Key*)malloc(sizeof(Key)*Size);
    SMerge0(A,0,Size-1);
    free(AH);
}


void Merge(int * A, int Low, int High) 
{
    int Mid;

    if(High <= Low) return;

    Mid = Low + (High - Low)/2;
    
    Merge(A, Low, Mid);
    Merge(A, Mid + 1, High);
    Merge(A, Low, Mid);
}