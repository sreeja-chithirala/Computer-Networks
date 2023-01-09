#include<iostream>
using namespace std;

#define INT_MAX 9999
#define N 5
  
int minDist(int dist[],bool set[])
{
	int min= INT_MAX,min_index;
	for(int v=0;v<N;v++)
	if(set[v]==false && dist[v]<=min)
	
	min=dist[v],min_index=v;
    
    return min_index;
}

int printsol(int dist[], int n)
{
  cout<<"Vertex Distance from Source\n";
  for (int i = 0; i < N; i++)
  {
    cout<<"\t\n"<< i<<"\t"<<dist[i];
  }
  return 0;
}

  

void dijkstra(int g[N][ N],int src)
{  
    int i ;
	int dist[N];
	bool set[N];
	for(i=0;i<N;i++)
	
		dist[i]= INT_MAX,set[i]=false;
     	dist[src]=0;
	for(int c=0;c<N-1;c++)
	{
		int u=minDist(dist,set);
		set[u]=true;
		
		
		for(int v=0;v<N;v++)
		
		
		if(!set[v]&& g[u][v]&&dist[u]!= INT_MAX && dist[u]+g[u][v]<dist[v])
		  {
		    dist[v]=dist[u]+g[u][v];
     	  }
	
    	
   
  }
  printsol(dist,N);
}

int main()
{
	 
	int G[N][N], i, j ;
	 
	 cout<<"Enter the adjacency matrix: "<<endl;
	 
	for(i=0;i < N;i++)
	
	{
		for(j=0;j < N;j++)
		{
			 cin>>G[i][j];
        }
		cout<<endl;
}
	dijkstra(G,0);
	 
return 0 ;
}
