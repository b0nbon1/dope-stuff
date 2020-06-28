#include <iostream>
#include <string>
#include <vector>

class User
{
  static int user_count;
  std::string status = "Diamond";

  public:
    static int get_user_count()
    {
      return user_count;
    }
    std::string first_name;
    std::string last_name;
    std::string get_status()
    {
      return status;
    }
    void set_status(std::string status)
    {
      if(status == "Gold" || status == "Silver" || status == "Bronze")
      {
        this->status = status;
      }
    }
    // default cons
    User()
    {
      std::cout << "Constructor \n";
      user_count++;
    }
    // constructor wit args
    User(std::string first_name, std::string last_name, std::string status)
    {
      this->first_name = first_name;
      this->last_name = last_name;
      this->status = status;
      user_count++;
    }
    // destructor method
    ~User()
    {
      std::cout << "Destructor \n";
      user_count--;
    }
    friend void output_status(User user);
};

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
  return 0;
}