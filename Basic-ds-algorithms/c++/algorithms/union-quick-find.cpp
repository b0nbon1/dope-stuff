#include <vector>
#include <iostream>

class UF
{
  private:
    std::vector<int> id;
  public:
    UF(int N)
    {
      this->id.reserve(N);
      for(int i = 0; i < N; i++) {
        this->id.push_back(i);
      }
    }

    bool connected(int p, int q) 
    {
      return this->id[p] == this->id[q];
    }
    
    void union_uf(int p, int q)
    {
      int pid = this->id[p];
      int qid = this->id[q];
      for (int i = 0; i < this->id.size(); i++)
        if(this->id[i] == pid) this->id[i] = qid;
    }

    std::vector<int> getArr () {
      return this->id;
    }
};

int main() {
  UF UnionFind(25);
  
  UnionFind.union_uf(2,7); 
  UnionFind.union_uf(2, 21);
  std::vector<int> unio;

  unio = UnionFind.getArr();
  
  for(int i = 0; i < unio.size(); i++) {
    std::cout << unio[i] << std::endl;
  }
  return 0;
}
