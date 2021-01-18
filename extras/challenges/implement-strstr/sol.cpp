#include <bits/stdc++.h>

using namespace std;

void fill_lsp(vector<int> &lsp, string pattern, int size)
{
  int i = 1, j = 0;

  while (i < size)
  {
    if (pattern[i] == pattern[j])
      lsp[i++] = ++j;
    else
    {
      if (j != 0)
        j = lsp[j - 1];
      else
        lsp[i++] = 0;
    }
  }
}

int strStr(string haystack, string needle)
{
  int lenh = haystack.length(), lenn = needle.length(), i, j;

  /* Edge cases */
  if (lenn == 0)
    return 0;
  if (lenn > lenh)
    return -1;

  /* KMP Algorithm - familiarize and this will be easy to understand. */
  vector<int> lsp(lenn);
  fill_lsp(lsp, needle, lenn);

  for (size_t i = 0; i < lsp.size(); i++)
  {
    cout << lsp[i] << "\t";
  }
  cout << endl;
  

  i = 0;
  j = 0;
  while (i < lenh)
  {
    if (haystack[i] == needle[j])
    {
      i++;
      j++;
      /* Found substring */
      if (j >= lenn)
        return i - j;
    }
    else
    {
      if (j != 0)
        j = lsp[j - 1];
      else
        i++;
    }
  }

  /* No needle is found while traversing the haystack */
  return -1;
}

int main() {

  strStr("hnlnlmlello", "llo");
  return 0;
}