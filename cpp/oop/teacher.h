#ifndef TEACHER_H
#define TEACHER_H

#include <vector>
#include <string>
#include <iostream>
#include "user.h"

class Teacher : public User
{
  public:
    std::vector<std::string> classes_teaching;
    Teacher();
    void output();
};

#endif