#include <bits/stdc++.h>

using namespace std;

bool isValid(string s)
{
  stack<char> st;

  for (auto i = 0; i < s.size(); i++)
  {
    if (s[i] == '(' || s[i] == '{' || s[i] == '[')
    {
      st.push(s[i]);
      continue;
    }

    if (st.empty())
      return false;

    if (s[i] == ')' && st.top() != '(')
      return false;
    if (s[i] == '}' && st.top() != '{')
      return false;
    if (s[i] == ']' && st.top() != '[')
      return false;
    st.pop();
  }

  return st.empty() ? 1 : 0;
}

int main()
{
  isValid("([)]");
  return 0;
}