

struct Rectangle
{
  int length;
  int breadth;
};

void initialize(struct Rectangle *r, int l, int b)
{
  r ->breadth = b;
  r ->length = l;
}

int area(struct Rectangle r)
{
  return r.length * r.breadth;
}

void changeLength(struct Rectangle *r, int l)
{
  r ->length = l;
}

int main()
{
  struct Rectangle r;
  
  initialize(&r, 10, 5);

  area(r);

  changeLength(&r, 20);
}