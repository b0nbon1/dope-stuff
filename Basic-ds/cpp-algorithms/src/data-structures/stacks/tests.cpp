#include <gtest/gtest.h>
#include "stack.hpp"

TEST( StackArray, Test_push_Stacktop){
  StackArray<int> stack;
  stack.push(12);
  stack.push(19);

  EXPECT_EQ(stack.peek(), 19);
}

TEST( StackArray, Test_pop){
  StackArray<int> stack;
  stack.push(12);
  stack.push(19);

  EXPECT_EQ(stack.pop(), 19);
}

TEST( StackArray, Test_peek){
  StackArray<int> stack;
  stack.push(12);
  stack.push(19);

  EXPECT_EQ(stack.peek(), 19);
}

TEST( StackArray, Test_isEmpty){
  StackArray<int> stack;

  EXPECT_TRUE(stack.isEmpty());
}

TEST( StackArray, Test_notiIsEmpty){
  StackArray<int> stack;
  stack.push(19);

  EXPECT_FALSE(stack.isEmpty());
}
