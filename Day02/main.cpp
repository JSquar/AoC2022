/*
 * File: main.cpp
 * Created: Friday, 2nd December 2022 5:55:06 pm
 * Author: Jannek Squar (jannek.squar@uni-hamburg.de)
 * -----
 *
 * -----
 * Last Modified: Saturday, 3rd December 2022 1:47:10 am
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

TEST(Testsuite_first_part, read) {
  std::string file = "input_small.txt";
  std::list<char> output;
  read_input(file, output);

  std::list<char>::const_iterator citer = output.cbegin();
  EXPECT_EQ('A', *citer);
  EXPECT_EQ('Y', *std::next(citer, 1));
  EXPECT_EQ('B', *std::next(citer, 2));
  EXPECT_EQ('X', *std::next(citer, 3));
  EXPECT_EQ('C', *std::next(citer, 4));
  EXPECT_EQ('Z', *std::next(citer, 5));
}

TEST(Testsuite_first_part, get_single_result) {
  std::string file = "input_small.txt";
  std::list<char> output;
  read_input(file, output);
  std::list<char>::const_iterator citer = output.cbegin();

  EXPECT_EQ(8,
            get_single_result((*std::next(citer, 0)), (*std::next(citer, 1))));
  EXPECT_EQ(1,
            get_single_result((*std::next(citer, 2)), (*std::next(citer, 3))));
  EXPECT_EQ(6,
            get_single_result((*std::next(citer, 4)), (*std::next(citer, 5))));
}

TEST(Testsuite_second_part, get_single_result) {
  std::string file = "input_small.txt";
  std::list<char> output;
  read_input(file, output);
  std::list<char>::const_iterator citer = output.cbegin();

  EXPECT_EQ(4, get_single_result_alternative((*std::next(citer, 0)),
                                             (*std::next(citer, 1))));
  EXPECT_EQ(1, get_single_result_alternative((*std::next(citer, 2)),
                                             (*std::next(citer, 3))));
  EXPECT_EQ(7, get_single_result_alternative((*std::next(citer, 4)),
                                             (*std::next(citer, 5))));
}

TEST(Testsuite_first_part, get_final_result) {
  std::string file = "input_small.txt";
  std::list<char> output;
  read_input(file, output);

  EXPECT_EQ(15, get_all_results(output, &get_single_result));
}

TEST(Testsuite_first_part, final_answer_a) {
  std::string file = "input_big.txt";
  std::list<char> output;
  read_input(file, output);

  EXPECT_EQ(9759, get_all_results(output, &get_single_result));
}

TEST(Testsuite_second_part, final_answer_a) {
  std::string file = "input_big.txt";
  std::list<char> output;
  read_input(file, output);

  EXPECT_EQ(12429, get_all_results(output, &get_single_result_alternative));
}