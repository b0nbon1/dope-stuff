#include <iostream>
#include <string>

struct User
{
  std::string firstname;
  std::string last_name;
  std::string get_status()
  {
    return status;
  }
  private:
    std::string status = "Diamond";
};


int main()
{
  User me;
  me.firstname = "Bonvic";
  me.last_name = "Bundi";
  me.get_status();
  return 0;
}