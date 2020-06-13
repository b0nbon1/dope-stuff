#include <string>
#include <iostream>
#include <cctype>
#include <regex>

// My solution
std::string to_camel_case(std::string text) {
    std::string const delims{ "-_" };
    std::string res;

    size_t beg, pos = 0;
    int rec = 0;
    while ((beg = text.find_first_not_of(delims, pos)) != std::string::npos)
    {
      pos = text.find_first_of(delims, beg + 1);
      std::string temp = text.substr(beg, pos - beg);
      if (rec != 0) temp[0] = toupper(temp[0]);
      res += temp;
      rec++;
    }
    return res;
}

int main(int argc, const char** argv) {
  to_camel_case("the-stealth-warrior");
  return 0;
}

// other solutions from people
std::string to_camel_case1(std::string text)
{
  for(int i = 0; i < text.size(); ++i)
  {
    if(text[i] == '-' || text[i] == '_')
    {
      text.erase(i,1);
      text[i] = toupper(text[i]);
    }
  }
  return text;
}

std::string to_camel_case2(std::string s)
{
  for(int i{0}; i < s.size(); ++i)
    if(s[i] == '-' || s[i] == '_')
      s.erase(i, 1), s[i] = toupper(s[i]);
  return s;
}

std::string to_camel_case3(std::string text) {
  std::regex reg("\\W|_");
  
  for (std::sregex_iterator it = std::sregex_iterator(text.begin(), text.end(), reg); it != std::sregex_iterator(); it++)
  {
    std::smatch match = *it;
    text[match.position()+1] = std::toupper(text[match.position()+1], std::locale());
  }
  
  return std::regex_replace(text, reg, "");
}

std::string to_camel_case4(const std::string & text)
{
    std::string result;
    result.reserve(text.length());

    bool capital = false;

    for (auto c : text)
    {    
        // any non-alphanumeric character causes the next one to be upper-case
        if (!std::isalpha(c))
        {
            capital = true;
        }
        
        // this character should be upper case if the "capital" flag is set or if
        // it's already an upper-case character
        else if (capital || std::isupper(c))
        {
            result.push_back(std::toupper(c));
            capital = false; // unset the "capital" flag after emitting the character
        }
        
        // anything else is emitted as lower case
        else
        {
            result.push_back(std::tolower(c));
        }
    }
    
    return result;
}