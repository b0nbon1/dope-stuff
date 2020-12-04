class Rectangle
{
  private:
    int length;
    int breadth;
  public:
    void initialize(int l, int b)
    {
      breadth = b;
      length = l;
    }

    int area()
    {
      return length * breadth;
    }

    void changeLength(int l)
    {
      length = l;
    }
};

int main()
{
  Rectangle r;
  
  r.initialize(10, 5);

  r.area();

  r.changeLength(20);
}
