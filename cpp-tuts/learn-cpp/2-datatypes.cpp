
/*
                                  data types
                              /             \               \
                    primitive               userdefined     derived
        (data types prov by compiler)         |                 |
        /        |    \                     enum              array
      integral  bool  floating              structure         pointer
      /\                  /\                union             reference
    int char         double float            class
*/

/*
  modifiers ==> signed, unsigned, long
*/

int main()
{
  int i; // -32768 to 32767
  char c; // characters
  float f; // float -3.4 x 10^-38 to 3.4 x 10^38
  double d; // double -1.7 x 10^-308 to 1.7 x 10^308.

  float price = 12.75f;
  return 0;
}