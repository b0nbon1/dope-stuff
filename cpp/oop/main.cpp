#include <iostream>
#include <string>
#include <vector>
#include "user.h"
#include "teacher.h"

int main()
{
  // User me;
  // me.first_name = "Bonvic";
  // me.last_name = "Bundi";
  // me.get_status();

  // std::vector<User> users;
  // users.push_back(me);

  // User user1, user2, user3;
  // user1.first_name = "Bon";
  // user1.last_name = "Vic";

  // user1.first_name = "Vic";
  // user1.last_name = "Bundi";

  // user1.first_name = "Bon";
  // user1.last_name = "Bundi";
  // users.push_back(user1);
  // users.push_back(user2);
  // users.push_back(user3);

  // User user;
  // user.first_name = "Vesh";
  // user.last_name = "Nje";
  // add_user_if_not_exists(users, user)

  User user("Bonvic", "Bundi", "Diamond");

  std::cout <<  user.get_status() << std::endl;

  User user1, user2, user3, user4;
  std::cout <<  User::get_user_count() << std::endl;

  user.~User();
  std::cout <<  User::get_user_count() << std::endl;

  Teacher teacher;
  User& u = teacher;
  u.output();

  return 0;
}