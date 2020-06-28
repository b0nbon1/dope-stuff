#ifndef USER_H
#define USER_H

class User
{
  static int user_count;
  std::string status = "Diamond";

  public:
    static int get_user_count();
    std::string first_name;
    std::string last_name;
    std::string get_status();
    void set_status(std::string status);
    // default cons
    User();
    // constructor wit args
    User(std::string first_name, std::string last_name, std::string status);
    // destructor method
    ~User();
    friend void output_status(User user);

    // virtual to enable overrides to child
    virtual void output();
};

#endif
