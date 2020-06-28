#include <iostream>
#include <string>
#include <vector>
#include "user.h"


int User::get_user_count()
{
  return user_count;
}

std::string User::get_status()
{
  return status;
}

void User::set_status(std::string status)
{
  if(status == "Gold" || status == "Silver" || status == "Bronze")
  {
    this->status = status;
  }
}

// default cons
User::User()
{
  std::cout << "Constructor \n";
  user_count++;
}

// constructor wit args
User::User(std::string first_name, std::string last_name, std::string status)
{
  this->first_name = first_name;
  this->last_name = last_name;
  this->status = status;
  user_count++;
}
// destructor method
User::~User()
{
  // std::cout << "Destructor \n";
  user_count--;
}

void User::output()
{
  std::cout << "I am a User \n";
}

// friend function
void output_status(User user)
{
  std::cout << user.status << std::endl;
}

int User::user_count = 0;

int add_user_if_not_exists(std::vector<User> &users, User user)
{
  for(int i = 0; i < users.size(); i++)
  {
    if(users[i].first_name == user.first_name &&
      users[i].last_name == user.last_name)
    {
      return i;
    }
  }
  users.push_back(user);
  return users.size() - 1;
}
