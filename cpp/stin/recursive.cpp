#include <iostream>

// explains recursions...
void recurse(int x) {
  if ( x < 0) {
    std::cout << "holla we're here" << std::endl;
    return;
  }

  std::cout << x << " is what is x before" << std::endl;

  recurse(x -1);
  std::cout << x << " is what is x after" << std::endl;
}

// static variables,
/*
we first resolve function stats till the recurse is ove then
we start adding back he static vars or glob vars
which will be constant while adding to the prev result
*/
int stats(int n)
{
  // declare stat var
  static int x = 0;

  // recurse check
  if(n > 0)
  {
    // increment x
    x++;

    /*
      first stats will be run untill the end of the recursion while x being incremented,
      then since `= x` is being called after the recurse func it will be run when recursion is done in ascending
      so let assume n was 2, 
      the tree will be:
              fun(2) => x = 0
                |
              fun(1) => x = 1
                |
              fun(0) => x = 2
    the tracing tree after recurse:
            fun(0) => 0 + 2 = 2
                |
            fun(1) => 2 + 2 = 4
                |
            fun(2) => 4 + 0 = 4
    so ans. will be 4

    general tree trace will be:
              0 ->  1 -> 2
              fun(2) -> 4
                |
              fun(1) -> 2 + 2
                |
              fun(0) -> 0 + 2
    */
    return stats(n - 1) + x;
  }
  std::cout << "holla we're here " << x << std::endl;
  return 0;

}

void tree(int n)
  {
    if(n > 0)
    {
      std::cout << n << " is the n now" << std::endl;
      tree(n-1); // name => f-1 
      tree(n-1); // name => f-2
    }
  }

// types of recursion

/*
   *************Tail recursion******************
   when the recurse function is called as the last fun that's a tail recursion
   example:
   void fun(int n)
   {
     if (n > 0)
     {
       printf("%d ", n);
       fun(n-1);
     }
   }

   return will be => 3,2,1 if n is 3

   *************Head recursion*******************
   all the processing are done after the recurse fun(), the recurse func is always the first to be called.
   the processing are done during returning and not during calling time.
   example:
   void fun(int n)
   {
     if (n > 0)
     {
       fun(n-1);
       printf("%d ", n);
     }
   }

   return will be => 1,2,3 if n is 3
  
  *************Tree Recursion******************
  this one is complex a bit, remember when reading it...
  tree recursion has more than one recursion call in it. 
  there can be two or more recursion in it.
  example:
  void func(int n)
  {
    if(n > 0)
    {
      printf("%d ", n);
      func(n-1); // name => f-1 
      func(n-1); // name => f-2
    }
  }
  explaination => we're going to trace this func using a tree.
  first f-1 is called and as it is called also it printing the value, so calls happens untill the returning time 
  where f-2 is now called but in ascending way while also the f-1 is being called since it's before f-2

  here is the tree for it:
  f => func

                                            func(3)
                                          /\          \
                                         /  \          func(2)
                                        /    \          /\   \
                                       /      \        2 f(1) f(1)
                                      /        \        /\  \  /\  \
                                     /          \      /  \  \1  \  \
                                    /            \    /    \  \   \  f(0)
                           3(what it prints)  func(2)1    f(0)f(0) f(0)
                                             /\     \
                                            /  \     fun(1)
                                           /    \     / \ \
                                          /      \   /   \ \
                                         /        \ 1  f(0) f(0)
                                        2     func(1)
                                                  /\      \
                                                 /  \       \
                                                /    \       \
                                              1   func(0) func(0)

        outputs: 3,2,1,1,2,1,1
                          
*/

int main() {
  // recurse(10);
  // std::cout << stats(2);
  tree(3);

  return 0;
}