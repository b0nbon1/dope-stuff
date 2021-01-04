#include <gtest/gtest.h>
#include "array.hpp"

TEST( Arrays, Test_append){
  Array<int> arr;
  arr.append(5);
  arr.append(6);
  arr.append(7);
  EXPECT_EQ(arr[2], 7);
}

TEST( Arrays, Test_prepend){
  Array<int> arr;
  arr.append(5);
  arr.append(6);
  arr.append(7);
  arr.prepend(8);
  EXPECT_EQ(arr[0], 8);
}

TEST( Arrays, Test_insertAt){
  Array<int> arr;
  arr.append(5);
  arr.append(6);
  arr.insertAt(3, 0);
  EXPECT_EQ(arr[0], 3);
}

TEST( Arrays, Test_deleteAt){
  Array<int> arr;
  arr.append(5);
  arr.append(6);
  arr.deleteAt(0);
  EXPECT_EQ(arr[0], 6);
}

TEST( Arrays, Test_length){
  Array<int> arr;
  arr.append(5);
  arr.append(6);
  EXPECT_EQ(arr.length(), 2);
}
