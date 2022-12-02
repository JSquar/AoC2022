/*
 * File: main.cpp
 * Created: Friday, 2nd December 2022 5:55:06 pm
 * Author: Jannek Squar (jannek.squar@uni-hamburg.de)
 * -----
 *
 * -----
 * Last Modified: Friday, 2nd December 2022 7:32:54 pm
 * Modified By: Jannek Squar (jannek.squar@uni-hamburg.de)
 * -----
 * Copyright (c) 2022 Jannek Squar
 *
 */

// Build with g++ -lgtest -o main.x main.cpp RPS.cpp

#include "RPS.h"
#include <gtest/gtest.h>
#include <list>
#include <string>

int main(int argc, char *argv[]) {
  ::testing::InitGoogleTest();
  return RUN_ALL_TESTS();
}

TEST(Testsuite, input_small) {
  std::string file = "input_small.txt";
  std::list<std::string> output;
  read_input(file, output);

  //   for (std::list<std::string>::iterator &iter : output) {
  std::cout << "Hallo Welt! " << output.size() << "\n";
  for (std::string iter : output) {
    std::cout << iter << std::endl;
  }
}